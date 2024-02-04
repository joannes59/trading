{
    'name': "Trading base",
    'summary': "Common element of trading",
    'description': """
        Description détaillée de votre module.
    """,
    'author': "joannes59",
    "license": "AGPL-3",
    'website': "github.com/joannes59/trading",
    'category': 'trading',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'views/menu_views.xml',
        'views/trading_asset_views.xml',

        'security/res_group.xml',
        'security/ir.model.access.csv'

    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
