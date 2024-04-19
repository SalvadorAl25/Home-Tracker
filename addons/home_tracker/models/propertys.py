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

class HomeProperties(models.Model):

    _name = 'home.property'
    _description = 'Gestor de Propiedades'

    name = fields.Char(string='Name Property', required=True, copy=False, readonly=True, index=True, default='New Property')
    img_of_prop = fields.Binary(string='Image Property')
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
    active_prop = fields.Boolean(string='Active')
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
    contracts_ids = fields.One2many(comodel_name='home.contracts', inverse_name='property_id', string='Contracts')


    @api.model
    def create(self, vals):
        if vals.get('name','New Property') == 'New Property':
            name_seq = self.env['ir.sequence'].next_by_code('edifice.sequence') or 'New Property'
            country_id = vals.get('country_id')
            state_id = vals.get('state_id')
            city_id = vals.get('city_id')
            n = self._name_create_seq(country_id, state_id, city_id)
            name = n + '/' + str(name_seq)
            vals['name'] = name 
            vals['states'] = 'registered'
        return super(HomeProperties, self).create(vals)
    
    def _name_create_seq(self,country_id, state_id, city_id):
        country_code = self.env['res.country'].search([('id','=',country_id)])
        state_code = self.env['res.country.state'].search([('id','=',state_id)])
        city_code = self.env['res.city'].search([('id','=',city_id)]) 
        format_name = str(country_code.code) + '/'+ str(state_code.code) +'/' + str(city_code.name[:3]).upper()

        return format_name
    
    def new_contrat(self):
        return {
            'name': 'New Contrat',
            'type': 'ir.actions.act_window',
            'res_model': 'home.contracts',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'current'
        }