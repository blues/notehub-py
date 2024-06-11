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

from notehub_py.models.get_device_sessions200_response import GetDeviceSessions200Response

class TestGetDeviceSessions200Response(unittest.TestCase):
    """GetDeviceSessions200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetDeviceSessions200Response:
        """Test GetDeviceSessions200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetDeviceSessions200Response`
        """
        model = GetDeviceSessions200Response()
        if include_optional:
            return GetDeviceSessions200Response(
                sessions = [
                    notehub_py.models.device_session.DeviceSession(
                        session = '', 
                        device = '', 
                        sn = '', 
                        product = '', 
                        fleets = [
                            ''
                            ], 
                        cell = '', 
                        scan = 'YQ==', 
                        triangulate = notehub_py.models.triangulate.triangulate(), 
                        rssi = 1.337, 
                        sinr = 1.337, 
                        rsrp = 1.337, 
                        rsrq = 1.337, 
                        bars = 1.337, 
                        rat = '', 
                        bearer = '', 
                        ip = '', 
                        bssid = '', 
                        ssid = '', 
                        iccid = '', 
                        apn = '', 
                        tower = notehub_py.models.tower_location.TowerLocation(
                            time = 1.337, 
                            n = '', 
                            c = '', 
                            lat = 1.337, 
                            lon = 1.337, 
                            zone = '', 
                            mcc = 1.337, 
                            mnc = 1.337, 
                            lac = 1.337, 
                            cid = 1.337, 
                            l = '', 
                            z = 1.337, 
                            count = 1.337, 
                            towers = 1.337, ), 
                        tri = notehub_py.models.tower_location.TowerLocation(
                            time = 1.337, 
                            n = '', 
                            c = '', 
                            lat = 1.337, 
                            lon = 1.337, 
                            zone = '', 
                            mcc = 1.337, 
                            mnc = 1.337, 
                            lac = 1.337, 
                            cid = 1.337, 
                            l = '', 
                            z = 1.337, 
                            count = 1.337, 
                            towers = 1.337, ), 
                        when = 1.337, 
                        where_when = 1.337, 
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
                        work = 1.337, 
                        events = 1.337, 
                        moved = 1.337, 
                        orientation = '', 
                        hp_secs_total = 1.337, 
                        hp_secs_data = 1.337, 
                        hp_secs_gps = 1.337, 
                        hp_cycles_total = 1.337, 
                        hp_cycles_data = 1.337, 
                        hp_cycles_gps = 1.337, 
                        period = notehub_py.models.device_usage.DeviceUsage(
                            since = 1.337, 
                            duration = 1.337, 
                            bytes_rcvd = 1.337, 
                            bytes_sent = 1.337, 
                            bytes_rcvd_secondary = 1.337, 
                            bytes_sent_secondary = 1.337, 
                            sessions_tcp = 1.337, 
                            sessions_tls = 1.337, 
                            notes_rcvd = 1.337, 
                            note_sent = 1.337, ), )
                    ],
                has_more = True
            )
        else:
            return GetDeviceSessions200Response(
                sessions = [
                    notehub_py.models.device_session.DeviceSession(
                        session = '', 
                        device = '', 
                        sn = '', 
                        product = '', 
                        fleets = [
                            ''
                            ], 
                        cell = '', 
                        scan = 'YQ==', 
                        triangulate = notehub_py.models.triangulate.triangulate(), 
                        rssi = 1.337, 
                        sinr = 1.337, 
                        rsrp = 1.337, 
                        rsrq = 1.337, 
                        bars = 1.337, 
                        rat = '', 
                        bearer = '', 
                        ip = '', 
                        bssid = '', 
                        ssid = '', 
                        iccid = '', 
                        apn = '', 
                        tower = notehub_py.models.tower_location.TowerLocation(
                            time = 1.337, 
                            n = '', 
                            c = '', 
                            lat = 1.337, 
                            lon = 1.337, 
                            zone = '', 
                            mcc = 1.337, 
                            mnc = 1.337, 
                            lac = 1.337, 
                            cid = 1.337, 
                            l = '', 
                            z = 1.337, 
                            count = 1.337, 
                            towers = 1.337, ), 
                        tri = notehub_py.models.tower_location.TowerLocation(
                            time = 1.337, 
                            n = '', 
                            c = '', 
                            lat = 1.337, 
                            lon = 1.337, 
                            zone = '', 
                            mcc = 1.337, 
                            mnc = 1.337, 
                            lac = 1.337, 
                            cid = 1.337, 
                            l = '', 
                            z = 1.337, 
                            count = 1.337, 
                            towers = 1.337, ), 
                        when = 1.337, 
                        where_when = 1.337, 
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
                        work = 1.337, 
                        events = 1.337, 
                        moved = 1.337, 
                        orientation = '', 
                        hp_secs_total = 1.337, 
                        hp_secs_data = 1.337, 
                        hp_secs_gps = 1.337, 
                        hp_cycles_total = 1.337, 
                        hp_cycles_data = 1.337, 
                        hp_cycles_gps = 1.337, 
                        period = notehub_py.models.device_usage.DeviceUsage(
                            since = 1.337, 
                            duration = 1.337, 
                            bytes_rcvd = 1.337, 
                            bytes_sent = 1.337, 
                            bytes_rcvd_secondary = 1.337, 
                            bytes_sent_secondary = 1.337, 
                            sessions_tcp = 1.337, 
                            sessions_tls = 1.337, 
                            notes_rcvd = 1.337, 
                            note_sent = 1.337, ), )
                    ],
                has_more = True,
        )
        """

    def testGetDeviceSessions200Response(self):
        """Test GetDeviceSessions200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
