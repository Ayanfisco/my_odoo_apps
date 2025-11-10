# -*- coding: utf-8 -*-
from odoo import api, fields, models


class InvoiceReminderSettings(models.Model):
    _name = 'invoice.reminder.settings'
    _description = 'Invoice Payment Reminder Settings'

    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)
    active = fields.Boolean(string='Enable Reminders', default=True)

    # Reminder Tiers
    first_reminder_days = fields.Integer(string='First Reminder (Days Overdue)', default=3)
    second_reminder_days = fields.Integer(string='Second Reminder (Days Overdue)', default=7)
    final_reminder_days = fields.Integer(string='Final Reminder (Days Overdue)', default=14)

    # Email Configuration
    send_email = fields.Boolean(string='Send Email Reminders', default=True)
    email_from = fields.Char(string='From Email', help='Leave empty to use company email')

    @api.model
    def get_settings(self):
        """Get or create settings for current company"""
        settings = self.search([('company_id', '=', self.env.company.id)], limit=1)
        if not settings:
            settings = self.create({'company_id': self.env.company.id})
        return settings