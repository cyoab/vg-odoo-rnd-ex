{
    'name': 'Estate',
    'description': 'Real Estate management module',
    'version': '1.0',
    'category': 'Real Estate/Estate',
    'depends': ['sale'], 
    'data': [
        'security/ir.model.access.csv',
        'security/estate_security.xml',
        'views/estate_views.xml',
        'views/estate_menu.xml',
    ],
    'license': 'OPL-1',
    'application': True,
}