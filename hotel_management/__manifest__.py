# -*- coding: utf-8 -*-
{
    'name': 'Hotel Management',
    'description': 'Hotel Management Module',
    'author': 'Renilkumar kajavadra',
    'data': [
                'security/ir.model.access.csv',
                'views/hotel_management_views.xml',
                'views/hotel_management_menus.xml',
                'views/hotel_management_orders.xml',
                'views/hotel_management_staff.xml',
                'views/hotel_management_chef.xml',
                'views/hotel_management_cuisine.xml'
                ],
    'demo': [
                'demo/demo.xml',
                'demo/hotel_cuisine.xml'
                ],
    'application': True,
    'installable': True,
    'license': 'LGPL-3'
}
