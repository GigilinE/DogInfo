from odoo import http
from odoo.http import request
import logging

_logger = logging.getLogger(__name__)


class TestPage(http.Controller):
    
    @http.route(['/my-test', '/my-test/'], type='http', auth='user', website=True)
    def my_test_page(self, **kw):
        """Pagina di test semplice"""
        _logger.info("Accesso alla pagina /my-test")
        
        # Dati da passare al template
        values = {
            'user_name': request.env.user.name,
            'current_time': 'Ora corrente: 2024-07-01',
            'test_data': [
                {'nome': 'Test 1', 'valore': 'Valore 1'},
                {'nome': 'Test 2', 'valore': 'Valore 2'},
            ]
        }
        
        return request.render('dog_registration_portal.test_page', values)
    
    @http.route(['/my-test/action'], type='http', auth='user', website=True, methods=['POST'])
    def my_test_action(self, **post):
        """Azione POST di esempio"""
        _logger.info("Ricevuti dati POST: %s", post)
        
        # Qui puoi processare i dati del form
        message = post.get('message', 'Nessun messaggio')
        
        # Redirect con messaggio di successo
        return request.redirect('/my-test?success=1&msg=' + message)