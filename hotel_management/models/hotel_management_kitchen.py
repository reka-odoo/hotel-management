# -*- coding: utf-8 -*-

from odoo import models,fields,api

class hotelManagementKitchen(models.Model):
    _name = 'hotel.management.kitchen'
    _description = 'Hotel Management Kitchen Model'
    # _inherit = "hotel.management.orders"

    # kitchen_ids = fields.One2many("hotel.management.orders", "kitchen_id", string="Order")
    name=fields.Char()
    t_no=fields.Integer(readonly=True)
    tt_no=fields.Char()
    kitchen_ids = fields.One2many("hotel.management.food",'other_id',string="kitchen")

    # @api.depends()
    # def _compute_kitchen_orders(self):
    #     orders = self.env['hotel.management.orders']
    #         for record in self:
                


