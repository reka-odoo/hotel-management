# -*- coding: utf-8 -*-

from odoo import models,fields

class hotelManagementCustomer(models.Model):
    _name = 'hotel.management.customer'
    _description = 'Hotel Management Customer Module'

    name = fields.Char(string='Customer Name', )
    customer_mobile_number = fields.Char(string='Customer Mobile Number', )
    date = fields.Date(string='Date',default=lambda self: fields.Datetime.now())
    table_number = fields.Integer(string='Table Number')
    bill = fields.Float(string='Bill', required=True)
    # menu = fields.Selection(string='Menu',
    #     selection=[('gujarati', 'Gujarati'), ('punjabi', 'Punjabi'), ('south_indian', 'South Indian'), ('chinese', 'Chinese')]
    #     )
