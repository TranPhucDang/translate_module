# -*- coding: utf-8 -*-
#################################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2017-Today Ascetic Business Solution <www.asceticbs.com>
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
    'name': "Định lượng kho hàng",
    'author': 'Satavan - Business all in one',
    'category': 'Warehouse',
    'summary': """Tính toán và hiển thị số lượng sản phẩm có sẵn từ tất cả các kho dựa trên thời ngian thựcthời gian thực""",
    'license': 'AGPL-3',
    'website': 'https://satavan.com',
    'description': """
""",
    'version': '12.0',
    'depends': ['sale','stock'],
    'data': ['security/warehouse_security.xml','views/product_view.xml'],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
