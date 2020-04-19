# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum
from schema.com_aws_orders.ordernotification.Customer import Customer  # noqa: F401,E501
from schema.com_aws_orders.ordernotification.Price import Price  # noqa: F401,E501
from schema.com_aws_orders.ordernotification.Product import Product  # noqa: F401,E501
from schema.com_aws_orders.ordernotification.Shipping_address import Shipping_address  # noqa: F401,E501

class OrderNotification(object):


    _types = {
        'customer': 'Customer',
        'price': 'Price',
        'product': 'Product',
        'shipping_address': 'Shipping_address',
        'created_at': 'datetime',
        'currency': 'str',
        'order_id': 'float',
        'shipping_id': 'str',
        'tax_price': 'float'
    }

    _attribute_map = {
        'customer': 'customer',
        'price': 'price',
        'product': 'product',
        'shipping_address': 'shipping_address',
        'created_at': 'created_at',
        'currency': 'currency',
        'order_id': 'order_id',
        'shipping_id': 'shipping_id',
        'tax_price': 'tax_price'
    }

    def __init__(self, customer=None, price=None, product=None, shipping_address=None, created_at=None, currency=None, order_id=None, shipping_id=None, tax_price=None):  # noqa: E501
        self._customer = None
        self._price = None
        self._product = None
        self._shipping_address = None
        self._created_at = None
        self._currency = None
        self._order_id = None
        self._shipping_id = None
        self._tax_price = None
        self.discriminator = None
        self.customer = customer
        self.price = price
        self.product = product
        self.shipping_address = shipping_address
        self.created_at = created_at
        self.currency = currency
        self.order_id = order_id
        self.shipping_id = shipping_id
        self.tax_price = tax_price


    @property
    def customer(self):

        return self._customer

    @customer.setter
    def customer(self, customer):


        self._customer = customer


    @property
    def price(self):

        return self._price

    @price.setter
    def price(self, price):


        self._price = price


    @property
    def product(self):

        return self._product

    @product.setter
    def product(self, product):


        self._product = product


    @property
    def shipping_address(self):

        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):


        self._shipping_address = shipping_address


    @property
    def created_at(self):

        return self._created_at

    @created_at.setter
    def created_at(self, created_at):


        self._created_at = created_at


    @property
    def currency(self):

        return self._currency

    @currency.setter
    def currency(self, currency):


        self._currency = currency


    @property
    def order_id(self):

        return self._order_id

    @order_id.setter
    def order_id(self, order_id):


        self._order_id = order_id


    @property
    def shipping_id(self):

        return self._shipping_id

    @shipping_id.setter
    def shipping_id(self, shipping_id):


        self._shipping_id = shipping_id


    @property
    def tax_price(self):

        return self._tax_price

    @tax_price.setter
    def tax_price(self, tax_price):


        self._tax_price = tax_price

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
        if issubclass(OrderNotification, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, OrderNotification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

