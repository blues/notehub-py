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

from notehub_py.models.http import Http

class TestHttp(unittest.TestCase):
    """Http unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Http:
        """Test Http
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Http`
        """
        model = Http()
        if include_optional:
            return Http(
                fleets = [
                    ''
                    ],
                filter = notehub_py.models.http_filter.http_filter(
                    type = 'all', 
                    system_notefiles = True, 
                    files = [
                        ''
                        ], ),
                transform = notehub_py.models.http_transform.http_transform(
                    format = '', 
                    jsonata = '', ),
                throttle_ms = 56,
                url = '',
                http_headers = {"headerName1":"headerValue1","headerName2":"headerValue2"},
                disable_http_headers = True,
                timeout = 56
            )
        else:
            return Http(
        )
        """

    def testHttp(self):
        """Test Http"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
