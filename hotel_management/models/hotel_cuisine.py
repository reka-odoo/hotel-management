# -*- coding: utf-8 -*-

from odoo import models,fields

class hotelCuisine(models.Model):
    _name = 'hotel.cuisine'
    _description = 'Hotel Cuisine Model'

    name=fields.Char(required=True)

