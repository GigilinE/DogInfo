from odoo import http, fields, _, tools
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.exceptions import AccessError, MissingError, ValidationError
import logging

_logger = logging.getLogger(__name__)


class CustomerPortalExtended(CustomerPortal):
    # Manteniamo solo l'override minimo necessario per non interferire con Odoo
    pass