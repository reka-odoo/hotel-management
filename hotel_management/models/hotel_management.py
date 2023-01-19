# -*- coding: utf-8 -*-

from odoo import models,fields,api

class hotelManagement(models.Model):
    _name = 'hotel.management'
    _description = 'Hotel Management Model'

    name = fields.Char(string='Hotel Name')
    hotel_description = fields.Text(string='Description')
    hotel_contact_number = fields.Char(string='Hotel Contact No.')
    hotel_email = fields.Char(string='Hotel Email')
    hotel_address = fields.Char(string='Address')
    postcode = fields.Integer(string='Postcode')
    hotel_type = fields.Selection(string = 'Hotel Type',
        selection = [('dinning','Dinning'), ('banquet', 'Banquet')]
        )
    restaurant = fields.Char(string='Restaurant Name')
    
    #for Tag
    hotel_cuisine_ids = fields.Many2many("hotel.management.cuisine", string='Cuisine')

    #for Food Info
    food_id = fields.Many2one("hotel.management.cuisine")
