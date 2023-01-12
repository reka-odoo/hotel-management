# -*- coding: utf-8 -*-

from odoo import models,fields

class hotelManagementChef(models.Model):
    _name = 'hotel.management.chef'
    _description = 'Hotel Management Chef Module'

    name = fields.Char(string='Chef Name',)
    chef_mobile_number=fields.Char(string='Chef Mobile Number')
    chef_address=fields.Text(string='Chef Address')
    chef_joining_date=fields.Date(string='Chef Joining Date')
    chef_type=fields.Selection(string = 'Chef Type',
        selection = [('head_chef','Head Chef'),('sous_chef','Sous Chef'),('line_cook','Line Cook'),('prep_cook','Prep Cook')]
        )
    chef_email=fields.Char(string='Chef Email')
    chef_salary=fields.Float(string='Chef Salary')
    chef_birth_date=fields.Date(string='Chef Birth Date')
    chef_manager=fields.Char(string='Manager')
