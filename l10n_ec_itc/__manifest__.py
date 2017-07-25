# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2017 ITC Store

{
    'name': 'ITC - Accounting',
    'version': '1.1',
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
