# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class Price(object):


    _types = {
        'item_price': 'float',
        'shipping': 'float',
        'taxes': 'float',
        'total_price': 'float'
    }

    _attribute_map = {
        'item_price': 'item_price',
        'shipping': 'shipping',
        'taxes': 'taxes',
        'total_price': 'total_price'
    }

    def __init__(self, item_price=None, shipping=None, taxes=None, total_price=None):  # noqa: E501
        self._item_price = None
        self._shipping = None
        self._taxes = None
        self._total_price = None
        self.discriminator = None
        self.item_price = item_price
        self.shipping = shipping
        self.taxes = taxes
        self.total_price = total_price


    @property
    def item_price(self):

        return self._item_price

    @item_price.setter
    def item_price(self, item_price):


        self._item_price = item_price


    @property
    def shipping(self):

        return self._shipping

    @shipping.setter
    def shipping(self, shipping):


        self._shipping = shipping


    @property
    def taxes(self):

        return self._taxes

    @taxes.setter
    def taxes(self, taxes):


        self._taxes = taxes


    @property
    def total_price(self):

        return self._total_price

    @total_price.setter
    def total_price(self, total_price):


        self._total_price = total_price

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self._types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Price, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Price):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

