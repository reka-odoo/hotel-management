# -*- coding: utf-8 -*-

from odoo import models,fields

class hotelManagementStaff(models.Model):
    _name = 'hotel.management.staff'
    _description = 'Hotel Management Staff Model'

    name = fields.Char(string='Staff Name')
    staff_mobile_number = fields.Char(string='Staff Mobile Number')
    staff_address = fields.Text(string='Staff Address')
    staff_joining_date = fields.Date(string='Staff Joining Date')
    staff_type = fields.Selection(string = 'Staff Type',
        selection = [('waiter','Waiter'),
                     ('bartender','Bartender'),
                     ('busser','Busser'),
                     ('cashier','Cashier'),
                     ('dishwasher','Dishwasher'),
                     ('maintenance_and_cleaning_staff','Maintenance and Cleaning Staff')]
        )
    staff_email = fields.Char(string='Staff Email')
    staff_salary = fields.Float(string='Staff Salary')
    staff_birth_date = fields.Date(string='Staff Birth Date')
    staff_manager = fields.Char(string='Manager')
