# -*- coding: utf-8 -*-

from odoo import models,fields,api

class hotelManagement(models.Model):
    _name = 'hotel.management'
    _description = 'Hotel Management Module'

    name = fields.Char(string='Hotel Name')
    hotel_description = fields.Text(string='Description')
    hotel_contact_number = fields.Char(string='Hotel Contact No.')
    hotel_email=fields.Char(string='Hotel Email')
    hotel_address = fields.Char(string='Address')
    postcode=fields.Integer(string='Postcode')
    hotel_type = fields.Selection(string = 'Hotel Type',
        selection = [('dinning','Dinning'), ('banquet', 'Banquet')]
        )
    restaurant=fields.Char(string='Restaurant Name')

    #for Tag
    hotel_cuisine_ids = fields.Many2many("hotel.management.cuisine",string='Cuisine')

    # #for Order Info 
    # order_id = fields.Many2one("hotel.management.orders")
    # food_items=fields.Many2one("hotel.management.cuisine", string='Food Items')
    # food_price=fields.Float(string='Food Price(₹)')
    # food_quantity=fields.Integer(string='Quantity')
    # sub_total=fields.Float(string='Subtotal(₹)', compute="_compute_sub_total")

    #for Food Info
    food_id = fields.Many2one("hotel.management.cuisine")
    
    # @api.depends("food_price", "food_quantity")
    # def _compute_sub_total(self):
    #     for record in self:
    #         record.sub_total = record.food_price * record.food_quantity
