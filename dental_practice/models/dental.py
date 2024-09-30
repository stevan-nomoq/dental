from odoo import models, fields, api

class Patient(models.Model):
    _inherit = "res.partner"

    patient = fields.Boolean(string="Is Contact a Dental Patient", default=False)
    tooth_id = fields.Many2one('dental.teeth', string="Tooth")
    diag_id = fields.Many2many("dental.diags", string='Diagnostics')
    treat_id = fields.Many2one("product.template", string="Treatments")

    def write(self, vals):
        res = super(Patient, self).write(vals)
        if 'treat_id' in vals:
            # if there is an open bill add a new line, if not, open a new SO
            existing_so = self.env['sale.order'].search([('partner_id', '=', self.id),('state', 'in', ['draft', 'sent'])])
            if existing_so:
                # if we need to add one or multiple sale order lines in the DB
                self.env["sale.order.line"].create(
                    {
                        "order_id": existing_so.id,
                        "product_id": vals["treat_id"],  # some product.product ID,
                    }
                )
            else:
                sale_order = self.env['sale.order'].create({
                    'partner_id': self.id,
                    'order_line': [(0, 0, {
                        'product_id': vals['treat_id'],
                    })],
                })
        return res
class Diags(models.Model):
    _name = "dental.diags"

    name = fields.Char(string="Diagnostic")

class Teeth(models.Model):
    _name = "dental.teeth"

    name = fields.Char(string="Tooth")