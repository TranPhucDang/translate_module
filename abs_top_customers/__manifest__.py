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
{
    'name': "Khách hàng hàng đầu",
    'author': 'Satavan - Business all in one',
    'category': 'Sales',
    'summary': """Hiển thị khách hàng hàng đầu từ đơn đặt hàng""",
    'website': 'https://satavan.com',
    'license': 'AGPL-3',
    'description': """ """,
    'version': '12.0.0.1',
    'depends': ['base','sale_management'],
    'data': ['security/ir.model.access.csv','wizard/wizard_top_customers_view.xml','views/menu_top_customers.xml','views/tree_view_top_customer_view.xml'],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}




