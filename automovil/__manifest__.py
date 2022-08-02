
# -*- coding: utf-8 -*-
###############################################################################
#
#    Carlos Contreras<carlosecv@realsystems.com.mx>
#
#    Copyright (c) All rights reserved:
#        (c) 2022  Real Systems
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#
#    Odoo and OpenERP is trademark of Odoo S.A.
#
###############################################################################
{
    'name': 'Automovil Module Course',
    'summary': 'This is a test course for programming in Odoo',
    'version': '15.0.1',

    'description': """
Automovil Module Project.
==============================================

* Automovil
* Characteristics
* Owner Automoviles

Titulo 1
============

Titulo 2
============

Hola <b>mundo<b> este es otro Texto


    """,

    'author': 'Real Systems',
    'maintainer': 'Carlos Enrique Contreras Vara',
    'contributors': ['Edgar Giovanni <edgarpv@realsystems.com.mx>','Carlos Daniel <carloscp@realsystems.com.mx>',
                      'Alejandro del Rio <adelriocastillo@gmail.com>',  ],

    'website': 'https://www.realsystems.com.mx/',

    'license': 'AGPL-3',
    'category': 'Instruction Course',

    'depends': [
        'base'
    ],
    'external_dependencies': {
        'python': [
        ],
    },
    'data': [
        'data/decimal_precision.xml',
        'security/ir.model.access.csv',
        'views/automovil_views.xml',
    ],
    'demo': [
    ],
    'js': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'images': [
    ],
    'test': [
    ],

    'installable': True
}
