from odoo import http, fields, _, tools
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.exceptions import AccessError, MissingError, ValidationError
import logging

_logger = logging.getLogger(__name__)


class CustomerPortalExtended(CustomerPortal):
    
    def _get_mandatory_fields(self):
        """Override to include dog fields as valid fields"""
        mandatory_fields = super()._get_mandatory_fields()
        return mandatory_fields
    
    def details_form_validate(self, data):
        """Override to handle dog fields validation"""
        error, error_message = super().details_form_validate(data)
        
        # Remove dog fields from validation errors since they're custom
        dog_fields = ['x_studio_dog_name', 'x_studio_dog_breed', 'x_studio_dog_age', 'x_studio_dog_weight']
        
        # Filter out dog field errors from the standard validation
        if error:
            for field in dog_fields:
                if field in error:
                    del error[field]
        
        return error, error_message
    
    @http.route(['/my/account'], type='http', auth='user', website=True)
    def account(self, redirect=None, **post):
        """Override account method to handle dog information fields"""
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        
        values.update({
            'partner': partner,
            'error': {},
            'error_message': [],
        })
        
        if post and request.httprequest.method == 'POST':
            # Handle form submission with dog fields
            error, error_message = self.details_form_validate(post)
            values.update({'error': error, 'error_message': error_message})
            
            if not error:
                # Get all partner fields that are writable
                partner_fields = request.env['res.partner']._fields.keys()
                values_to_update = {}
                
                # Add standard portal fields
                for field_name in self._get_mandatory_fields():
                    if field_name in post:
                        values_to_update[field_name] = post[field_name]
                
                # Add all other standard fields that exist in post
                standard_fields = ['company_name', 'vat', 'phone', 'street', 'street2', 'city', 'zipcode', 'state_id', 'country_id']
                for field in standard_fields:
                    if field in post and field in partner_fields:
                        if field in ['state_id', 'country_id']:
                            values_to_update[field] = int(post[field]) if post[field] else False
                        else:
                            values_to_update[field] = post[field] or False
                
                # Add dog fields
                dog_fields = [
                    'x_studio_dog_name',
                    'x_studio_dog_breed', 
                    'x_studio_dog_age',
                    'x_studio_dog_weight'
                ]
                
                for field in dog_fields:
                    if field in post and field in partner_fields:
                        if field == 'x_studio_dog_age':
                            # Convert to integer
                            try:
                                values_to_update[field] = int(post[field]) if post[field] else False
                            except ValueError:
                                values_to_update[field] = False
                        elif field == 'x_studio_dog_weight':
                            # Convert to float
                            try:
                                values_to_update[field] = float(post[field]) if post[field] else False
                            except ValueError:
                                values_to_update[field] = False
                        else:
                            # String fields
                            values_to_update[field] = post[field] or False
                
                # Update the partner
                try:
                    partner.sudo().write(values_to_update)
                    _logger.info(f"Updated partner {partner.id} with fields: {list(values_to_update.keys())}")
                except Exception as e:
                    _logger.error(f"Error updating partner: {e}")
                    error_message.append(_("Error updating your information. Please try again."))
                    values.update({'error_message': error_message})
                
                if redirect and not error_message:
                    return request.redirect(redirect)
                elif not error_message:
                    return request.redirect('/my/account')
        
        # Get countries and states for form
        countries = request.env['res.country'].sudo().search([])
        states = request.env['res.country.state'].sudo().search([])
        
        values.update({
            'countries': countries,
            'states': states,
            'has_check_vat': hasattr(request.env['res.partner'], 'check_vat'),
            'partner_can_edit_vat': partner.can_edit_vat() if hasattr(partner, 'can_edit_vat') else True,
            'redirect': redirect,
            'page_name': 'my_details',
        })
        
        response = request.render("portal.portal_my_details", values)
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['Content-Security-Policy'] = "frame-ancestors 'self'"
        return response