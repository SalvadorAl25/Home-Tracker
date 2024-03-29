from odoo import api,models,fields, _

TYPES_PENALTIES = [
    ('percent', 'Percent'),
    ('fixed_payment', 'Fixed Payment'),
]

class Penalties(models.Model):

    _name = 'penalties'
    _description = 'Penalties'

    type_pay_pen = fields.Selection(selection=TYPES_PENALTIES, string='Type Payment Penalty')
    value = fields.Float(string='Value')
    mount = fields.Float(string='Mount')