from odoo import api, fields, models, _

class Picking(models.Model):
    _inherit='stock.picking'
    #noplate = fields.Many2one('account.analytic.account','noplate')
    noplate = fields.Char(string="No Plate")