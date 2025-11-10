# -*- coding: utf-8 -*-
{
    'name': 'Free Invoice Payment Reminder',
    'version': '18.0.1.0.0',
    'category': 'Accounting/Accounting',
    'summary': 'Automated invoice payment reminders for overdue invoices',
    'description': """
Invoice Payment Reminder
=========================
Automatically send payment reminders for overdue invoices to improve cash flow.

Key Features:
-------------
* Automated daily checks for overdue invoices
* Multi-tier reminder system (3, 7, 14 days overdue)
* Customizable email templates
* Reminder history tracking
* Dashboard with reminder statistics
* Configurable reminder settings per company
* Works with standard Odoo invoicing

Benefits:
---------
* Reduce late payments
* Improve cash flow
* Save time on manual follow-ups
* Professional automated communication
* Track all reminder activities

Perfect for small to medium businesses looking to streamline their accounts receivable process.
    """,
    'author': 'Tech Joe',
    'license': 'OPL-1',
    'price': 49.00,
    'currency': 'USD',
    'depends': ['account', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
        'data/email_templates.xml',
        'views/reminder_settings_views.xml',
        'views/account_move_views.xml',
    ],
    'images': [
        'static/description/icon.png',
        'static/description/screenshot_1.png',
        'static/description/screenshot_2.png',
        'static/description/screenshot_3.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}