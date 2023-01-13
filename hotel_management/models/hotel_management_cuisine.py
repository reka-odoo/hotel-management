# -*- coding: utf-8 -*-

from odoo import models,fields,api

class hotelManagementCuisine(models.Model):
    _name = 'hotel.management.cuisine'
    _description = 'Hotel Management Cuisine Model'

    name=fields.Char(string='Cuisine')

    #for Order Info 
    order_id = fields.Many2one("hotel.management.orders")
    food_items=fields.Char(string='Food Items')
    food_price=fields.Float(string='Food Price(₹)')
    food_quantity=fields.Integer(string='Quantity')
    sub_total=fields.Float(string='Subtotal(₹)', compute="_compute_sub_total")


    #for Food Info
    # food_ids = fields.One2many("hotel.management" , "food_id", string="Food Info")
    
    @api.depends("food_price", "food_quantity")
    def _compute_sub_total(self):
        for record in self:
            record.sub_total = record.food_price * record.food_quantity