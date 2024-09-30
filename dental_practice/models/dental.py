from odoo import models, fields

class Patient(models.Model):
    _inherit = "res.partner"

    patient = fields.Boolean(string="Is Contact a Dental Patient", default=False)

class Treatment(models.Model):
    _inherit = "product.template"