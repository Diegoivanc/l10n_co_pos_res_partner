{
    'name': 'Colombia - Punto de venta - res partner',
    'category': 'Localization',
    'version': '1.0',
    'author': '',
    'license': 'AGPL-3',
    'maintainer': ' ',
    'website': ' ',
    'summary': ' ',
    'description': """
Colombia Point of Sale:
======================
  """,
    'depends': [
        'point_of_sale',
        'l10n_co_res_partner'
       #'l10n_co_tax_extension'
    ],
    'data': [
        'views/pos_view.xml',
        #'views/point_of_sale_view.xml',
        #'report/report_sessionsummary.xml',
        #'security/ir.model.access.csv',
        #'views/report_receipt.xml',
        #'views/view_report_pos_order.xml'
    ],
    'qweb': ['static/src/xml/*.xml'],
    'installable': True,
}
