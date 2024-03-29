from odoo import api,models,fields,_

TYPE_COMMISSION = [
    ('maintenance', 'Maintenance'),
    ('services', 'Services'),
    ('transfer', 'Transfer'),

]

class Contracts(models.Model):
    _name = 'contracts'
    _description = 'Contratos'

    name_t_contract = fields.Char(string='Name Contract')
    mount_maintenance = fields.Float(string='Mount Maintenance')
    mount_rent = fields.Float(string='Rent')
    mount_deposit = fields.Float(string='Deposit')
    amount_deposit = fields.Float(string='Amount')
    contract_doc = fields.Binary(string='Contract Document')
    type_commission = fields.Selection(selection=TYPE_COMMISSION, string='Type Commission')
    mount_commission = fields.Float(string='Mount Commission')
    date_contract = fields.Date(string='Date Contract')

    property_id = fields.Many2one(comodel_name='property' ,string='Property')
    admin_id = fields.Many2one(related='property_id.admin_property_id', string='Admin Property')
    currency_id = fields.Many2one(related='property_id.currency_id', string='Currency')
    tenant_id = fields.Many2one(comodel_name='tenant', string='Tenant')
    penalty_id = fields.Many2one(comodel_name='penalty', string='Penalty')
    endorsement_person_id = fields.Many2one(comodel_name='res.partner', string='Endorsement Person')

    payments_ids= fields.One2many(comodel_name='payments.rent', inverse_name='contract_id', string='Payments')
    maintenance_n_services_ids = fields.One2many(comodel_name='maintenance.n.services', related='property.maintenance_n_services_ids', string='Maintenance & Services')
