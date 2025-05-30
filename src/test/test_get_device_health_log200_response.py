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

from notehub_py.models.get_device_health_log200_response import (
    GetDeviceHealthLog200Response,
)


class TestGetDeviceHealthLog200Response(unittest.TestCase):
    """GetDeviceHealthLog200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDeviceHealthLog200Response:
        """Test GetDeviceHealthLog200Response
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetDeviceHealthLog200Response`
        """
        model = GetDeviceHealthLog200Response()
        if include_optional:
            return GetDeviceHealthLog200Response(
                health_log = [
                    notehub_py.models.get_device_health_log_200_response_health_log_inner.getDeviceHealthLog_200_response_health_log_inner(
                        when = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        alert = True, 
                        text = '', )
                    ]
            )
        else:
            return GetDeviceHealthLog200Response(
                health_log = [
                    notehub_py.models.get_device_health_log_200_response_health_log_inner.getDeviceHealthLog_200_response_health_log_inner(
                        when = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        alert = True, 
                        text = '', )
                    ],
        )
        """

    def testGetDeviceHealthLog200Response(self):
        """Test GetDeviceHealthLog200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
