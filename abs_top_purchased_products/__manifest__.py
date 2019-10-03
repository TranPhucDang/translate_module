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
    'name': "Sản phẩm bán chạy",
    'author': 'Satavan - Business all in one',
    'category': 'purchase',
    'summary': """Báo cáo sản phẩm bán chạy nhất dựa trên số lượng bán""",
    'website': 'https://satavan.com',
    'description': """
""",
    'version': '1.0',
    'depends': ['base','product','purchase'],
    'data': ['wizard/top_purchase_view.xml','views/top_purchased_view.xml','report/selected_product_report.xml','report/selected_product_template.xml','report/selected_product_amount_report.xml','report/selected_product_amount_template.xml'],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
