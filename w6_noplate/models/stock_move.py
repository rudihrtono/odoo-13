from odoo import api, fields, models, _


class StockMove(models.Model):
    _inherit = 'stock.move'

    def _create_account_move_line(self, credit_account_id, debit_account_id, journal_id, qty, description, svl_id, cost):
        super(StockMove, self)._create_account_move_line(credit_account_id, debit_account_id, journal_id, qty, description, svl_id, cost)

        obj = self.env['account.move']

        moves = obj.search([('stock_move_id', '=', self.id)])
        #print('#####')
        #print(self.picking_id.analytic_account_id.id)
        #print('#####')

        for move in moves:
            move.line_ids.write({
                'noplate': self.picking_id.noplate
            })