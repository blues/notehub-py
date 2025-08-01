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

from notehub_py.models.device_session import DeviceSession


class TestDeviceSession(unittest.TestCase):
    """DeviceSession unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeviceSession:
        """Test DeviceSession
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `DeviceSession`
        """
        model = DeviceSession()
        if include_optional:
            return DeviceSession(
                session = '',
                session_began = 56,
                why_session_opened = '',
                session_ended = 56,
                why_session_closed = '',
                device = '',
                sn = '',
                product = '',
                fleets = [
                    ''
                    ],
                cell = '',
                scan = 'YQ==',
                triangulate = None,
                rssi = 56,
                sinr = 56,
                rsrp = 56,
                rsrq = 56,
                bars = 56,
                rat = '',
                bearer = '',
                ip = '',
                bssid = '',
                ssid = '',
                iccid = '',
                apn = '',
                transport = '',
                tower = notehub_py.models.tower_location.TowerLocation(
                    source = '', 
                    time = 56, 
                    n = '', 
                    c = '', 
                    lat = 1.337, 
                    lon = 1.337, 
                    zone = '', 
                    mcc = 56, 
                    mnc = 56, 
                    lac = 56, 
                    cid = 56, 
                    l = '', 
                    z = 56, 
                    towers = 56, ),
                tri = notehub_py.models.tower_location.TowerLocation(
                    source = '', 
                    time = 56, 
                    n = '', 
                    c = '', 
                    lat = 1.337, 
                    lon = 1.337, 
                    zone = '', 
                    mcc = 56, 
                    mnc = 56, 
                    lac = 56, 
                    cid = 56, 
                    l = '', 
                    z = 56, 
                    towers = 56, ),
                when = 56,
                where_when = 56,
                where = '',
                where_lat = 1.337,
                where_lon = 1.337,
                where_location = '',
                where_country = '',
                where_timezone = '',
                usage_actual = True,
                voltage = 1.337,
                temp = 1.337,
                continuous = True,
                tls = True,
                work = 56,
                events = 56,
                moved = 56,
                orientation = '',
                hp_secs_total = 56,
                hp_secs_data = 56,
                hp_secs_gps = 56,
                hp_cycles_total = 56,
                hp_cycles_data = 56,
                hp_cycles_gps = 56,
                period = notehub_py.models.device_usage.DeviceUsage(
                    since = 56, 
                    duration = 56, 
                    bytes_rcvd = 56, 
                    bytes_sent = 56, 
                    bytes_rcvd_secondary = 56, 
                    bytes_sent_secondary = 56, 
                    sessions_tcp = 56, 
                    sessions_tls = 56, 
                    notes_rcvd = 56, 
                    notes_sent = 56, ),
                power_charging = True,
                power_usb = True,
                power_primary = True,
                power_mah = 1.337,
                penalty_secs = 56,
                failed_connects = 56
            )
        else:
            return DeviceSession(
        )
        """

    def testDeviceSession(self):
        """Test DeviceSession"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()
