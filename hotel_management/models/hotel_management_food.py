# -*- coding: utf-8 -*-

from odoo import models,fields

class hotelManagementFood(models.Model):
    _name = 'hotel.management.food'
    _description = 'Hotel Management Food Model'

    name=fields.Char(required=True)
    food_ids=fields.One2many("hotel.management", "food_id", string="Order Info")


