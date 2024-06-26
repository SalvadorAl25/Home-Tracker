from odoo import api, models, fields, _ 

ROLES = [
    ('tenant', 'Tenant'),
    ('resident', 'Resident'),
    ('owner', 'Owner'),
    ('admin', 'Admin'),
    ('manager', 'Manager'),
]

class ResPartner(models.Model):

    _inherit ='res.partner'

    roles = fields.Selection(selection=ROLES, string='Roles')
    cat_maint_id = fields.Many2one(comodel_name='catalog.maintenance', string='Catalog Maintenance')

class TaxRegimen(models.Model):

    _name = 'tax.regimen'
    _description = 'Tax Regimen'

    code = fields.Integer(string='Code')
    name = fields.Char(string='Name')
    