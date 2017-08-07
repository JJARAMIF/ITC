# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2017 ITC Tecnologia

{
    'name': 'ITC - POS',
    'summary': """Cambios en el POS para Ecuador""",
	'version': '1.2',
	'author': "ITC Tecnologia",
	'maintainer': 'ITC Tecnologia',
	'website': 'http://www.itc.ec',
    'license': 'AGPL-3',
    'category': 'Localization',
    'description': """
        Agregar campos del contacto requeridos en el POS
    """,

    'depends': [
        'point_of_sale',
    ],
    'data': [
        'data/pos.xml',
        'views.xml'
    ],
    'qweb': [
        'static/src/xml/l10n_ec_pos.xml',
        'static/src/xml/pos.xml'
    ]
}
