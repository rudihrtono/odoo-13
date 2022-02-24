# ?? 2015-2016 Akretion (http://www.akretion.com)
# @author Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'BSA Stock Negative',
    'version': '13.0.1.0.0',
    'category': 'Integration',
    'summary': 'BSA Stock Negative',
    'sequence': '300',
    'author': 'Dx',
    'maintainer': 'Dx',
    'license': 'LGPL-3',
    'support': 'support@waresix.com',
    'website': '',
    'depends': ['stock'],
    'demo': [],
    'data': [
             
        'views/product_product_views.xml', 'views/stock_location_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
