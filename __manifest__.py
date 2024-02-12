# -*- coding: utf-8 -*-
{
    "name": "base_11",
    "summary": """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    "description": """
        Long description of module's purpose
    """,

    "author": "Francisco N. Baez C.",

    #'website': "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": 'Sale',

    "version": '1.0',

    "license": 'LGPL-3',

    # any module necessary for this one to work correctly
    "depends": [],

    # always loaded
    "data": [
        'security/ir.model.access.csv',
        'views/prperty_view.xml',
        'views/prperty_type_view.xml',
        'views/menu_items.xml',
        'static/description/icon.png'
        
    ],

    #only loaded in demonstration mode
    "demo": [
        'demo/demo.xml',
    ],
    
    "installable": True,
    "application": True,
    

    

}
