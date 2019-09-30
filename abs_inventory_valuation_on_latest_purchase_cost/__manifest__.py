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
    'name'    : "Định giá hàng tồn kho",
    'author'  : 'Satavan - Business all in one',
    'category': 'Warehouse',
    'summary' : """Định giá hàng tồn kho dựa trên chi phí mua hàng mới nhất""",
    'license' : 'AGPL-3',
    'website' : 'https://satavan.com',
    'description': """ """,
    'version' : '1.0',
    'depends' : ['base','stock','purchase'],
    'data'    : ['views/stock_quant_view.xml','views/stock_quant_schedular_view.xml'],
    'images': ['static/description/banner.png'],
    'installable' : True,
    'application' : True,
    'auto_install': False,
}
