# -*- coding: utf-8 -*-

from odoo import fields, models,Command

class hotelManagementAccount(models.Model):
    _inherit = "hotel.management.orders"

    def send_kitchen(self):
       for record in self:
            self.env['account.move'].create(
                {
                    # "partner_id": record.name,
                    "move_type": 'out_invoice',
                    "invoice_line_ids": [
                        Command.create(
                            {
                                "name": record.order_ids.food_item_id.food_items,
                                "quantity": record.order_ids.food_item_id.food_quantity,
                                "price_unit": record.order_ids.food_item_id.food_price
                            }
                        ),
                    ],
                }
            )
            return super().send_kitchen()
