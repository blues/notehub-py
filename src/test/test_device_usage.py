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

from notehub_py.models.device_usage import DeviceUsage


class TestDeviceUsage(unittest.TestCase):
    """DeviceUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceUsage:
        """Test DeviceUsage
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `DeviceUsage`
        """
        model = DeviceUsage()
        if include_optional:
            return DeviceUsage(
                since = 56,
                duration = 56,
                bytes_rcvd = 56,
                bytes_sent = 56,
                bytes_rcvd_secondary = 56,
                bytes_sent_secondary = 56,
                sessions_tcp = 56,
                sessions_tls = 56,
                notes_rcvd = 56,
                notes_sent = 56
            )
        else:
            return DeviceUsage(
        )
        """

    def testDeviceUsage(self):
        """Test DeviceUsage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
