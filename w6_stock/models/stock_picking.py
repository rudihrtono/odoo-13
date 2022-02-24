from odoo import api, fields, models, _

class Picking(models.Model):
    _inherit='stock.picking'
    analytic_account_id=fields.Many2one('account.analytic.account','Project')