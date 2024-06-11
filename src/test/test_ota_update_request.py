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

from notehub_py.models.ota_update_request import OTAUpdateRequest

class TestOTAUpdateRequest(unittest.TestCase):
    """OTAUpdateRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OTAUpdateRequest:
        """Test OTAUpdateRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OTAUpdateRequest`
        """
        model = OTAUpdateRequest()
        if include_optional:
            return OTAUpdateRequest(
                filename = '',
                device_uids = [
                    ''
                    ],
                fleet_uids = [
                    ''
                    ],
                device_tags = [
                    ''
                    ],
                version = '',
                md5 = '',
                type = '',
                product = '',
                target = '',
                unpublished = True,
                cancel_dfu = True
            )
        else:
            return OTAUpdateRequest(
        )
        """

    def testOTAUpdateRequest(self):
        """Test OTAUpdateRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
