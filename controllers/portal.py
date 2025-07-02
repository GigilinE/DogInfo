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
        
        # Aggiungi i campi del cane al contesto
        values.update({
            'x_studio_dog_name': partner.x_studio_dog_name if hasattr(partner, 'x_studio_dog_name') else '',
            'x_studio_dog_breed': partner.x_studio_dog_breed if hasattr(partner, 'x_studio_dog_breed') else '',
            'x_studio_dog_age': partner.x_studio_dog_age if hasattr(partner, 'x_studio_dog_age') else 0,
            'x_studio_dog_weight': partner.x_studio_dog_weight if hasattr(partner, 'x_studio_dog_weight') else 0.0,
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
            
            # Estrai i campi dog se esistono
            for field_name in ['x_studio_dog_name', 'x_studio_dog_breed', 'x_studio_dog_age', 'x_studio_dog_weight']:
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
                
                if 'x_studio_dog_name' in dog_fields:
                    update_values['x_studio_dog_name'] = dog_fields['x_studio_dog_name'] or False
                
                if 'x_studio_dog_breed' in dog_fields:
                    update_values['x_studio_dog_breed'] = dog_fields['x_studio_dog_breed'] or False
                
                if 'x_studio_dog_age' in dog_fields:
                    try:
                        update_values['x_studio_dog_age'] = int(dog_fields['x_studio_dog_age']) if dog_fields['x_studio_dog_age'] else False
                    except ValueError:
                        update_values['x_studio_dog_age'] = False
                
                if 'x_studio_dog_weight' in dog_fields:
                    try:
                        update_values['x_studio_dog_weight'] = float(dog_fields['x_studio_dog_weight']) if dog_fields['x_studio_dog_weight'] else False
                    except ValueError:
                        update_values['x_studio_dog_weight'] = False
                
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