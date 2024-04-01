from odoo import api,fields,models, _

class CatalogMaintenance(models.Model):

    _name = 'catalog.maintenance'
    _description = 'Catalog Maintenance'

    maint_name = fields.Char(string='Maintenance Name')
    suppliers_ids = fields.One2many(comodel_name='res.partner', string='suppliers', inverse_name='cat_maint_id')