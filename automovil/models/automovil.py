from odoo import api, fields, models


class Automovil(models.Model):
    _name = 'automovil'
    _description = 'Automovil'


    def _default_model_year(self):
        return fields.Date.add(fields.Date.today(), years=-10)

    name = fields.Char(string='Name',required=True,
                        help="Name of the Automovil")

    is_on = fields.Boolean(string='¿The engine is On?',
                        help="""Check True if Automovil Engine
                                is On or uncheck if its On
                                Check - Engine is On
                                Uncheck - Engine is Off
                                """
                                )
    velocity = fields.Float(string='Vehicle Velocity',digits='Automovil Velocity',
                                    help = """Automovil Velocity oin Km/hr""")

    doors_number = fields.Integer("Doors",default=4)

    description = fields.Text(string='Description',
                        help="""Give a Detailed description\nCharacteristics of your Automovil like:\n* Has Sun Hole\n* Has Air conditioner\n* Has Confort line Additions\n
                                """)

    model_year = fields.Date(string='Model Year',default=_default_model_year,
        help="""Give a Detailed description\n"""
         """Characteristics of your Automovil like:\n"""
         """* Has Sun Hole\n"""
         """* Has Air conditioner\n"""
         """* Has Confort line Additions\n"""
                )

    last_service_date = fields.Datetime(string="Last Service Date", default=fields.Datetime.now)

    last_verification_date = fields.Date(string="Last Verification Date", default=fields.Datetime.today())
    next_verification_date = fields.Date(string="Next Verification Date",
                                         default=fields.Date.add(fields.Date.today(), months=+6))


    cylinders = fields.Selection(string='Cylinders', selection=[('cuatro', '4 Cylinders'),
                                                                ('seis', '6 Cylinders'),
                                                                ('ocho', '8 Cylinders'),],
                                                                default='cuatro',
                                                                required=True)



    @api.onchange('last_verification_date')
    def _onchange_last_verification_date(self):
        self.next_verification_date = fields.Date.add(self.last_verification_date, months=+6)

    @api.onchange('velocity')
    def _onchange_velocity(self):
        if self.velocity <= 0:
            self.is_on = False
        else:
            self.is_on = True
