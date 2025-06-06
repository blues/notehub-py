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

from notehub_py.models.get_alerts200_response import GetAlerts200Response


class TestGetAlerts200Response(unittest.TestCase):
    """GetAlerts200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetAlerts200Response:
        """Test GetAlerts200Response
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `GetAlerts200Response`
        """
        model = GetAlerts200Response()
        if include_optional:
            return GetAlerts200Response(
                alerts = [
                    notehub_py.models.alert.Alert(
                        uid = '', 
                        monitor_uid = '', 
                        monitor_name = '', 
                        device_uid = '', 
                        created_at = 56, 
                        value = 1.337, 
                        resolved = True, 
                        version = 56, 
                        alert_source = 'app', 
                        source = '', 
                        monitor_type = 'event', 
                        field_name = '', 
                        data = [
                            notehub_py.models.alert_data_inner.Alert_data_inner(
                                alert_source = 'app', 
                                source = '', 
                                source_type = 'event', 
                                value = 1.337, 
                                source_uid = '', 
                                when = '', )
                            ], 
                        notifications = [
                            notehub_py.models.alert_notifications_inner.Alert_notifications_inner(
                                notification_type = 'email', 
                                status = 1.337, 
                                recipients = '', )
                            ], )
                    ],
                has_more = True
            )
        else:
            return GetAlerts200Response(
                alerts = [
                    notehub_py.models.alert.Alert(
                        uid = '', 
                        monitor_uid = '', 
                        monitor_name = '', 
                        device_uid = '', 
                        created_at = 56, 
                        value = 1.337, 
                        resolved = True, 
                        version = 56, 
                        alert_source = 'app', 
                        source = '', 
                        monitor_type = 'event', 
                        field_name = '', 
                        data = [
                            notehub_py.models.alert_data_inner.Alert_data_inner(
                                alert_source = 'app', 
                                source = '', 
                                source_type = 'event', 
                                value = 1.337, 
                                source_uid = '', 
                                when = '', )
                            ], 
                        notifications = [
                            notehub_py.models.alert_notifications_inner.Alert_notifications_inner(
                                notification_type = 'email', 
                                status = 1.337, 
                                recipients = '', )
                            ], )
                    ],
                has_more = True,
        )
        """

    def testGetAlerts200Response(self):
        """Test GetAlerts200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
