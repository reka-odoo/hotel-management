# -*- coding: utf-8 -*-

from odoo import models,fields

class hotelManagement(models.Model):
    _name = 'hotel.management'
    _description = 'Hotel Management Module'

    name = fields.Char(string='Hotel Name')
    hotel_description = fields.Text(string='Description')
    hotel_contact_number = fields.Char(string='Hotel Contact No.')
    hotel_email=fields.Char(string='Hotel Email')
    hotel_address = fields.Char(string='Address')
    # hotel_timing=fields.Time(string='Hotel Timing')
    # hotel_menu = fields.Selection(string = 'Hotel Menu',
    #     selection = [('gujarati', 'Gujarati'), ('punjabi', 'Punjabi'), ('south_indian', 'South Indian'), ('chinese', 'Chinese'), ('italian', 'Italian')]
    #     )
    postcode=fields.Integer(string='Postcode')
    hotel_cuisine_ids = fields.Many2many("hotel.cuisine",string='Cuisine')
    hotel_type = fields.Selection(string = 'Hotel Type',
        selection = [('dinning','Dinning'), ('banquet', 'Banquet')]
        )
    restaurant=fields.Char(string='Restaurant Name')
    # restaurant_type=fields.Char(string='Restaurant Type', selection = [()])
    # hotel_restaurant_type=fields.Selection("Signature Restaurants", selection=[()])
    