# -*- coding: utf-8 -*-

from odoo import models,fields

class hotelManagementStaff(models.Model):
    _name = 'hotel.management.staff'
    _description = 'Hotel Management Staff Module'

    staff_name=fields.Char('Staff Name')
    staff_mobile_number=fields.Char('Staff Mobile Number')
    staff_address=fields.Text('Staff Address')
    staff_type=fields.Selection(string = 'Staff Type',
        selection = [('waiter','Waiter'),('bartender','Bartender'),('busser','Busser'),('cashier','Cashier'),('dishwasher','Dishwasher'),('maintenance_and_cleaning_staff','Maintenance and Cleaning Staff')]
        )
    staff_email=fields.Char('Staff Email')
    staff_salary=fields.Float('Staff Salary')
    staff_birth_date=fields.date('Staff Birth Date')


    