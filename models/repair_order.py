# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class Repair(models.Model):
    _inherit = ['repair.order']
    
    phone_id = fields.Char(related='partner_id.phone')
    mobile_id = fields.Char(related='partner_id.mobile')
    street_id = fields.Char(related='partner_id.street')
    street2_id = fields.Char(related='partner_id.street2')
    city_id = fields.Char(related='partner_id.city')