# -*- coding: utf-8 -*-

from odoo import models,fields

class hotelMenuType(models.Model):
    _name = 'hotel.menu.type'
    _description = 'Hotel Menu Type Model'

    name=fields.Char(required=True)

