# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2017 ITC Tecnologia

{
    'name': 'ITC - Accounting',
	'summary': """NIIF SUPERCIAS Plan de Cuentas.""",
    'version': '1.2',
	'author': "ITC Tecnologia",
    'maintainer': 'Fabrica de Software Libre',
    'website': 'http://www.itc.ec',
    'license': 'AGPL-3',
    'category': 'Localization',
    'description': """
Modulo Base Odoo que inicializa el Plan de Cuentas para Ecuador.
==============================================================================

Plan de Cuentas y Localizacion Ecuador.
    """,
    'author': 'ITC Store',
    'depends': [
        'account',
        'base_vat',
        'base_iban',
    ],
    'data': [
        'data/l10n_ec_chart_data.xml',
		'data/account.account.template.csv',
		'data/account_tax_data.xml',
		'data/account_default.xml',
        'data/account_chart_template_data.yml',
		],
}
