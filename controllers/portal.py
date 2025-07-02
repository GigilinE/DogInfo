from odoo import http, fields, _, tools
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.exceptions import AccessError, MissingError, ValidationError
import logging

_logger = logging.getLogger(__name__)


class CustomerPortalExtended(CustomerPortal):
    
    # Extend OPTIONAL_BILLING_FIELDS to include dog fields
    OPTIONAL_BILLING_FIELDS = CustomerPortal.OPTIONAL_BILLING_FIELDS + [
        'dog_name', 'dog_breed', 'dog_age', 'dog_weight'
    ]
    
    def details_form_validate(self, data):
        """Override to add validation for dog fields"""
        error, error_message = super().details_form_validate(data)
        
        # Add validation for dog fields
        if data.get('dog_age'):
            try:
                age = int(data['dog_age'])
                if age < 0 or age > 30:
                    error['dog_age'] = 'Age must be between 0 and 30'
                    error_message.append('Invalid dog age')
            except ValueError:
                error['dog_age'] = 'Age must be a number'
                error_message.append('Invalid dog age format')
        
        if data.get('dog_weight'):
            try:
                weight = float(data['dog_weight'])
                if weight < 0 or weight > 200:
                    error['dog_weight'] = 'Weight must be between 0 and 200 kg'
                    error_message.append('Invalid dog weight')
            except ValueError:
                error['dog_weight'] = 'Weight must be a number'
                error_message.append('Invalid dog weight format')
        
        return error, error_message
    
    @http.route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        """Override del metodo account per gestire i campi del cane"""
        # IMPORTANTE: Chiamare super() per mantenere il comportamento standard
        response = super(CustomerPortalExtended, self).account(redirect, **post)
        
        # Se è una risposta renderizzata, aggiungi i valori dei campi custom
        if hasattr(response, 'qcontext'):
            partner = request.env.user.partner_id
            # Aggiungi esplicitamente i valori dei campi custom
            response.qcontext.update({
                'dog_name': post.get('dog_name', partner.dog_name or ''),
                'dog_breed': post.get('dog_breed', partner.dog_breed or ''),
                'dog_age': post.get('dog_age', partner.dog_age or ''),
                'dog_weight': post.get('dog_weight', partner.dog_weight or ''),
            })
        
        return response