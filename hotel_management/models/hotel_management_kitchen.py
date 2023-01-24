# -*- coding: utf-8 -*-

from odoo import models,fields,Command

class hotelManagementKitchen(models.Model):
    _name = 'hotel.management.kitchen'
    _description = 'Hotel Management Kitchen Model'
    # _inherit = "hotel.management.orders", "hotel.management.food"
    # _inherit = "hotel.management.orders"

    # kitchen_ids = fields.One2many("hotel.management.orders", "kitchen_id", string="Order")
    # name=fields.Char()
    # table_no = fields.Integer(string = 'Table Number', readonly=True)
    # kitchen_order_type = fields.Selection(string = 'Order Type')
    # kitchen_ids = fields.One2many("hotel.management.food",'other_id',string="kitchen")

    # @api.depends()
    # def _compute_kitchen_orders(self):
    #     orders = self.env['hotel.management.orders']
    #         for record in self:
   
    # def send_kitchen(self):
    #    for record in self:
    #         self.env['hotel.management.kitchen'].create(
    #             {
    #                 "name": record.name,
    #                 "table_no": record.table_number,
    #                 "kitchen_order_type": record.order_type,
                    
    #                 "invoice_line_ids": [
    #                     Command.create(
    #                         {
    #                             "name": record.name,
    #                             "quantity": 1.0,
    #                             "price_unit": record.selling_price * 6.0 / 100,
    #                         }
    #                     ),
    #                 ],
    #             }
    #         )  
    #         return super().sold_button()          