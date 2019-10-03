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
from odoo import api, fields, models, _

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    rfq_total = fields.Integer('My RFQ',compute = 'compute_order')
    rfq_order_ids = fields.One2many('purchase.order','employee_id')

    ### compute method for count total number of purchase order 
    @api.multi
    def compute_order(self):
        count = 0
        for employee in self:
            invoices = self.env['purchase.order']
            for record in employee.rfq_order_ids:
                if record.state == 'draft':
                    count += 1 
            employee.rfq_total = count

    ### to display purchase order in oe-button
    @api.multi
    def create_RFQ_lines(self):   
        return {
            'name': _('Purchase Orders'),
            'domain': [('id','in',[x.id for x in self.rfq_order_ids]),('state','=','draft')],
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'purchase.order',
            'view_id': False,
            'views': [(self.env.ref('purchase.purchase_order_tree').id, 'tree'), (self.env.ref('purchase.purchase_order_form').id, 'form')],
            'type': 'ir.actions.act_window' 
        }



