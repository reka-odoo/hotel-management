# -*- coding: utf-8 -*-

from odoo import models,fields,api

class hotelManagementCustomer(models.Model):
    _name = 'hotel.management.orders'
    _description = 'Hotel Management Orders Module'

    name = fields.Char(string='Customer Name', required=True)
    customer_mobile_number = fields.Char(string='Mobile Number')
    customer_email=fields.Char(string='Customer Email')
    date = fields.Date(string='Date',default=lambda self: fields.Datetime.now())
    table_number = fields.Integer(string='Table Number')
    total_bill = fields.Float(string='Total Bill(₹)', readonly=True, compute="_compute_total_bill")
    order_type = fields.Selection(string='Order Type', 
        selection = [('dinning', 'Dinning'), ('take_away', 'Take Away')]
        )
   
    #for Order Info
    order_ids=fields.One2many("hotel.management", "order_id", string="Order Info")

    @api.depends()
    def _compute_total_bill(self):
        for record in self:
            record.total_bill = sum(self.order_ids.mapped('sub_total'))
