# -*- coding: utf-8 -*-

from odoo import models,fields,api,Command
from odoo.exceptions import UserError

class hotelManagementCustomer(models.Model):
    _name = 'hotel.management.orders'
    _description = 'Hotel Management Orders Model'

    #for Order Info
    order_ids = fields.One2many("hotel.management.food", "order_id", string = "Food")
    name = fields.Char(string='Customer Name')
    customer_mobile_number = fields.Char(string='Mobile Number')
    customer_email = fields.Char(string='Customer Email')
    date = fields.Date(string='Date',default=lambda self: fields.Datetime.now())
    table_number = fields.Integer(string='Table Number')
    total_bill = fields.Float(string='Total Bill(₹)', readonly=True, compute="_compute_total_bill")
    order_type = fields.Selection(string='Order Type', 
        selection = [('dinning', 'Dinning'), ('take_away', 'Take Away')]
        )

    state = fields.Selection(selection=[('new', 'New'),
                                        ('in_progress','In Progress'),
                                        ('completed', 'Completed'),
                                        ('canceled', 'Canceled')],
                                        default='new')
        
    

    #for kitchen Info
    # kitchen_id = fields.Many2one("hotel.management.kitchen")

    @api.depends("order_ids")
    def _compute_total_bill(self):
        for record in self:
            record.total_bill = sum(self.order_ids.mapped('sub_total'))

    def send_kitchen(self):
        for record in self:
            if record.state == 'canceled':
                raise UserError("Order is Canceled.")
            else:
                record.state = 'in_progress'
            self.env['hotel.management.kitchen'].create(
                {
                    "name":record.name,
                    # "table_no":record.table_number
                    "kitchen_ids": [
                        Command.create(
                            {
                                "kitchen_food_items": record.order_ids.food_item_id.food_items,
                                # "quantity": record.order_ids.food_item_id.food_quantity,
                                # "price_unit": record.order_ids.food_item_id.food_price
                            }
                        ),
                    ],
                }
            )
            # return super().send_kitchen()
    