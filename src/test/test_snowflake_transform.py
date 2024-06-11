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

from notehub_py.models.snowflake_transform import SnowflakeTransform

class TestSnowflakeTransform(unittest.TestCase):
    """SnowflakeTransform unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SnowflakeTransform:
        """Test SnowflakeTransform
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SnowflakeTransform`
        """
        model = SnowflakeTransform()
        if include_optional:
            return SnowflakeTransform(
                format = 'jsonata',
                jsonata = ''
            )
        else:
            return SnowflakeTransform(
        )
        """

    def testSnowflakeTransform(self):
        """Test SnowflakeTransform"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
