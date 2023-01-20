# -*- coding: utf-8 -*-

from odoo import models,fields

class hotelManagementKitchen(models.Model):
    _name = 'hotel.management.kitchen'
    _description = 'Hotel Management Kitchen Model'
    # _inherit = "hotel.management.orders"

    # kitchen_ids = fields.One2many("hotel.management.orders", "kitchen_id", string="Order")
    name=fields.Char()
    t_no=fields.Integer(readonly=True)
    tt_no=fields.Char()