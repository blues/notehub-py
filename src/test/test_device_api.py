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

from notehub_py.api.device_api import DeviceApi


class TestDeviceApi(unittest.TestCase):
    """DeviceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DeviceApi()

    def tearDown(self) -> None:
        pass

    def test_delete_device_environment_variable(self) -> None:
        """Test case for delete_device_environment_variable

        """
        pass

    def test_delete_project_device(self) -> None:
        """Test case for delete_project_device

        """
        pass

    def test_disable_device(self) -> None:
        """Test case for disable_device

        """
        pass

    def test_disable_device_connectivity_assurance(self) -> None:
        """Test case for disable_device_connectivity_assurance

        """
        pass

    def test_enable_device(self) -> None:
        """Test case for enable_device

        """
        pass

    def test_enable_device_connectivity_assurance(self) -> None:
        """Test case for enable_device_connectivity_assurance

        """
        pass

    def test_get_device(self) -> None:
        """Test case for get_device

        """
        pass

    def test_get_device_environment_variables(self) -> None:
        """Test case for get_device_environment_variables

        """
        pass

    def test_get_device_environment_variables_by_pin(self) -> None:
        """Test case for get_device_environment_variables_by_pin

        """
        pass

    def test_get_device_health_log(self) -> None:
        """Test case for get_device_health_log

        """
        pass

    def test_get_device_latest(self) -> None:
        """Test case for get_device_latest

        """
        pass

    def test_get_device_public_key(self) -> None:
        """Test case for get_device_public_key

        """
        pass

    def test_get_device_sessions(self) -> None:
        """Test case for get_device_sessions

        """
        pass

    def test_get_project_device_public_keys(self) -> None:
        """Test case for get_project_device_public_keys

        """
        pass

    def test_get_project_devices(self) -> None:
        """Test case for get_project_devices

        """
        pass

    def test_get_project_fleet_devices(self) -> None:
        """Test case for get_project_fleet_devices

        """
        pass

    def test_handle_note_add(self) -> None:
        """Test case for handle_note_add

        """
        pass

    def test_handle_note_changes(self) -> None:
        """Test case for handle_note_changes

        """
        pass

    def test_handle_note_create_add(self) -> None:
        """Test case for handle_note_create_add

        """
        pass

    def test_handle_note_delete(self) -> None:
        """Test case for handle_note_delete

        """
        pass

    def test_handle_note_get(self) -> None:
        """Test case for handle_note_get

        """
        pass

    def test_handle_note_signal(self) -> None:
        """Test case for handle_note_signal

        """
        pass

    def test_handle_note_update(self) -> None:
        """Test case for handle_note_update

        """
        pass

    def test_handle_notefile_changes(self) -> None:
        """Test case for handle_notefile_changes

        """
        pass

    def test_handle_notefile_changes_pending(self) -> None:
        """Test case for handle_notefile_changes_pending

        """
        pass

    def test_handle_notefile_delete(self) -> None:
        """Test case for handle_notefile_delete

        """
        pass

    def test_post_provision_project_device(self) -> None:
        """Test case for post_provision_project_device

        """
        pass

    def test_put_device_environment_variables(self) -> None:
        """Test case for put_device_environment_variables

        """
        pass

    def test_put_device_environment_variables_by_pin(self) -> None:
        """Test case for put_device_environment_variables_by_pin

        """
        pass


if __name__ == '__main__':
    unittest.main()
