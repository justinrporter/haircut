# thanks https://github.com/supernifty/django-paypal-store-example/blob/master/samplesite/sampleapp/paypal.py

import decimal
import urllib
import sys
import ssl

from django.conf import settings

import models

class Verify(object):
    '''builds result, results, response'''
    def __init__(self, tx):
        try:
            transaction = models.Donation.objects.get(transaction_id=tx)
            self.result = 'Transaction %s has already been processed' % tx
            self.response = self.result
        except models.Donation.DoesNotExist:
            post = {}
            post['cmd'] = '_notify-synch'
            post['tx'] = tx
            post['at'] = settings.PAYPAL_PDT_TOKEN
            ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            self.response = urllib.urlopen( settings.PAYPAL_PDT_URL, urllib.urlencode(post),context=ctx).read()
            lines = self.response.split('\n')
            self.result = lines[0].strip()
            self.results = dict()
            for line in lines[1:]: # skip first line
                linesplit = line.split('=', 2)
                if len(linesplit) == 2:
                    self.results[linesplit[0].strip()] = urllib.unquote(linesplit[1].strip())

    def success(self):
        return self.result == 'SUCCESS' and self.results['payment_status'] == 'Completed'

    def amount(self):
        return self.results['payment_gross']

    def email(self):
        return urllib.unquote(self.results['payer_email'])
