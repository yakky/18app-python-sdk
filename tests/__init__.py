# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from mock import patch
from unittest import TestCase
import os.path

from python_18app.api import API


class Test18App(TestCase):
    merchant = 'AAAAAA00H01H501P'
    canned_response = {
        'nominativoBeneficiario': 'RSSMRA99A01H501F',
        'partitaIvaEsercente': merchant,
        'ambito': 'LIBRI',
        'bene': 'LIBRO',
        'importo': 10.0
    }
    configuration = {
        'endpoint': '18app',
        'certificate': os.path.join(os.path.dirname(__file__), 'share', '18app.pem'),
        'certificate_key': os.path.join(os.path.dirname(__file__), 'share', '18app.pem'),
        'keystore': os.path.join(os.path.dirname(__file__), 'share', 'keyStore-test.pem'),
        'merchant': merchant
    }
    voucher = ''

    def test_check(self):
        soap_api = API(**self.configuration)
        data = soap_api.check(self.voucher)
        self.assertEqual(data['nominativoBeneficiario'], self.canned_response['nominativoBeneficiario'])
        self.assertEqual(data['partitaIvaEsercente'], self.merchant)
        self.assertEqual(data['importo'], 10)

    def atest_spend(self):
        soap_api = API(**self.configuration)
        data = soap_api.spend(self.voucher)
        self.assertEqual(data['nominativoBeneficiario'], self.canned_response['nominativoBeneficiario'])
        self.assertEqual(data['partitaIvaEsercente'], self.merchant)
        self.assertEqual(data['importo'], 10)

    def test_authorize(self):
        soap_api = API(**self.configuration)
        data = soap_api.authorize(self.voucher)
        self.assertEqual(data['nominativoBeneficiario'], self.canned_response['nominativoBeneficiario'])
        self.assertEqual(data['partitaIvaEsercente'], self.merchant)
        self.assertEqual(data['importo'], 10)

    def test_confirm(self):
        soap_api = API(**self.configuration)
        data = soap_api.confirm(self.voucher, 10)
        self.assertEqual(data, 'OK')
