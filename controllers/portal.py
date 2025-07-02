# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
import logging

_logger = logging.getLogger(__name__)


class CustomerPortalExtended(CustomerPortal):
    
    def _prepare_portal_layout_values(self):
        """Override per aggiungere i campi dog al contesto del template"""
        values = super()._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        
        # Aggiungi i campi del cane al contesto con i nomi corretti
        values.update({
            'dog_name': partner.dog_name if hasattr(partner, 'dog_name') else '',
            'dog_breed': partner.dog_breed if hasattr(partner, 'dog_breed') else '',
            'dog_age': partner.dog_age if hasattr(partner, 'dog_age') else 0,
            'dog_weight': partner.dog_weight if hasattr(partner, 'dog_weight') else 0.0,
        })
        return values

    @http.route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        """Override per gestire l'aggiornamento dei campi dog"""
        partner = request.env.user.partner_id
        
        if post and request.httprequest.method == 'POST':
            _logger.info(f"Received POST data: {list(post.keys())}")
            
            # Separa i campi dog dai campi standard
            dog_fields = {}
            standard_post = post.copy()
            
            # Estrai i campi dog se esistono (con i nomi corretti)
            for field_name in ['dog_name', 'dog_breed', 'dog_age', 'dog_weight']:
                if field_name in post and hasattr(partner, field_name):
                    dog_fields[field_name] = standard_post.pop(field_name)
            
            # Prima gestisci i campi standard con il metodo parent
            try:
                response = super().account(redirect=redirect, **standard_post)
            except Exception as e:
                _logger.error(f"Error in parent account method: {e}")
                # Se fallisce il parent, gestisci solo i campi dog
                values = self._prepare_portal_layout_values()
                response = request.render("portal.portal_my_details", values)
            
            # Poi aggiorna i campi del cane se ci sono
            if dog_fields:
                update_values = {}
                
                if 'dog_name' in dog_fields:
                    update_values['dog_name'] = dog_fields['dog_name'] or False
                
                if 'dog_breed' in dog_fields:
                    update_values['dog_breed'] = dog_fields['dog_breed'] or False
                
                if 'dog_age' in dog_fields:
                    try:
                        update_values['dog_age'] = int(dog_fields['dog_age']) if dog_fields['dog_age'] else False
                    except ValueError:
                        update_values['dog_age'] = False
                
                if 'dog_weight' in dog_fields:
                    try:
                        update_values['dog_weight'] = float(dog_fields['dog_weight']) if dog_fields['dog_weight'] else False
                    except ValueError:
                        update_values['dog_weight'] = False
                
                # Aggiorna il partner con i campi dog
                if update_values:
                    try:
                        partner.sudo().write(update_values)
                        _logger.info(f"Successfully updated dog fields: {update_values}")
                    except Exception as e:
                        _logger.error(f"Error updating dog fields: {e}")
            
            return response
        
        # GET request - carica normalmente la pagina
        return super().account(redirect=redirect, **post)