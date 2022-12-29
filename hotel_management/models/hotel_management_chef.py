# -*- coding: utf-8 -*-

from odoo import models,fields

class hotelManagementChef(models.Model):
    _name = 'hotel.management.chef'
    _description = 'Hotel Management Chef Module'

    chef_name = fields.Char('Chef Name',)
    chef_mobile_number=fields.Char('Chef Mobile Number')
    chef_address=fields.Text('Chef Address')
    chef_type=fields.Selection(string = 'Chef Type',
        selection = [('head_chef','Head Chef'),('sous_chef','Sous Chef'),('line_cook','Line Cook'),('prep_cook','Prep Cook')]
        )
    chef_email=fields.Char('Chef Email')
    chef_salary=fields.Float('Chef Salary')
    chef_birth_date=fields.date('Chef Birth Date')
     