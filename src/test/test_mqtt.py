# coding: utf-8

"""
    Notehub API

    The OpenAPI definition for the Notehub.io API. 

    The version of the OpenAPI document: 1.0.0
    Contact: engineering@blues.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from notehub_py.models.mqtt import Mqtt

class TestMqtt(unittest.TestCase):
    """Mqtt unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Mqtt:
        """Test Mqtt
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Mqtt`
        """
        model = Mqtt()
        if include_optional:
            return Mqtt(
                fleets = [
                    ''
                    ],
                filter = notehub_py.models.http_filter.http_filter(
                    type = 'all', 
                    system_notefiles = True, 
                    files = [
                        ''
                        ], ),
                transform = notehub_py.models.http_transform.http_transform(
                    format = '', 
                    jsonata = '', ),
                throttle_ms = 56,
                timeout = 56,
                broker = '',
                port = 56,
                username = '',
                password = '',
                topic = '',
                certificate = '-----BEGIN CERTIFICATE-----\nMIIBpTCCA...JgVLttUY=\n-----END CERTIFICATE-----',
                certificate_name = '',
                key = '-----BEGIN PRIVATE KEY-----\nMIIEvwIBA...SleBlvA==\n-----END PRIVATE KEY-----',
                private_key_name = ''
            )
        else:
            return Mqtt(
        )
        """

    def testMqtt(self):
        """Test Mqtt"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
