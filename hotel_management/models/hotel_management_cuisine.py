# -*- coding: utf-8 -*-

from odoo import models,fields

class hotelManagementCuisine(models.Model):
    _name = 'hotel.management.cuisine'
    _description = 'Hotel Management Cuisine Model'

    name=fields.Char(required=True)
    
