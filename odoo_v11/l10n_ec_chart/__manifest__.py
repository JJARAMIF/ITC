# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2017 ITC Tecnologia

{
    'name': 'ITC - Accounting',
	'summary': """NIIF SUPERCIAS Plan de Cuentas""",
    'version': '11.1.1',
	'author': "ITC Tecnologia",
    'maintainer': 'ITC Tecnologia',
    'website': 'http://www.itc.ec',
    'license': 'AGPL-3',
    'category': 'Localization',
    'description': """
Modulo Base que inicializa el Plan de Cuentas para Ecuador.
===========================================================
Plan de Cuentas y Localizacion Ecuador.
    """,

    'depends': [
        'account',
    ],
    'data': [
	    'data/l10n_ec_chart.xml',
		'data/account.account.tag.csv',
		'data/account.account.template.csv',
		'data/account_chart_template.yml',
		],
}
