# -*- coding: utf-8 -*-
{
    'name': 'Product Salesman Group',
    'version': '1.0',
    'category': 'Sales Management',
    'sequence': 14,
    'summary': 'Sales, Product, Category, Clasification',
    'description': """
Product Salesman Group
======================
    """,
    'author':  'Ingenieria ADHOC',
    'website': 'www.ingadhoc.com',
    'images': [
    ],
    'depends': [
        'product',
    ],
    'data': [
        'product_view.xml',
        'salesman_group_view.xml',
        'res_user.xml',
        'security/ir.model.access.csv',
        'security/sale_security.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
