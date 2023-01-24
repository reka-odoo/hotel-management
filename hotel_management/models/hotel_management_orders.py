# -*- coding: utf-8 -*-

from odoo import models,fields,api,Command
from odoo.exceptions import UserError

class hotelManagementCustomer(models.Model):
    _name = 'hotel.management.orders'
    _description = 'Hotel Management Orders Model'

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
        
    #for Order Info
    order_ids = fields.One2many("hotel.management.food", "order_id", string = "Food Items")

    #for kitchen Info
    kitchen_id = fields.Many2one("hotel.management.kitchen",string="kitchen")

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

#         for rec in self:
#             # ls = []
#             # ls.append(rec.order_ids.food_item_id.food_items)
#             self.env['hotel.management.kitchen'].create({
#                 'name':rec.name,
#                 't_no' : rec.table_number,
#                 'kitchen_ids': [
#                     Command.create({
#                         'food_item_id' : rec.order_ids.food_item_id,
#                         'food_price_table':rec.order_ids.food_price_table,                    
#                         'food_quantity' :rec.order_ids.food_quantity ,
#                         'sub_total' : rec.order_ids.sub_total,
#                         'food_price' : rec.order_ids.food_price,
#                 })
# ]

#                 # "food_data":[
#                 #     (
#                 #         {
#                 #             'tt_no': ls
#                 #         }
#                 #     ),
#                 # ],
            
#             })
        # return super().send_kitchen()
