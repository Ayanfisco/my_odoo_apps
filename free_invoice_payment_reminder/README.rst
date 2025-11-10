========================
Invoice Payment Reminder
========================

Automated invoice payment reminders for overdue invoices to improve cash flow.

Features
========

* Automated daily checks for overdue invoices
* Multi-tier reminder system (3, 7, 14 days overdue)
* Customizable email templates
* Reminder history tracking
* Dashboard with reminder statistics
* Configurable reminder settings per company
* Works with standard Odoo invoicing
* Manual reminder trigger option

Installation
============

1. Download the module
2. Place it in your Odoo addons directory
3. Update the app list (Apps → Update Apps List)
4. Search for "Invoice Payment Reminder"
5. Click Install

Configuration
=============

1. Go to Accounting → Configuration → Payment Reminder Settings
2. Configure your reminder schedule:

   * First Reminder: Days overdue before first notice (default: 3)
   * Second Reminder: Days overdue before second notice (default: 7)
   * Final Reminder: Days overdue before final warning (default: 14)

3. Set email configuration (optional)
4. Enable/disable reminders using the Active toggle

Usage
=====

Automatic Mode
--------------

Once configured, the system automatically:

* Checks for overdue invoices daily at 9:00 AM
* Sends appropriate reminders based on days overdue
* Logs all reminder activity in invoice chatter
* Tracks reminder count and last reminder date

Manual Mode
-----------

To send a reminder immediately for a specific invoice:

1. Open the invoice
2. Click "Send Reminder" button in the header
3. System will send the appropriate reminder based on days overdue

Viewing Reminder Information
-----------------------------

For each invoice, you can see:

* Days Overdue: Calculated automatically
* Reminder Count: How many reminders have been sent
* Last Reminder Date: When the last reminder was sent

Email Templates
===============

The module includes three professional email templates:

1. **First Reminder**: Friendly payment reminder
2. **Second Reminder**: More urgent follow-up
3. **Final Reminder**: Final warning before action

All templates can be customized through Settings → Technical → Email Templates

Requirements
============

* Odoo 18.0
* account module (installed by default)
* mail module (installed by default)
* Configured outgoing email server

Support
=======

For support, bug reports, or feature requests:

License
=======

OPL-1 (Odoo Proprietary License v1.0)

Credits
=======

Author: Tech Joe

Changelog
=========

Version 18.0.1.0.0 (2024-11-09)
--------------------------------

* Initial release
* Automated payment reminder system
* Three-tier reminder emails
* Configurable reminder schedule
* Reminder tracking and history
* Manual reminder trigger