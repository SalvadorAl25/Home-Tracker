from odoo import api,models, fields, _
from datetime import date
import logging
_logger = logging.getLogger(__name__)

STATES = [
    ('registered', 'Registrado'),
    ('in_rent', 'En Renta'),
]

TYPE_PROPERTY = [
    ('publish', 'Publish'),
    ('private', 'Private'),
    ('social', 'Social'),
]

CATEGORY_PROPERTY = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
    ('very_high', 'Very High'),
]

DIR_FACADE = [
    ('NORTH', 'North'),
    ('EAST', 'East'),
    ('SOUTH', 'South'),
    ('WEST', 'West'),
]

class HomeTrackerProperties(models.Model):

    _name = 'hometracker.property'
    _description = 'Propiedades'

    name = fields.Char(string='Name Property', required=True, copy=False, readonly=True, index=True, default='New Property')
    street = fields.Char(string='Street')
    num_ext = fields.Integer(string='Number External')
    num_int = fields.Integer(string='Number Internal')
    street_2 = fields.Char(string='Street 2')
    colony = fields.Char(string='Colony')
    city_id = fields.Many2one(comodel_name='res.city', string='City')
    state_id = fields.Many2one(comodel_name='res.country.state', string='Country State')
    country_id = fields.Many2one(comodel_name='res.country', string='Country')
    cp = fields.Char(string='Zip Code')
    maps = fields.Html(string='Google Maps')
    edifices = fields.Integer(string='Edifices')
    weight = fields.Float(string='Weight')
    height = fields.Float(string='Height')
    price_p_rent = fields.Float(string='Price per Rent')
    states = fields.Selection(string='State', selection=STATES)
    active = fields.Boolean(string='Active')
    type_property = fields.Selection(selection=TYPE_PROPERTY, string='Type Property')
    furnished = fields.Boolean(string='Furnished')
    quantity_brooms = fields.Integer(string='Quantity Bedrooms')
    quantity_bathrooms = fields.Integer(string='Quantity Bathrooms')
    quantity_parkings = fields.Integer(string='Quantity Parkings')
    category_property = fields.Selection(selection=CATEGORY_PROPERTY, string='Category Property')
    dir_facade = fields.Selection(selection=DIR_FACADE, string='Directory Facade')
    url_video = fields.Char(string='URL Video')
    commission= fields.Float(string='Commission')
    attachments = fields.Many2many(comodel_name='ir.attachment', string='Attachments')
    
    owner_property_id = fields.Many2one(comodel_name='res.partner', string='Owner Property')
    admin_property_id = fields.Many2one(comodel_name='res.partner', string='Admin. Property')
    currency_id = fields.Many2one(comodel_name='res.currency', string='Currency')

    property_insurance_ids = fields.One2many(comodel_name='insurance.policies', inverse_name='property_id', string='Property Insurance')
    maintenance_n_services_ids = fields.One2many(comodel_name='maintenance.n.services', inverse_name='property_id', string='Maintenance & Services')
    contracts_ids = fields.One2many(comodel_name='hometracker.contracts', inverse_name='property_id', string='Contracts')


    @api.model
    def create(self, vals):
        if vals.get('name','New Property') == 'New Property':
            name_seq = self.env['ir.sequence'].next_by_code('edifice.sequence') or 'New Property'
            name = 'PROP/' + str(name_seq)
            _logger.info(f"***** name: {name}")
            vals['name'] = name 
            vals['states'] = 'registered'
        return super(HomeTrackerProperties, self).create(vals)