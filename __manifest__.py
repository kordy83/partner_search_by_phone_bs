# -*- coding: utf-8 -*-
{
    'name': "Partner Search By Phone",

    'summary': """
        Enables to search partners in quotation, sale, purchase, invoice etc by the phone and mobile numbers""",

    'description': """
        Enables to search partners in quotation, sale, purchase, invoice etc by the phone and mobile numbers
    """,

    'license': 'LGPL-3',
    'author': "kordy",
    

    'category': 'Uncategorized',
    'version': '16.0.1.0.0',

    'depends': ['base', 'repair'],
    'data': [
        'views/repair_order.xml',
    ],
    'application': True,
    'installable': True,
    
}
