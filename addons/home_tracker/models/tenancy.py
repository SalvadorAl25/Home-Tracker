from odoo import api, models, fields, _

class Tenant(models.Model):
    _name = 'home.tenant'
    _description = 'Tenant'

    proof_tax_situation = fields.Binary(string='Proof Tax Situation')
    tenant_name = fields.Char(string='Name')
    tenant_last_name = fields.Char(string='Last Name')
    tenant_mother_last_name = fields.Char(string='Mother Last Name')
    rfc = fields.Char(string='RFC')
    curp = fields.Char(string='CURP')
    occupation = fields.Char(string='Occupation')
    identification = fields.Binary(string='Identification')

    tax_regimen_id = fields.Many2one(string='Tax Regimen', comodel_name='tax.regimen')
    company_id = fields.Many2one(string='Company', comodel_name='res.company')
    partner_id = fields.Many2one(string='Contact', comodel_name='res.partner')
    contracts_ids = fields.One2many(comodel_name='home.contracts', inverse_name='tenant_id', string='contracts')

