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

from notehub_py.models.create_fleet_request import CreateFleetRequest

class TestCreateFleetRequest(unittest.TestCase):
    """CreateFleetRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateFleetRequest:
        """Test CreateFleetRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateFleetRequest`
        """
        model = CreateFleetRequest()
        if include_optional:
            return CreateFleetRequest(
                label = ''
            )
        else:
            return CreateFleetRequest(
        )
        """

    def testCreateFleetRequest(self):
        """Test CreateFleetRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
