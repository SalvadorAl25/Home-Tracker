from odoo import api,models,fields,_
from datetime import date, timedelta
import logging
_logger = logging.getLogger(__name__)

TYPE_COMMISSION = [
    ('maintenance', 'Maintenance'),
    ('services', 'Services'),
    ('transfer', 'Transfer'),

]

STATES = [
    ('registered', 'Registered'),
    ('active', 'Active'),
    ('cancelled', 'Cancelled'),
    ('expired', 'Expired'),
    ('in_dispute', 'In Dispute'),
    ('renewal', 'Renewal'),
    ('pending','Pending'),
]

class Contracts(models.Model):
    _name = 'home.contracts'
    _description = 'Contratos'

    name = fields.Char(string='Name Contract', required=True, copy=False, readonly=True, index=True, default='New Contract')
    mount_maintenance = fields.Float(string='Mount Maintenance')
    mount_rent = fields.Float(string='Rent')
    mount_deposit = fields.Float(string='Deposit')
    amount_deposit = fields.Float(string='Amount')
    contract_doc = fields.Binary(string='Contract Document')
    type_commission = fields.Selection(selection=TYPE_COMMISSION, string='Type Commission')
    mount_commission = fields.Float(string='Mount Commission')
    date_contract = fields.Date(string='Date Contract')
    states = fields.Selection(selection=STATES, string='State')

    property_id = fields.Many2one(comodel_name='home.property' ,string='Property')
    admin_id = fields.Many2one(related='property_id.admin_property_id', string='Admin Property')
    currency_id = fields.Many2one(related='property_id.currency_id', string='Currency')
    tenant_id = fields.Many2one(comodel_name='home.tenant', string='Tenant')
    penalty_id = fields.Many2one(comodel_name='home.penalties', string='Penalty')
    endorsement_person_id = fields.Many2one(comodel_name='res.partner', string='Endorsement Person')

    payments_ids= fields.One2many(comodel_name='payments.rent', inverse_name='contract_id', string='Payments')
    maintenance_n_services_ids = fields.One2many(comodel_name='maintenance.n.services', related='property_id.maintenance_n_services_ids', string='Maintenance & Services')

    @api.model
    def create(self, vals):
        year_today = date.today().year
        if vals.get('name','New Contract') == 'New Contract':
            name_seq = self.env['ir.sequence'].next_by_code('contract.sequence') or 'New Contract'
            property_id = vals.get('property_id')
            contr, stat, city_f, type_pro = self._get_location_property(property_id)
            city = city_f.upper()
            prop_type = type_pro[:3].upper()
            name = contr+'-'+stat+'-'+city+'-'+prop_type+'-'+name_seq+'-'+str(year_today)
            vals['name'] = name 
            vals['states'] = 'registered'
        return super(Contracts, self).create(vals)
    
    def _get_location_property(self,id_property):
        property_id = self.env['home.property'].search([('id','=',id_property)])
        country = property_id.country_id
        state = property_id.state_id
        city = property_id.city_id
        type_prop = property_id.type_property

        return country.code, state.code, city.name[:3], type_prop

