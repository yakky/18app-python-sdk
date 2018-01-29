# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import os.path
import requests
from zeep import Transport, Client


class API(object):
    ENDPOINT_18APP = '18app'
    ENDPOINT_CARTA_DOCENTE = 'docente'
    ENDPOINT_18APP_TEST = '18app_test'
    ENDPOINT_CARTA_DOCENTE_TEST = 'docente_test'

    def __init__(self, endpoint, certificate, certificate_key, merchant, keystore=None, plugins=None):
        """
        API client initialization

        :param endpoint: 18app / docente version
        :param certificate: absolute path to client certificate (PEM format)
        :param certificate_key: absolute path to client private key (PEM format)
        :param merchant: merchant code
        :param keystore: absolute path to endpoint ssl certificate (only if self signed, for test environment)
        :param plugins: zeep plugins to be used by the client
        """
        session = requests.Session()
        namespace = ''
        wsdl = ''
        wsdl_path = ''
        if endpoint == self.ENDPOINT_18APP:
            namespace = 'http://bonus.mibact.it/VerificaVoucher/'
            wsdl = 'VerificaVoucher-18app.wsdl'
        elif endpoint == self.ENDPOINT_18APP_TEST:
            namespace = 'http://bonus.mibact.it/VerificaVoucher/'
            wsdl = 'VerificaVoucher-18app-test.wsdl'
        elif endpoint == self.ENDPOINT_CARTA_DOCENTE:
            namespace = 'http://bonus.miur.it/VerificaVoucher/'
            wsdl = 'VerificaVoucher-docente.wsdl'
        elif endpoint == self.ENDPOINT_CARTA_DOCENTE_TEST:
            namespace = 'http://bonus.miur.it/VerificaVoucher/'
            wsdl = 'VerificaVoucher-docente-test.wsdl'
        if wsdl:
            wsdl_path = os.path.join(os.path.dirname(__file__), 'share', wsdl)
        session.cert = (
            certificate,
            certificate_key
        )
        if keystore:
            session.verify = os.path.abspath(keystore)
        transport = Transport(session=session)
        self.merchant = merchant
        self.plugins = plugins
        self.client = Client(wsdl_path, plugins=plugins, transport=transport)
        self.client.set_ns_prefix('ns', namespace)

    def check(self, voucher):
        """
        Check if the voucher code is valid

        :param voucher: voucher code
        :return: API response
        """
        Check = self.client.get_type('ns:Check')
        check = Check(tipoOperazione='1', codiceVoucher=voucher, partitaIvaEsercente=self.merchant)
        data = self.client.service.Check(check)
        return data

    def spend(self, voucher):
        """
        Spend the voucher

        :param voucher: voucher code
        :return: API response
        """
        Check = self.client.get_type('ns:Check')
        check = Check(tipoOperazione='2', codiceVoucher=voucher, partitaIvaEsercente=self.merchant)
        data = self.client.service.Check(check)
        return data

    def authorize(self, voucher):
        """
        Authorize

        :param voucher: code
        :return: tns:CheckResponse
        """
        Check = self.client.get_type('ns:Check')
        check = Check(tipoOperazione='3', codiceVoucher=voucher, partitaIvaEsercente=self.merchant)
        data = self.client.service.Check(check)
        return data

    def confirm(self, voucher, amount):
        """
        Call the confirm API to spend the voucher

        :param voucher: code
        :param amount: amount to spend
        :return: tns:ConfirmResponse
        """
        Confirm = self.client.get_type('ns:Confirm')
        confirm = Confirm(
            tipoOperazione='1', codiceVoucher=voucher, importo=amount
        )
        data = self.client.service.Confirm(confirm)
        return data
