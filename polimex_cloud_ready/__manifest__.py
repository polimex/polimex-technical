# -*- coding: utf-8 -*-

{
    'name': 'Odoo fixes for cloud based deployment in multi-company environment',
    'version': '1.0',
    'category': 'Technical Settings',
    'summary': 'Odoo fixes for cloud based deployment in multi-company environment',
    'author': 'Polimex Dev Team',
    'license': 'LGPL-3',

    'description': """
        Odoo fixes for cloud based deployment in multi-company environment
       """,

    'website': 'https://polimex.co',

    'depends': ['base',],

    'data': [
        # 'security/base_security.xml',
        # 'data/hr_leave_type.xml',
        # 'data/paper_format.xml',
        # 'views/hr_leave_type_views.xml',
        # 'views/hr_employee.xml',
        # 'reports/report_form_76_bg.xml',
        # 'wizards/report_form_76_wizard.xml',
    ],

    "images": [
        'static/images/main_screenshot.png',
    ],

    'installable': True,
    'auto_install': False,
}
