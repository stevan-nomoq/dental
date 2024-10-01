{
    'name': 'Dental Practice',
    'version': '0.3',
    'summary': 'A dental practice management',
    'description': '',
    'sequence': 1,
    'author': 'Odoo S.A.',
    'website': 'http://www.odoo.com',
    'depends': ['base', 'contacts', 'stock', 'sale_management', 'website', 'appointment'],
    'data': [
        'views/dental.xml',
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'data/treatments.xml',
        'data/diagnostics.xml',
        'wizard/dental_wizard_views.xml'
    ],
    'assets': {
        'web.assets_backend': [
            # 'dental_practice/static/src/**/*',
        ],
    },
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3'
}
