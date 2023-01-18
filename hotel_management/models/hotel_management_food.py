# -*- coding: utf-8 -*-

from odoo import models,fields,api

class hotelManagementFood(models.Model):
    _name = 'hotel.management.food'
    _description = 'Hotel Management Food Module'

    #for Order Info 
    order_id = fields.Many2one("hotel.management.orders")
    food_items=fields.Char(string='Food Items')
    food_price=fields.Float(string='Food Price(₹)')
    food_quantity=fields.Integer(string='Quantity')
    sub_total=fields.Float(string='Subtotal(₹)', compute="_compute_sub_total")

    #for Food Info
    food_id = fields.Many2one("hotel.management.cuisine")

    @api.depends("food_price", "food_quantity")
    def _compute_sub_total(self):
        for record in self:
            record.sub_total = record.food_price * record.food_quantity
