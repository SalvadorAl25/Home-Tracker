from odoo import api, models, fields, _

REASONS = [
    ('Rent', 'Rent'),
    ('Deposit', 'Deposit'),
    ('Maintenance', 'Maintenance'),
    ('Other', 'Other'),
]

class PaymentsRent(models.Model):

    _name = 'payments.rent'
    _description = 'Payments Rent'

    payment_reason = fields.Selection(selection=REASONS, string='payment reason')
    date_payment = fields.Float(string='Date Payment')
    amount = fields.Float(string='Amount')
    invoice_id = fields.Many2one(comodel_name='account.move', string='Invoice')
    contract_id = fields.Many2one(comodel_name='contracts', string='contract')