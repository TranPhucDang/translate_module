# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2016-today Ascetic Business Solution <www.asceticbs.com>
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

class Employee(models.Model):

    _inherit = "hr.employee"

    purchase_order_count = fields.Integer(compute='_compute_purchase_order', string='Number of Purchase Order')
    purchase_order_stages = fields.Char(compute='_compute_purchase_order', string='Purchase Order Status')

    def _compute_purchase_order(self):
        for employee in self:
            user = employee.user_id
            if user:
                orders = self.env['purchase.order'].sudo().search([('create_uid','=',user.id)])
                employee.purchase_order_count = str(len(orders))
                tt_order = {}
                count = 0
                order_state_text = ''
                for order in orders:
                    if order.state not in tt_order:
                        value = dict(self.env['purchase.order'].fields_get(allfields=['state'])['state']['selection'])[order.state]
                        tt_order.update({value:0})
                    state_orders = self.env['purchase.order'].sudo().search([('create_uid','=',user.id),('state','=',order.state)])
                    tt_order[value] = len(state_orders)
                for item in tt_order:
                    if tt_order[item] != 0:
                        if order_state_text:
                            order_state_text = order_state_text + ' | ' + item + ': ' + str(tt_order[item])
                        else:
                            order_state_text =  item + ': ' + str(tt_order[item])
                employee.purchase_order_stages = order_state_text

    @api.multi
    def display_employee_purchase_order(self):
        """Display employee purchase order"""
        if self.user_id:
            context="{'group_by':'state'}"
            template_id = self.env.ref('purchase.purchase_order_tree').id
            search_id = self.env.ref('purchase.view_purchase_order_filter').id
            return {
                'name': _('Employee Purchase Order'),
                'view_type': 'form',
                'view_mode': 'tree,kanban,pivot,graph,calendar,form',
                'res_model': 'purchase.order',
                'type': 'ir.actions.act_window',
                'view_id': template_id,
                'views': [(self.env.ref('purchase.purchase_order_tree').id, 'tree'),
                          (self.env.ref('purchase.view_purchase_order_kanban').id, 'kanban'),
                          (self.env.ref('purchase.purchase_order_pivot').id, 'pivot'),
                          (self.env.ref('purchase.purchase_order_graph').id, 'graph'),
                          (self.env.ref('purchase.purchase_order_calendar').id, 'calendar'),
                          (self.env.ref('purchase.purchase_order_form').id, 'form')],
                'search_view_id': search_id,
                'domain': [('create_uid','=',self.user_id.id)],
                'context': context
             }



