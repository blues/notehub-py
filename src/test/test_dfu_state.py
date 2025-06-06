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

from notehub_py.models.dfu_state import DFUState


class TestDFUState(unittest.TestCase):
    """DFUState unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DFUState:
        """Test DFUState
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `DFUState`
        """
        model = DFUState()
        if include_optional:
            return DFUState(
                type = 'card',
                file = '',
                length = 1.337,
                crc32 = 1.337,
                md5 = '',
                mode = 'idle',
                status = '',
                began = 1.337,
                retry = 1.337,
                errors = 1.337,
                read = 1.337,
                updated = 1.337,
                version = ''
            )
        else:
            return DFUState(
        )
        """

    def testDFUState(self):
        """Test DFUState"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
