from odoo import api,models, fields, _

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

class Propertys(models.Model):

    _name = 'property'
    _description = 'Propiedades'

    name_prop = fields.Char(string='Name Property')
    street = fields.Char(string='Street')
    num_ext = fields.Integer(string='Number External')
    num_int = fields.Integer(string='Number Internal')
    street_2 = fields.Char(string='Street 2')
    colony = fields.Char(string='Colony')
    city_id = fields.Many2one(comodel_name='res.city', string='City')
    state_id = fields.Many2one(comodel_name='res.country.state', string='State')
    country_id = fields.Many2one(comodel_name='res.country', string='Country')
    cp = fields.Char(string='Zip Code')
    maps = fields.Html(string='Google Maps')
    edifices = fields.Integer(string='Edifices')
    weight = fields.Float(string='Weight')
    height = fields.Float(string='Height')
    price_p_rent = fields.Float(string='Price per Rent')
    state = fields.Selection(selection=STATES)
    active = fields.Boolean(string='Active')
    type_property = fields.Selection(selection=TYPE_PROPERTY, string='Type Property')
    furnished = fields.Boolean(string='Furnished')
    quantity_brooms = fields.Integer(string='Quantity Bedrooms')
    quantity_bathrooms = fields.Integer(string='Quantity Bathrooms')
    quantity_parkings = fields.Integer(string='quantity Parkings')
    category_property = fields.Selection(selection=CATEGORY_PROPERTY, string='category Property')
    dir_facade = fields.Selection(selection=DIR_FACADE, string='Directory Facade')
    url_video = fields.Char(string='URL Video')
    commission= fields.Float(string='Commission')
    plans = fields.Many2many(comodel_name='ir.attachment', string='Plans', attachment=True)
    photos = fields.Many2many(comodel_name='ir.attachment', string='Photos', attachment=True)
    documents = fields.Many2many(comodel_name='ir.attachment', string='Documents', attachment=True)
    
    owner_property_id = fields.Many2one(comodel_name='res.partner', string='Owner Property')
    admin_property_id = fields.Many2one(comodel_name='res.partner', string='Admin. Property')
    currency_id = fields.Many2one(comodel_name='res.currency', string='Currency')

    property_insurance_ids = fields.One2many(comodel_name='insurance.policies', inverse_name='property_id', string='Property Insurance')
    maintenance_n_services_ids = fields.One2many(comodel_name='maintenance.n.services', inverse_name='property_id', string='Maintenance & Services')
    contracts_ids = fields.One2many(comodel_name='contracts', inverse_name='property_id', string='Contracts')
    