# -*- coding: utf-8 -*-

from odoo import models,fields,api

class hotelManagementCuisine(models.Model):
    _name = 'hotel.management.cuisine'
    _description = 'Hotel Management Cuisine Model'

    name = fields.Char(string='Cuisine')
    food_description = fields.Text(string='Description')

    #for Food Info
    food_ids = fields.One2many("hotel.management.food", "food_id", string = "Food Info")
    