# -*- coding: utf-8 -*-
{
    'name': "Home Tracker",
    'version': '0.1',
    'summary': """Gestor de Propiedades Personal""",
    'description': """
                Software Gestor de Propiedades para uso personal o individual    
                """,
    'author': "Jesús Salvador Alcalá Arroyo",
    'website': "",
    'category': 'Management',

    'depends': ['base','contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/home_tracker_menus.xml',
        'views/cat_maintenance_view.xml',
        'views/insurance_policies_view.xml',
        'views/mantenance_n_services.xml',
        'views/penalties_view.xml',
        'views/contracts_view.xml',
        'views/properties_view.xml',
        'views/tenancy_view.xml',
    ],
    'demo': ['demo/demo.xml',],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
