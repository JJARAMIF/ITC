# -*- coding: utf-8 -*-
{
    'name': "l10n_ec_pos",
    'summary': """
    Cambios en el POS para Ecuador
    """,
    'description': """
        Agregar campos del contacto requeridos en el POS
    """,
    'author': "ITC Tecnologia",
    'website': "http://www.itc.ec",
    'category': 'POS',
    'version': '1.1',
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
