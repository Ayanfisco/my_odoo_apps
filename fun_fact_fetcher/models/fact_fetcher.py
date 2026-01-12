from odoo import models, fields, api, _
import logging
import requests

_logger = logging.getLogger(__name__)

class FactFetcher(models.Model):
    _name = 'fact.fetcher'
    _description = 'Fetch Random Facts from an External API'

    name = fields.Char(string='Fact title', default="My Fact")
    fact_text = fields.Text(string='Random Fact')
    fetch_date = fields.Datetime(string='Fetched On')

    def fetch_random_fact(self):
        url = "https://uselessfacts.jsph.pl/random.json?language=en"

        try:
            response = requests.get(url, timeout=10)

            if response.status_code == 200:
                data = response.json()

                self.write({
                    'fact_text': data.get('text', 'No fact found.'),
                    'fetch_date': fields.Datetime.now()
                })

                #Show success message
                return{
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': _('Success'),
                        'message': _('Random fact fetched successfully.'),
                        'type': 'success',
                        'sticky': False,
                    }
                }
            else:
                _logger.error(f"API returned status code {response.status_code}")
        except Exception as e:
            _logger.error(f"Error fetching fact: {str(e)}")

            # Show error message to user
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Error!',
                    'message': f'Could not fetch fact: {str(e)}',
                    'type': 'danger',
                    'sticky': False,
                }
            }
