# -*- coding: utf-8 -*-

from odoo import models, fields, Command, api


class hotelManagementKitchen(models.Model):
    _name = 'hotel.management.kitchen'
    _description = 'Hotel Management Kitchen Model'
    _inherit = "hotel.management.orders"
    # _inherit = "hotel.management.orders"

    # kitchen_ids = fields.One2many("hotel.management.orders", "kitchen_id", string="Order")
    name = fields.Char()
    table_no = fields.Integer()
    # kitchen_order_type = fields.Selection(string = 'Order Type')
    kitchen_food_items = fields.Char()
    kitchen_food_price = fields.Float()
    kitchen_food_quantity = fields.Integer()

    kitchen_id = fields.Many2one("hotel.management.orders")
    kitchen_ids = fields.Many2many(
        "hotel.management.orders", string="Kitchen", compute="_compute_kitchen_ids")

    @api.depends("kitchen_id","order_ids")
    def _compute_kitchen_ids(self):
        for order in self:
            order.kitchen_ids = order.kitchen_id.order_ids

    @api.model
    def create(self, values):
        rebate_id = self.env['hotel.management.orders'].browse(values['order_ids.'])
        section_list = rebate_id.mapped('rebate_ids.rebate_section_name')
        if values['rebate_section_name'] in section_list:
            raise ve("message")
        return super().create(values)

    # @api.depends()
    # def _compute_kitchen_orders(self):
    #     orders = self.env['hotel.management.orders']
    #         for record in self:

    # def send_kitchen(self):
    #     for record in self:
    #             self.env['hotel.management.kitchen'].create(
    #                 {
    #                     "name": record.name,
    #                     # "table_no": record.table_number,
    #                     # "kitchen_order_type": record.order_type,
    #                     "kitchen_food_items": record.order_ids.food_item_id.food_items
                        
    #                     # "kitchen_ids": [
    #                     #     Command.create(
    #                     #         {
    #                     #             "kitchen_food_items": record.order_ids.food_item_id.food_items,
    #                     #             "kitchen_food_quantity": record.order_ids.food_item_id.food_quantity,
    #                     #             "kitchen_food_price": record.order_ids.food_item_id.food_price,
    #                     #         }
    #                     #     ),
    #                     # ],
    #                 }
    #             )  
    #             return super().send_kitchen() 