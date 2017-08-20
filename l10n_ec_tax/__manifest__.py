# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2017 ITC Tecnologia

{
    'name': 'ITC - Taxes',
	'summary': """Plan de Impuestos Ecuador""",
    'version': '10.1.2',
	'author': "ITC Tecnologia",
    'maintainer': 'ITC Tecnologia',
    'website': 'http://www.itc.ec',
    'license': 'AGPL-3',
    'category': 'Accounting',
    'description': """
Modulo Base que inicializa el Plan de Impuestos para Ecuador.
=============================================================
Plan de Impuestos Ecuador.
    """,

    'depends': [
        'l10n_ec_chart',
    ],
    'data': [
		'data/l10n_ec_tax.xml',
		'data/account.account.tag.csv',
        'data/account.tax.group.csv',
		'data/account.tax.template.csv',
        'data/account.fiscal.position.csv',
        'security/ir.model.access.csv',
        'view/views.xml',
        'view/account_tax_report.xml',
		'data/account_tax_template.yml',
    ]
}
