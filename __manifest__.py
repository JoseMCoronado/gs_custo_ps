# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Goodstores Base Customizations/Developments',
    'category': 'Sale',
    'summary': 'Custom',
    'version': '1.0',
    'description': """
Core workflow customizations/developments.
        """,
    'depends': ['base','crm','sale'],
    'data': [
        'data/ir_model.xml',
        'data/ir_model_fields.xml',
        'data/ir_ui_views.xml',
        'data/base_automation.xml',
        'data/created_records.xml',
        'data/ir_ui_qweb.xml'
    ],
    'installable': True,
}
