# -*- coding:utf-8 -*-

from odoo import fields, models, api

class CustomAction(models.TransientModel):
    _name = 'wizard.sale.order.custom'

    def _default_orders(self):
        return self.env['sale.order'].browse(self._context.get('active_ids'))

    sale_ids = fields.Many2many('sale.order', string='Sales', default=_default_orders,
                                 auto_join=True, required=True, readonly=True)

    @api.multi
    def confirm_action(self):
        if self.sale_ids:
        	for sale in self.sale_ids:
        		# Do something here
