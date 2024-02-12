# -*- coding: utf-8 -*-

from odoo import models, fields

class Property(models.models):
    _name = 'estate.property'

# campos menu 1
    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    data_availability = fields.Date(string="Available from")
    expected_price = fields.Float(string="Expected Price")
    best_offer = fields.Float(string="Best Offer")
    selling_price = fields.Float(string="selling price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area(sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage", default=False)
    garden = fields.Boolean(string="Garden", default=False)
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string="Garden Orientation", default='north')
    
#campos menu 2
class PropertyType(models.models):
    _name = 'estate.property.type'

    name = fields.char(string="name", required=True)
