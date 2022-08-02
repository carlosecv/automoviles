from odoo import api, fields, models


class Automovil(models.Model):
    _name = 'automovil'
    _description = 'Automovil'

    name = fields.Char(string='Name')

    is_on = fields.Boolean(string='¿The engine is On?')
    velocity = fields.Float(string='Vehicle Velocity',digits='Automovil Velocity')
    doors_number = fields.Integer("Doors")
    description = fields.Text(string='Description')

