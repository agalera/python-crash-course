#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import urllib
import datetime
import logging
from collections import namedtuple

# third party libs
# import requests


# globals capital letters, usually on top of the file. Avoid using them. Better approach always a configuration file or in this case, as a class attribute
WEATHER_API_URL = "https://www.metaweather.com/api/"


# About DOCSTRINGS formats
# https://stackoverflow.com/QUESTIONS/3898572/what-is-the-standard-python-docstring-format

# PEP 257. Docstring conventions
# https://www.python.org/dev/peps/pep-0256/

# reST is recommended by the PEP 287 and is used by Sphinx
# PEP 287: https://www.python.org/dev/peps/pep-0287/#specification
def celsius_to_fahrenheit(temperature):
    """
    Change temperature from C to F.

    T(°C) = (T(°F) - 32) / 1.8

    :param temperature: in Celsius
    :type temperature: int
    :return: temperature in Fahrenheit
    :rtype: int
    :raises: TypeError
    """
    # Reduce the amount of code susceptible to raise exceptions.
    # You shouldn't be throwing exceptions, but maybe logging them
    # https://docs.python.org/2/library/exceptions.html
    try:
        temperature = int(temperature)
    except Exception as e:
        raise e
    return (temperature * 1.8) + 32



# Google Style is widely used as well
def fahrenheit_to_celsius(temperature):
    """
    Change temperature from C to F.

    Args:
        temperature: temp. in F.

    Returns:
        temperature: temp. in C
    Raises:
        TypeError: uncomputable temperature
    """
    try:
        return (temperature - 32) / 1.8
    except:
        raise TypeError("uncomputable temperature")


# named tuples have an instance method namedtuple._make
# Constructors, lambda use, Magic method
class Temperature(object):

    def __init__(self, temp, notation="C"):
        self.notation = notation
        self.to_fahrenheit = lambda t: (t * 1.8) + 32 # instance has control
        self.to_celsius = lambda t: (t * 1.8) + 32

        if notation == "C":
            self.celsius = temp
            self.fahrenheit = (lambda t: (t * 1.8) + 32)(temp)

        elif notation == "F":
            self.fahrenheit = temp
            self.celsius = (temp - 32) / 1.8 # self.to_celsius(temp)
        else:
            raise TypeError("Wrong notation format: C or F are allowed")

    def __add__(self, b):
        return self.celsius + b.celsius

    # doesn't access to class or instance attrs is like a func that belongs to a context
    @staticmethod
    def to_fahrenheit(temp):
        return (temp * 1.8) + 32

    @staticmethod
    def to_celsius(temp):
        # Take not of division: future concept. future division!
        return (temp - 32) / 1.8


class WeatherReport(object):
    #https://www.metaweather.com/api/location/44418/
    base_url = "https://www.metaweather.com/api/"

    def __init__(self, time_lapse, city=None):
        self.time_lapse = time_lapse
        self.city = city

    def __new__(self):
        pass

    def __str__(self):
        pass

    def __repr__(self):
        pass

    @classmethod
    def for_city(cls, city):
        return cls._make_city_report(city)

    @property
    def average(self):
        pass

    @property
    def top(self):
        pass

    @property
    def bottom(self):
        pass



def main(*args, **kwargs):
    """Main entry point for WeatherMan

    :param city: city name
    :type city: str
    :param date: date or daterange
    :type date: str
    """
    pass


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit()

    main(sys.argv)
