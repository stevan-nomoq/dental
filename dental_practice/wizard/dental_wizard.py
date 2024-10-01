from odoo import models, fields

class Dialog(models.TransientModel):
    _name = "dental.dialog"

    diag_id = fields.Many2many("dental.diags", string='Diagnostics')
    treat_id = fields.Many2one("product.template", string="Treatments")





