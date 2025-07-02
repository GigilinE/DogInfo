# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal

class CustomerPortalDog(CustomerPortal):

    def _prepare_portal_layout_values(self):
        values = super()._prepare_portal_layout_values()
        # Aggiungi i campi del cane al contesto
        partner = request.env.user.partner_id
        values.update({
            'x_studio_dog_name': partner.x_studio_dog_name if hasattr(partner, 'x_studio_dog_name') else '',
            'x_studio_dog_breed': partner.x_studio_dog_breed if hasattr(partner, 'x_studio_dog_breed') else '',
            'x_studio_dog_age': partner.x_studio_dog_age if hasattr(partner, 'x_studio_dog_age') else 0,
            'x_studio_dog_weight': partner.x_studio_dog_weight if hasattr(partner, 'x_studio_dog_weight') else 0.0,
        })
        return values

    @http.route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        if post and request.httprequest.method == 'POST':
            # Gestisci l'aggiornamento dei campi del cane
            partner = request.env.user.partner_id
            values = {}
            
            # Prima gestisci i campi standard con il metodo parent
            response = super().account(redirect=redirect, **post)
            
            # Poi aggiorna i campi del cane se esistono
            if hasattr(partner, 'x_studio_dog_name') and 'x_studio_dog_name' in post:
                values['x_studio_dog_name'] = post.get('x_studio_dog_name')
            if hasattr(partner, 'x_studio_dog_breed') and 'x_studio_dog_breed' in post:
                values['x_studio_dog_breed'] = post.get('x_studio_dog_breed')
            if hasattr(partner, 'x_studio_dog_age') and 'x_studio_dog_age' in post:
                try:
                    values['x_studio_dog_age'] = int(post.get('x_studio_dog_age', 0))
                except ValueError:
                    values['x_studio_dog_age'] = 0
            if hasattr(partner, 'x_studio_dog_weight') and 'x_studio_dog_weight' in post:
                try:
                    values['x_studio_dog_weight'] = float(post.get('x_studio_dog_weight', 0.0))
                except ValueError:
                    values['x_studio_dog_weight'] = 0.0
            
            if values:
                partner.sudo().write(values)
            
            return response
        
        return super().account(redirect=redirect, **post)