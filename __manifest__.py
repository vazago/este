{
    'name': "GDUSolapin",

    'summary': """
        Módulo que genera el solapin de una persona a traves
        de los  datos de gdu_persona""",

    'description': """
        Este módulo tiene como proposito imprimir el solapin de una persona
    """,

    'author': "Maykel Muradas Otero",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/solapin_view.xml',
        'report/report_card_front_1.xml',
        'security/ir.model.access.csv'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

