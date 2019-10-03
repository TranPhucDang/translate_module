# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2018-today Ascetic Business Solution <www.asceticbs.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################

from odoo import api, fields, models,_
from datetime import datetime
from odoo.exceptions import ValidationError

### Create new classs for displaying table for top selling products with amount in from_date to to_date using wizard 
class TopBuying(models.TransientModel):
    _name = "topbuying.orderline"

    date_from = fields.Date('From Date')
    date_to = fields.Date('To Date')

    @api.onchange('date_to')
    def onchange_date_to(self):
        for record in self:
            if record.date_to < record.date_from:
                raise ValidationError("Please select right date")
            else:
                pass

    ### Function for display tree view of products with amount in descending order for only Vendor Bills
    @api.multi
    def top_buying_product(self):
        vendor_bill_list = [] 
        invoice_line_list = []
        final_list = []
        order_line_list = []
        product_topbuying = self.env['products.vendorbills']
        vendor_bill_ids = self.env['account.invoice'].search([('date_invoice','<=',self.date_to),('date_invoice','>=',self.date_from),('state','in',('paid','open'))])
        if vendor_bill_ids:
            for vendor_bill in vendor_bill_ids:
                vendor_bill_list.append(vendor_bill)
            for vendor_bill in vendor_bill_list:
                for invoice_lines in vendor_bill.invoice_line_ids:
                    if invoice_lines.invoice_id.type == 'in_invoice':
                        invoice_line_list.append(invoice_lines)
            for product in invoice_line_list:
                if product.product_id:
                    total_amount = 0
                    for same_product in invoice_line_list:
                        if product.product_id == same_product.product_id:
                            total_amount = total_amount + same_product.price_subtotal
                    product_dict = { 'product' : product.product_id.id, 'amount' : total_amount }
                    topbuying_product_id = product_topbuying.create(product_dict)
                    if topbuying_product_id.product not in final_list: 
                        order_line_list.append(topbuying_product_id)
                        final_list.append(topbuying_product_id.product)
        return {
            'name': _('Top Buying Products'),
            'type': 'ir.actions.act_window',
            'domain': [('id','in',[x.id for x in order_line_list])],
            'view_mode': 'tree',
            'res_model': 'products.vendorbills',
            'view_id': False,
            'action' :'view_top_buying_product_tree',
            'target' : 'current'
        }

