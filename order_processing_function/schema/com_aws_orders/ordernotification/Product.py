# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class Product(object):


    _types = {
        'image_url': 'str',
        'inventory_id': 'int',
        'product_id': 'int',
        'size': 'str',
        'sku': 'str',
        'taxable': 'bool',
        'title': 'str',
        'weight': 'float',
        'weight_unit': 'str'
    }

    _attribute_map = {
        'image_url': 'image_url',
        'inventory_id': 'inventory_id',
        'product_id': 'product_id',
        'size': 'size',
        'sku': 'sku',
        'taxable': 'taxable',
        'title': 'title',
        'weight': 'weight',
        'weight_unit': 'weight_unit'
    }

    def __init__(self, image_url=None, inventory_id=None, product_id=None, size=None, sku=None, taxable=None, title=None, weight=None, weight_unit=None):  # noqa: E501
        self._image_url = None
        self._inventory_id = None
        self._product_id = None
        self._size = None
        self._sku = None
        self._taxable = None
        self._title = None
        self._weight = None
        self._weight_unit = None
        self.discriminator = None
        self.image_url = image_url
        self.inventory_id = inventory_id
        self.product_id = product_id
        self.size = size
        self.sku = sku
        self.taxable = taxable
        self.title = title
        self.weight = weight
        self.weight_unit = weight_unit


    @property
    def image_url(self):

        return self._image_url

    @image_url.setter
    def image_url(self, image_url):


        self._image_url = image_url


    @property
    def inventory_id(self):

        return self._inventory_id

    @inventory_id.setter
    def inventory_id(self, inventory_id):


        self._inventory_id = inventory_id


    @property
    def product_id(self):

        return self._product_id

    @product_id.setter
    def product_id(self, product_id):


        self._product_id = product_id


    @property
    def size(self):

        return self._size

    @size.setter
    def size(self, size):


        self._size = size


    @property
    def sku(self):

        return self._sku

    @sku.setter
    def sku(self, sku):


        self._sku = sku


    @property
    def taxable(self):

        return self._taxable

    @taxable.setter
    def taxable(self, taxable):


        self._taxable = taxable


    @property
    def title(self):

        return self._title

    @title.setter
    def title(self, title):


        self._title = title


    @property
    def weight(self):

        return self._weight

    @weight.setter
    def weight(self, weight):


        self._weight = weight


    @property
    def weight_unit(self):

        return self._weight_unit

    @weight_unit.setter
    def weight_unit(self, weight_unit):


        self._weight_unit = weight_unit

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
        if issubclass(Product, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

