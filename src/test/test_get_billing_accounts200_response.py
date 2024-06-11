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

from notehub_py.models.get_billing_accounts200_response import GetBillingAccounts200Response

class TestGetBillingAccounts200Response(unittest.TestCase):
    """GetBillingAccounts200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetBillingAccounts200Response:
        """Test GetBillingAccounts200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetBillingAccounts200Response`
        """
        model = GetBillingAccounts200Response()
        if include_optional:
            return GetBillingAccounts200Response(
                billing_accounts = [
                    notehub_py.models.billing_account.BillingAccount(
                        uid = '', 
                        name = '', 
                        role = 'billing_admin', )
                    ]
            )
        else:
            return GetBillingAccounts200Response(
        )
        """

    def testGetBillingAccounts200Response(self):
        """Test GetBillingAccounts200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
