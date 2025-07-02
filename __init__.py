# -*- coding: utf-8 -*-
from . import controllers
from . import models
from odoo import api, SUPERUSER_ID


def _post_init_hook(cr, registry):
    """Converte i campi Studio base in manual per migliore integrazione"""
    env = api.Environment(cr, SUPERUSER_ID, {})
    
    # Trova campi Studio che dovrebbero essere manual
    studio_fields = env['ir.model.fields'].search([
        ('name', 'like', 'x_studio_%'),
        ('model', 'in', ['res.partner', 'res.users']),
        ('state', '=', 'base')
    ])
    
    # Converti in stato manual
    if studio_fields:
        studio_fields.write({'state': 'manual'})