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

from notehub_py.models.snowflake import Snowflake

class TestSnowflake(unittest.TestCase):
    """Snowflake unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Snowflake:
        """Test Snowflake
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Snowflake`
        """
        model = Snowflake()
        if include_optional:
            return Snowflake(
                fleets = [
                    ''
                    ],
                filter = notehub_py.models.http_filter.http_filter(
                    type = 'all', 
                    system_notefiles = True, 
                    files = [
                        ''
                        ], ),
                transform = notehub_py.models.snowflake_transform.snowflake_transform(
                    format = 'jsonata', 
                    jsonata = '', ),
                timeout = 56,
                organization_name = '',
                account_name = '',
                user_name = '',
                private_key_name = 'present',
                pem = '-----BEGIN PRIVATE KEY-----\nMIIEvwIBA...SleBlvA==\n-----END PRIVATE KEY-----'
            )
        else:
            return Snowflake(
        )
        """

    def testSnowflake(self):
        """Test Snowflake"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
