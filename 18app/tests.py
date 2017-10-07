# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from unittest import TestCase

from mock import patch

from .api import API


class Test18App(TestCase):
    canned_response = {
        'nominativoBeneficiario': 'RSSMRA99A01H501E',
        'partitaIvaEsercente': 'AAAAAA00H01H501P',
        'ambito': 'LIBRI',
        'bene': 'LIBRO',
        'importo': 10.0
    }
    configuration = {}

    def test_check(self):
        soap_api = API(**self.configuration)
        data = soap_api.check(self.codice)
        self.assertEqual(data['nominativoBeneficiario'], 'RSSMRA99A01H501E')
        self.assertEqual(data['partitaIvaEsercente'], 'AAAAAA00H01H501P')
        self.assertEqual(data['importo'], 10)

    def test_spend(self):
        soap_api = API(**self.configuration)
        data = soap_api.spend(self.codice)
        self.assertEqual(data['nominativoBeneficiario'], 'RSSMRA99A01H501E')
        self.assertEqual(data['partitaIvaEsercente'], 'AAAAAA00H01H501P')
        self.assertEqual(data['importo'], 10)

    def test_authorize(self):
        soap_api = API(**self.configuration)
        data = soap_api.authorize(self.codice)
        self.assertEqual(data['nominativoBeneficiario'], 'RSSMRA99A01H501E')
        self.assertEqual(data['partitaIvaEsercente'], 'AAAAAA00H01H501P')
        self.assertEqual(data['importo'], 10)

    def test_confirm(self):
        soap_api = API(**self.configuration)
        data = soap_api.confirm(self.codice, 10)
        self.assertEqual(data, 'OK')

    def test_cancel_transaction(self):
        soap_api = API(**self.configuration)
        data = soap_api.check(self.codice)
        self.assertEqual(data['importo'], 10)
        data = soap_api.authorize(self.codice)
        self.assertEqual(data['importo'], 10)
        data = soap_api.check(self.codice)
