# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2018-Today Ascetic Business Solution <www.asceticbs.com>
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
from odoo import api, fields, models, _
from datetime import date

class StockQuant(models.Model):
    _inherit = "stock.quant"

    latest_purchase_cost = fields.Float(string='Latest Purchase Cost',help="Latest Purchase Cost")


#Class is Extended for new feature for set latest purchase cost on stock.quant model.
class PurchaseOrderofstock(models.Model):
    _inherit = "purchase.order"

    #This function is find the latest order date and write that products unit price on stock.quant model's product.  
    def _set_latest_cost(self): 

        latest_product_line = self.env['purchase.order.line'].search([('order_id.state','in',('purchase','done'))]) 
        product_list = []

        for product in latest_product_line:
            if product.product_id:
                product_list.append(product.product_id)

        for product in product_list:
            if product:
                order_line = self.env['purchase.order.line'].search([('product_id','=',product.id),('order_id.state','in',('purchase','done'))]) 
                max_pro_date = 0
                max_pro = 0

                for line in order_line:
                    if line.date_order > max_pro_date:
                        max_pro_date = line.date_order
                        max_pro = line 
                    stock_product = self.env['stock.quant'].search([('product_id','=',max_pro.product_id.id)])

                    for product in stock_product:
                        if product:
                            if max_pro.product_qty > 0:
                                latest_price = product.qty * max_pro.price_unit
                                product.latest_purchase_cost = latest_price

