# coding: utf-8

"""
    Notehub API

    The OpenAPI definition for the Notehub.io API. 

    The version of the OpenAPI document: 1.1.0
    Contact: engineering@blues.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from notehub_py.models.radresponder import Radresponder

class TestRadresponder(unittest.TestCase):
    """Radresponder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Radresponder:
        """Test Radresponder
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Radresponder`
        """
        model = Radresponder()
        if include_optional:
            return Radresponder(
                fleets = [
                    ''
                    ],
                test_api = True,
                data_feed_key = '',
                client_id = '',
                client_secret = ''
            )
        else:
            return Radresponder(
        )
        """

    def testRadresponder(self):
        """Test Radresponder"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
