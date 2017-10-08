# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

import os.path
import requests
from lxml import etree
from zeep import Transport, Client
from zeep.plugins import HistoryPlugin, Plugin


class API(object):
    def __init__(self, endpoint, wsdl, certificate, certificate_key, keystore, merchant):
        """
        API client initialization

        :param endpoint:  18app / docente version
        :param wsdl: absolute path /URL to wsdl
        :param certificate: absolute path to client certificate (PEM format)
        :param certificate_key: absolute path to client private key (PEM format)
        :param keystore: absolute path to keystore
        :param merchant: merchant code
        """
        session = requests.Session()
        namespace = ''
        if endpoint == '18app':
            namespace = 'http://bonus.mibact.it/VerificaVoucher/'
        elif endpoint == 'docente':
            namespace = 'http://bonus.miur.it/VerificaVoucher/'
        session.cert = (
            certificate,
            certificate_key
        )
        session.verify = os.path.abspath(keystore)
        transport = Transport(session=session)
        self.merchant = merchant
        self.client = Client(wsdl, transport=transport)
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
