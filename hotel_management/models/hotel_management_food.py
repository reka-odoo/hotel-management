# -*- coding: utf-8 -*-

from odoo import models,fields,api

class hotelManagementFood(models.Model):
    _name = 'hotel.management.food'
    _description = 'Hotel Management Food Model'
    _rec_name = 'food_items'

    #for Order Info 
    order_id = fields.Many2one("hotel.management.orders")
    food_items = fields.Char(string='Food Items')
    food_price = fields.Float(string='Food Price(₹)')
    food_quantity = fields.Integer(string='Quantity', required=True, default=1)
    sub_total = fields.Float(string='Subtotal(₹)', compute="_compute_sub_total")
    # other_id = fields.Many2one("hotel.management.food",string = "other")
    
    #Add Food Items in cuisine and we can see that field in orders also.
    food_price_table = fields.Float(string='Food Price (₹)', related = "food_item_id.food_price")
    food_item_id = fields.Many2one("hotel.management.food")

    #for Food Info
    food_id = fields.Many2one("hotel.management.cuisine")

    @api.depends("food_price_table", "food_quantity")
    def _compute_sub_total(self):
        for record in self:
            record.sub_total = record.food_price_table * record.food_quantity
