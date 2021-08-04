import unittest
import zendesk
import requests

class testZendesk(unittest.TestCase):
    def test_getTickets(self):
        result = zendesk.getTickets()
        validResponse = requests.get('https://zcc8848.zendesk.com/api/v2/tickets' , headers={"Authorization": "Basic %s" % 'cGFydGhlc2hrcGF0ZWxAZ21haWwuY29tOk15bmFtZWlzZG9uNQ=='})
        self.assertEqual(result, validResponse.json())