{
    'name': 'Dental Practice',
    'version': '0.2',
    'summary': 'A dental practice management',
    'description': '',
    'sequence': 1,
    'author': 'Odoo S.A.',
    'website': 'http://www.odoo.com',
    'depends': ['base', 'contacts', 'stock', 'sale_management', 'website', 'appointment'],
    'data': [
        'views/dental.xml',
        'security/ir.model.access.csv'
    ],
    'assets': {
        'web.assets_backend': [
             'dental_practice/static/src/**/*',
        ],
    },
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3'
}
