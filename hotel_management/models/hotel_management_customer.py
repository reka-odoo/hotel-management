# -*- coding: utf-8 -*-

from odoo import models,fields

class hotelManagementCustomer(models.Model):
    _name = 'hotel.management.customer'
    _description = 'Hotel Management Customer Module'

    customer_name = fields.Char('Customer Name', )
    customer_mobile_number = fields.Char('Customer Mobile Number', )
    date = fields.Date('Date',default=lambda self: fields.Datetime.now())
    table_number = fields.Integer('Table Number')
    bill = fields.Float('Bill', required=True)
    # menu = fields.Selection(string='Menu',
    #     selection=[('gujarati', 'Gujarati'), ('punjabi', 'Punjabi'), ('south_indian', 'South Indian'), ('chinese', 'Chinese')]
    #     )
