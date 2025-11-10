# -*- coding: utf-8 -*-
from datetime import date
from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class AccountMove(models.Model):
    _inherit = 'account.move'

    reminder_count = fields.Integer(string='Reminders Sent', default=0, readonly=True)
    last_reminder_date = fields.Date(string='Last Reminder Date', readonly=True)
    days_overdue = fields.Integer(string='Days Overdue', compute='_compute_days_overdue', store=False)

    @api.depends('invoice_date_due', 'payment_state')
    def _compute_days_overdue(self):
        """Calculate how many days the invoice is overdue"""
        for invoice in self:
            if invoice.invoice_date_due and invoice.payment_state not in ['paid', 'in_payment']:
                delta = date.today() - invoice.invoice_date_due
                invoice.days_overdue = max(0, delta.days)
            else:
                invoice.days_overdue = 0

    @api.model
    def _cron_send_payment_reminders(self):
        """Cron job to check and send payment reminders"""
        _logger.info('Starting payment reminder cron job...')

        settings = self.env['invoice.reminder.settings'].get_settings()
        if not settings.active:
            _logger.info('Payment reminders are disabled')
            return

        # Find overdue invoices
        overdue_invoices = self.search([
            ('move_type', '=', 'out_invoice'),
            ('state', '=', 'posted'),
            ('payment_state', 'in', ['not_paid', 'partial']),
            ('invoice_date_due', '<', date.today())
        ])

        sent_count = 0
        for invoice in overdue_invoices:
            if invoice._should_send_reminder(settings):
                invoice._send_payment_reminder(settings)
                sent_count += 1

        _logger.info(f'Payment reminder cron completed. Sent {sent_count} reminders.')

    def _should_send_reminder(self, settings):
        """Check if reminder should be sent based on days overdue"""
        days_overdue = self.days_overdue

        # Define reminder thresholds
        reminder_days = [
            settings.first_reminder_days,
            settings.second_reminder_days,
            settings.final_reminder_days
        ]

        # Check if we should send reminder today
        if days_overdue in reminder_days:
            # Don't send if already sent today
            if self.last_reminder_date == date.today():
                return False
            return True

        return False

    def _send_payment_reminder(self, settings):
        """Send payment reminder email"""
        template = self._get_reminder_template()
        if not template:
            _logger.warning(f'No reminder template found for invoice {self.name}')
            return

        try:
            template.send_mail(self.id, force_send=True)
            self.write({
                'reminder_count': self.reminder_count + 1,
                'last_reminder_date': date.today()
            })

            # Log in chatter
            self.message_post(
                body=_('Payment reminder sent to %s (%s days overdue)') % (
                    self.partner_id.name, self.days_overdue
                ),
                subject=_('Payment Reminder Sent')
            )
            _logger.info(f'Reminder sent for invoice {self.name}')
        except Exception as e:
            _logger.error(f'Failed to send reminder for invoice {self.name}: {str(e)}')

    def _get_reminder_template(self):
        """Get appropriate email template based on reminder count"""
        settings = self.env['invoice.reminder.settings'].get_settings()

        if self.days_overdue >= settings.final_reminder_days:
            template_name = 'invoice_payment_reminder.email_template_final_reminder'
        elif self.days_overdue >= settings.second_reminder_days:
            template_name = 'invoice_payment_reminder.email_template_second_reminder'
        else:
            template_name = 'invoice_payment_reminder.email_template_first_reminder'

        return self.env.ref(template_name, raise_if_not_found=False)

    def action_send_reminder_now(self):
        """Manual action to send reminder immediately"""
        settings = self.env['invoice.reminder.settings'].get_settings()
        self._send_payment_reminder(settings)
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'message': _('Payment reminder sent successfully'),
                'type': 'success',
                'sticky': False,
            }
        }