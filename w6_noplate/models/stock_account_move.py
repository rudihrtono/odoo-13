from odoo import api, fields, models, _

class Picking(models.Model):
        _inherit = 'account.move.line'

        noplate = fields.Char(string="No Plate")