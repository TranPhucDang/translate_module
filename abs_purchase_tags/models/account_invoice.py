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

from odoo import api,fields,models,_

class AccountInvoice(models.Model):
    _inherit ='account.invoice' #Inherit this model becuase we have to display all purchase tag on vendor_bills

    vendor_tag_ids = fields.Many2many('purchase.tag',string='Purchase Tag') #Field to store purchase tag

	
    #Override this function becuase we have to display purchase order tags on Onchange of purchase order id
    @api.onchange('purchase_id')
    def purchase_order_change(self):
        if not self.purchase_id:
            return {}
        if not self.partner_id:
            self.partner_id = self.purchase_id.partner_id.id
	   
        new_lines = self.env['account.invoice.line']
        for line in self.purchase_id.order_line - self.invoice_line_ids.mapped('purchase_line_id'):
            data = self._prepare_invoice_line_from_po_line(line)
            new_line = new_lines.new(data)
            new_line._set_additional_fields(self)
            new_lines += new_line

        self.invoice_line_ids += new_lines

        list1=[]   #define list to store multiple tag ids
        for rec in self.purchase_id: #Get purchase id 
            list1.append(rec.id)

        for i in range(0,len(list1)):   
            tag_id=self.env['purchase.order'].browse(list1[i]).tag_ids
            self.vendor_tag_ids=tag_id
        return {}





        
   
