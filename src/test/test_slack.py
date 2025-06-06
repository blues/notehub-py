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

from notehub_py.models.slack import Slack


class TestSlack(unittest.TestCase):
    """Slack unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Slack:
        """Test Slack
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `Slack`
        """
        model = Slack()
        if include_optional:
            return Slack(
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
                throttle_ms = 56,
                timeout = 56,
                slack_type = '',
                bearer = 'xoxb-1234-56789abcdefghijklmnop',
                channel = 'C8675309',
                webhook_url = 'https://hooks.slack.com/services/FOO4BAR/THIS4THAT/123xYzaBC456',
                text = '[.device] reported temp(s) of [.body.temp] at [.body.location]',
                blocks = ''
            )
        else:
            return Slack(
        )
        """

    def testSlack(self):
        """Test Slack"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
