# Sportradar APIs
# Copyright 2018 John W. Miller
# See LICENSE for details.

"""
API details and documentation: https://developer.sportradar.com/io-docs
"""

import requests
import time


class API(object):
    """Sportradar API"""

    # Create a persistent requests connection
    session = requests.Session()
    session.headers = {'application': 'PythonWrapper'}

    default_version = 7

    def __init__(self, api_key, format_='json', timeout=5, version=default_version, sleep_time=1.5, debug=False):
        """ Sportradar API Constructor

        :param api_key: key provided by Sportradar, specific to the sport's API
        :param format_: response format to request from the API (json, xml)
        :param language: language of the response data
        :param version: version of the api
        :param timeout: time before quitting on response (seconds)
        :param sleep_time: time to wait between requests, (free min is 1 second)
        """

        assert api_key != '', 'Must supply a non-empty API key.'
        self.api_key = {'api_key': api_key}
        self.api_root = 'http://api.sportradar.us/'
        self.FORMAT = "." + format_.strip(".")
        self.timeout = timeout
        self.version = version
        self.debug = debug
        self._sleep_time = sleep_time

    def _make_request(self, path, method='GET'):
        """Make a GET or POST request to the API"""
        time.sleep(self._sleep_time)  # Rate limiting
        full_uri = self.api_root + path + self.FORMAT
        if self.debug:
            print(path)
            print(full_uri)
        response = self.session.request(method,
                                        full_uri,
                                        timeout=self.timeout,
                                        params=self.api_key)
        # response.raise_for_status()  # Raise error for bad status
        return response

    def set_version(self, version):
        self.version = version
