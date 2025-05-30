# coding: utf-8

"""
Notehub API

The OpenAPI definition for the Notehub.io API.

The version of the OpenAPI document: 1.2.0
Contact: engineering@blues.io
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501


import unittest

from notehub_py.models.get_device_public_key200_response import (
    GetDevicePublicKey200Response,
)


class TestGetDevicePublicKey200Response(unittest.TestCase):
    """GetDevicePublicKey200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDevicePublicKey200Response:
        """Test GetDevicePublicKey200Response
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetDevicePublicKey200Response`
        """
        model = GetDevicePublicKey200Response()
        if include_optional:
            return GetDevicePublicKey200Response(
                uid = '',
                key = ''
            )
        else:
            return GetDevicePublicKey200Response(
                uid = '',
                key = '',
        )
        """

    def testGetDevicePublicKey200Response(self):
        """Test GetDevicePublicKey200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
