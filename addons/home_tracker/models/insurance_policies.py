from odoo import api, fields, models, _ 

class InsurancePolicies(models.Model):

    _name = 'insurance.policies'
    _description = 'Insurance Policies'

    num_police = fields.Char(string='Number Policy')
    date_in = fields.Date(string='Date In')
    date_end = fields.Date(string='Date End')
    coverage = fields.Html(string='Coverage')
    sum_assured = fields.Float(string='Sum Assured')
    yearly_fee = fields.Float(string='Yearly Fee')
    deductible = fields.Float(string='Deductible')

    property_id = fields.Many2one(comodel_name='hometracker.property', string='Property')