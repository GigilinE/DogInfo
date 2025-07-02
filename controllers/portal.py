from odoo import http, fields, _, tools
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.exceptions import AccessError, MissingError, ValidationError
import logging

_logger = logging.getLogger(__name__)


class CustomerPortalExtended(CustomerPortal):
    
    OPTIONAL_BILLING_FIELDS = CustomerPortal.OPTIONAL_BILLING_FIELDS + [
        'dog_name', 'dog_breed', 'dog_age', 'dog_weight'
    ]
    
    @http.route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        """Override del metodo account per gestire i campi del cane"""
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        values.update({
            'error': {},
            'error_message': [],
        })

        if post and request.httprequest.method == 'POST':
            error, error_message = self.details_form_validate(post)
            values.update({'error': error, 'error_message': error_message})
            values.update(post)
            
            if not error:
                # Prepara i valori da salvare
                values_to_update = {key: post[key] for key in self.MANDATORY_BILLING_FIELDS if key in post}
                values_to_update.update({key: post[key] for key in self.OPTIONAL_BILLING_FIELDS if key in post})
                
                # Gestione speciale per i campi numerici del cane
                if 'dog_age' in values_to_update:
                    try:
                        age_value = values_to_update['dog_age']
                        if age_value and age_value.strip():
                            values_to_update['dog_age'] = int(age_value)
                        else:
                            values_to_update['dog_age'] = False
                    except (ValueError, TypeError):
                        values_to_update['dog_age'] = False
                
                if 'dog_weight' in values_to_update:
                    try:
                        weight_value = values_to_update['dog_weight']
                        if weight_value and weight_value.strip():
                            values_to_update['dog_weight'] = float(weight_value)
                        else:
                            values_to_update['dog_weight'] = False
                    except (ValueError, TypeError):
                        values_to_update['dog_weight'] = False
                
                # Filtra i valori vuoti
                for field in ['dog_name', 'dog_breed']:
                    if field in values_to_update and values_to_update[field] == '':
                        values_to_update[field] = False
                
                # Aggiorna il partner
                partner.sudo().write(values_to_update)
                
                if redirect:
                    return request.redirect(redirect)
                return request.redirect('/my/home')

        # Prepara i valori per il template
        countries = request.env['res.country'].sudo().search([])
        states = request.env['res.country.state'].sudo().search([])

        values.update({
            'partner': partner,
            'countries': countries,
            'states': states,
            'has_check_vat': hasattr(request.env['res.partner'], 'check_vat'),
            'redirect': redirect,
            'page_name': 'my_details',
            # Aggiungi esplicitamente i valori dei campi del cane
            'dog_name': partner.dog_name or '',
            'dog_breed': partner.dog_breed or '',
            'dog_age': partner.dog_age or '',
            'dog_weight': partner.dog_weight or '',
        })

        response = request.render("portal.portal_my_details", values)
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['Content-Security-Policy'] = "frame-ancestors 'self'"
        return response
    
    def details_form_validate(self, data):
        """Override per validare anche i campi del cane"""
        error, error_message = super(CustomerPortalExtended, self).details_form_validate(data)
        
        # Validazione età del cane
        if 'dog_age' in data and data['dog_age']:
            try:
                age = int(data['dog_age'])
                if age < 0 or age > 30:
                    error['dog_age'] = 'wrong'
                    error_message.append(_('L\'età del cane deve essere tra 0 e 30 anni.'))
            except (ValueError, TypeError):
                if data['dog_age'].strip():  # Solo se non è vuoto
                    error['dog_age'] = 'wrong'
                    error_message.append(_('L\'età del cane deve essere un numero intero.'))
        
        # Validazione peso del cane
        if 'dog_weight' in data and data['dog_weight']:
            try:
                weight = float(data['dog_weight'])
                if weight < 0 or weight > 200:
                    error['dog_weight'] = 'wrong'
                    error_message.append(_('Il peso del cane deve essere tra 0 e 200 kg.'))
            except (ValueError, TypeError):
                if data['dog_weight'].strip():  # Solo se non è vuoto
                    error['dog_weight'] = 'wrong'
                    error_message.append(_('Il peso del cane deve essere un numero.'))
        
        return error, error_message