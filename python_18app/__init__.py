# -*- coding: utf-8 -*-

"""Top-level package for 18App Merchant Python SDK."""
from decimal import Decimal

from zeep.exceptions import Fault

__author__ = """Developers Italia"""
__email__ = 'info@developers.italia.it'
__version__ = '0.1.0'


def voucher_value(api, coupon):
    try:
        response = api.check(coupon)
        print(response)
    except Fault:
        return False
    try:
        return Decimal(response['importo'])
    except AttributeError:
        return Decimal('0')


def voucher_spend(api, coupon):
    try:
        response = api.spend(coupon)
    except Fault:
        return False
    try:
        return Decimal(response['importo'])
    except AttributeError:
        return Decimal('0')
