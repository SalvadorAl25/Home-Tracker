from odoo import api,fields,models, _

STATES = [
    ('draft', 'Draft'),
    ('confirm', 'Confirm'),
    ('done', 'Done'),
    ]

FREQUENCIES = [
    ('diary', 'Diary'),
    ('monthly', 'Monthly'),
    ('quarterly', 'Quarterly'),
    ('semiannual', 'Semiannual'),
    ('annual', 'Annual'),
    ('biannual', 'Biannual'),
]

class MaintenanceNServices(models.Model):

    _name ='maintenance.n.services'
    _description = 'Maintenance and Services'

    man_serv_name = fields.Char(string='Name Maintenance')
    charge_applies = fields.Boolean(string='Charge applies')
    date_program = fields.Date(string='Date Program')
    description = fields.Text(string='Description')
    complete = fields.Boolean(string='Complete')
    cost = fields.Float(string='Cost')
    frequency = fields.Selection(selection=FREQUENCIES, string='Frequency')
    note = fields.Text(string='Note')
    state = fields.Selection(selection=STATES, string='State')

    supplier_id = fields.Many2one(comodel_name='res.partner', string='Supplier')
    property_id = fields.Many2one(comodel_name='hometracker.property', string='Property')
    type_maintenance_id = fields.Many2one(comodel_name='catalog.maintenance', string='Type Maintenance')
    
