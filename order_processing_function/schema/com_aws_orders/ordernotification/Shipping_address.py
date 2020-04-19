# coding: utf-8
import pprint
import re  # noqa: F401

import six
from enum import Enum

class Shipping_address(object):


    _types = {
        'city': 'str',
        'country': 'str',
        'state': 'str',
        'street': 'str',
        'zip_code': 'str'
    }

    _attribute_map = {
        'city': 'city',
        'country': 'country',
        'state': 'state',
        'street': 'street',
        'zip_code': 'zip_code'
    }

    def __init__(self, city=None, country=None, state=None, street=None, zip_code=None):  # noqa: E501
        self._city = None
        self._country = None
        self._state = None
        self._street = None
        self._zip_code = None
        self.discriminator = None
        self.city = city
        self.country = country
        self.state = state
        self.street = street
        self.zip_code = zip_code


    @property
    def city(self):

        return self._city

    @city.setter
    def city(self, city):


        self._city = city


    @property
    def country(self):

        return self._country

    @country.setter
    def country(self, country):


        self._country = country


    @property
    def state(self):

        return self._state

    @state.setter
    def state(self, state):


        self._state = state


    @property
    def street(self):

        return self._street

    @street.setter
    def street(self, street):


        self._street = street


    @property
    def zip_code(self):

        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):


        self._zip_code = zip_code

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
        if issubclass(Shipping_address, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Shipping_address):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other

