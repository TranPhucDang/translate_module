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

{
    'name': "Lợi nhuận sản phẩm trong đơn đặt hàng",
    'author': 'Ascetic Business Solution',
    'category': 'sale_management',
    'summary': """Thực hiện theo danh sách kiểm tra để đảm bảo thực hiện tất cả các nhiệm vụ quan trọng trước khi xác nhận đơn đặt hàng""",
    'license': 'AGPL-3',
    'website': 'http://www.asceticbs.com',
    'description': """
""",
    'version': '1.0',
    'depends': ['base','sale_management','product'],
    'data': ['security/ir.model.access.csv','views/sale_task_view.xml','views/product_template_view.xml','views/sales_order_view.xml','views/sale_task_analysis.xml'],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
