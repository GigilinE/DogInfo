from odoo import http, _
from odoo.http import request
from odoo.exceptions import UserError
from odoo.addons.auth_signup.controllers.main import AuthSignupHome


class AuthSignupHomeExtended(AuthSignupHome):

    @http.route('/web/signup', type='http', auth='public', website=True, sitemap=False)
    def web_auth_signup(self, *args, **kw):
        qcontext = self.get_auth_signup_qcontext()
        
        if request.httprequest.method == 'POST':
            # Add dog fields to qcontext
            dog_fields = ['dog_name', 'dog_breed', 'dog_age', 'dog_weight']
            for field in dog_fields:
                if kw.get(field):
                    if field == 'dog_age':
                        try:
                            qcontext[field] = int(kw.get(field)) if kw.get(field) else None
                        except (ValueError, TypeError):
                            qcontext[field] = None
                    elif field == 'dog_weight':
                        try:
                            qcontext[field] = float(kw.get(field)) if kw.get(field) else None
                        except (ValueError, TypeError):
                            qcontext[field] = None
                    else:
                        qcontext[field] = kw.get(field)
        
        return super(AuthSignupHomeExtended, self).web_auth_signup(*args, **kw)

    def do_signup(self, qcontext):
        values = {key: qcontext.get(key) for key in ('login', 'name', 'password')}
        
        # Add dog fields to values
        dog_fields = ['dog_name', 'dog_breed', 'dog_age', 'dog_weight']
        for field in dog_fields:
            if qcontext.get(field):
                values[field] = qcontext.get(field)
        
        if not values:
            raise UserError(_("The form was not properly filled in."))
        if values.get('password') != qcontext.get('confirm_password'):
            raise UserError(_("Passwords do not match; please retype them."))
        
        supported_lang_codes = [code for code, _ in request.env['res.lang'].get_installed()]
        lang = request.context.get('lang', '')
        if lang in supported_lang_codes:
            values['lang'] = lang
        
        self._signup_with_values(qcontext.get('token'), values)
        request.env.cr.commit()