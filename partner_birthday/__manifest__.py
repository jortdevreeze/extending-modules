{
    'name': 'Partner Birthday',
    'version': '18.0.1.0.0',
    'summary': 'Add date of birth to partners and set up birthday reminders',
    'description': '''
        This module adds a date of birth field to partners and automatically
        creates reminders for the responsible salesperson to congratulate
        the partner on their birthday with their calculated age.
    ''',
    'author': 'Jort de Vreeze',
    'website': 'https://www.example.com',
    'category': 'CRM',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'data/automated_actions.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
