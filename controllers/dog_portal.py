from odoo import http, _
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class DogPortal(http.Controller):
    
    @http.route(['/my-dog', '/my-dog/'], type='http', auth='user', website=True)
    def my_dog(self, **kw):
        """Display dog information page"""
        partner = request.env.user.partner_id
        
        values = {
            'partner': partner,
            'page_name': 'dog_info',
            'error': {},
            'error_message': []
        }
        
        return request.render('dog_registration_portal.portal_my_dog', values)
    
    @http.route(['/my-dog/edit'], type='http', auth='user', website=True)
    def my_dog_edit(self, **kw):
        """Display dog information edit form"""
        partner = request.env.user.partner_id
        
        values = {
            'partner': partner,
            'page_name': 'dog_info_edit',
            'error': {},
            'error_message': []
        }
        
        return request.render('dog_registration_portal.portal_my_dog_edit', values)
    
    @http.route(['/my-dog/save'], type='http', auth='user', website=True, methods=['POST'], csrf=True)
    def my_dog_save(self, **post):
        """Save dog information"""
        partner = request.env.user.partner_id
        
        # Log the received data
        _logger.info("Dog save - Received data: %s", post)
        
        # Prepare values for update
        dog_values = {}
        
        # Process dog name
        if 'x_studio_dog_name' in post:
            dog_values['x_studio_dog_name'] = post.get('x_studio_dog_name', '').strip()
        
        # Process dog breed
        if 'x_studio_dog_breed' in post:
            dog_values['x_studio_dog_breed'] = post.get('x_studio_dog_breed', '')
        
        # Process dog age
        if 'x_studio_dog_age' in post:
            try:
                age = post.get('x_studio_dog_age', '').strip()
                if age:
                    dog_values['x_studio_dog_age'] = int(age)
                else:
                    dog_values['x_studio_dog_age'] = False
            except (ValueError, TypeError):
                _logger.warning("Invalid age value: %s", post.get('x_studio_dog_age'))
                dog_values['x_studio_dog_age'] = False
        
        # Process dog weight
        if 'x_studio_dog_weight' in post:
            try:
                weight = post.get('x_studio_dog_weight', '').strip()
                if weight:
                    dog_values['x_studio_dog_weight'] = float(weight)
                else:
                    dog_values['x_studio_dog_weight'] = False
            except (ValueError, TypeError):
                _logger.warning("Invalid weight value: %s", post.get('x_studio_dog_weight'))
                dog_values['x_studio_dog_weight'] = False
        
        # Update partner with dog information
        if dog_values:
            try:
                partner.sudo().write(dog_values)
                _logger.info("Successfully updated dog information for partner %s", partner.id)
                return request.redirect('/my-dog?success=1')
            except Exception as e:
                _logger.error("Error updating dog information: %s", str(e))
                return request.redirect('/my-dog/edit?error=1')
        
        return request.redirect('/my-dog')