# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2019-today Ascetic Business Solution <www.asceticbs.com>
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

### method of button 'submit' in wizard
class HrEmployeeCreate(models.TransientModel):
    _name = "hr.employee.create"

    name = fields.Many2one('res.partner',string = "Supplier name")
    order_lines = fields.One2many('hr.employee.create.line', 'line_order_id', string='Order Lines') 

    @api.multi
    def create_RFQ(self):
        obj_purchase_order = self.env['purchase.order']
        obj_purchase_order_line = self.env['purchase.order.line']

        emp_purchase_order_id = False

        if self.env.context.get('active_model') == 'hr.employee':
            active_id = self.env.context.get('active_id',False)
 
            employee_id = self.env['hr.employee'].search([('id','=',active_id)])

            purchase_order_dict = {'partner_id': self.name.id,'employee_id' : active_id} 
            purchase_order = obj_purchase_order.create(purchase_order_dict)

            ## create a new dictionary for set value of order lines. 
            for line in self.order_lines:
                if line:
                    product_tmpl_id = self.env['product.product'].search([('id','=',line.product_id.id)])
                    order_line_dict = {
                               'product_id' : product_tmpl_id.id,
                               'product_qty' : line.product_qty,
                               'name' : product_tmpl_id.name, 
                               'date_planned' : datetime.today(),
                               'price_unit' : line.price_unit,
                               'product_uom':product_tmpl_id.uom_id.id,
                               'order_id' : purchase_order.id 
                               }
                emp_purchase_order_id = obj_purchase_order_line.create(order_line_dict)

### create new class for get purchase order lines from wizard    
class HrEmployeeCreateLine(models.TransientModel):
    _name = "hr.employee.create.line"

    product_id = fields.Many2one('product.product', string='Product')
    product_qty = fields.Float('Quantity')
    price_unit = fields.Float('Unit Price')
    line_order_id = fields.Many2one('hr.employee.create')



