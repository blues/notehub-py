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

from notehub_py.models.get_project_device_public_keys200_response_device_public_keys_inner import (
    GetProjectDevicePublicKeys200ResponseDevicePublicKeysInner,
)


class TestGetProjectDevicePublicKeys200ResponseDevicePublicKeysInner(unittest.TestCase):
    """GetProjectDevicePublicKeys200ResponseDevicePublicKeysInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(
        self, include_optional
    ) -> GetProjectDevicePublicKeys200ResponseDevicePublicKeysInner:
        """Test GetProjectDevicePublicKeys200ResponseDevicePublicKeysInner
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetProjectDevicePublicKeys200ResponseDevicePublicKeysInner`
        """
        model = GetProjectDevicePublicKeys200ResponseDevicePublicKeysInner()
        if include_optional:
            return GetProjectDevicePublicKeys200ResponseDevicePublicKeysInner(
                uid = '',
                key = ''
            )
        else:
            return GetProjectDevicePublicKeys200ResponseDevicePublicKeysInner(
        )
        """

    def testGetProjectDevicePublicKeys200ResponseDevicePublicKeysInner(self):
        """Test GetProjectDevicePublicKeys200ResponseDevicePublicKeysInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
