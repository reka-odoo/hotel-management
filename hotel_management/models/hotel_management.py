# -*- coding: utf-8 -*-

from odoo import models,fields

class hotelManagement(models.Model):
    _name = 'hotel.management'
    _description = 'Hotel Management Module'

    hotel_name = fields.Char('Hotel Name',)
    hotel_description = fields.Text('Description')
    hotel_contact_number = fields.Char('Hotel Contact No.')
    hotel_address = fields.Char('Address')
    # hotel_menu = fields.Selection(string = 'Hotel Menu',
    #     selection = [('gujarati', 'Gujarati'), ('punjabi', 'Punjabi'), ('south_indian', 'South Indian'), ('chinese', 'Chinese'), ('italian', 'Italian')]
    #     )
    hotel_menu_type_ids = fields.Many2many("hotel.menu.type",string='Menu')
    hotel_type = fields.Selection(string = 'Hotel Type',
        selection = [('dinning','Dinning'), ('banquet', 'Banquet')]
        )
    