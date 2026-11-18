# Device

A device in a project. `best_location` is the best of `gps_location`, `triangulated_location` and `tower_location`; each is null when unknown.

## Properties

| Name                       | Type                                      | Description                                                                                                                       | Notes      |
| -------------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **best_id**                | **str**                                   | The serial number if set, otherwise the DeviceUID. Use it as a display name.                                                      | [optional] |
| **best_location**          | [**Location**](Location.md)               |                                                                                                                                   | [optional] |
| **cellular_usage**         | [**List[SimUsage]**](SimUsage.md)         |                                                                                                                                   | [optional] |
| **contact**                | [**Contact**](Contact.md)                 |                                                                                                                                   | [optional] |
| **deleted**                | **bool**                                  | True if this device has been deleted. Only present when reading with a &#x60;cursor&#x60;.                                        | [optional] |
| **dfu**                    | [**DFUEnv**](DFUEnv.md)                   |                                                                                                                                   | [optional] |
| **disabled**               | **bool**                                  | True if the device was disabled with &#x60;DisableDevice&#x60; and can&#39;t connect.                                             | [optional] |
| **firmware_host**          | **str**                                   | Host firmware version, as reported by the device. Usually a JSON string.                                                          | [optional] |
| **firmware_notecard**      | **str**                                   | Notecard firmware version, as reported by the device.                                                                             | [optional] |
| **fleet_uids**             | **List[str]**                             | FleetUIDs of the fleets the device is in.                                                                                         |
| **gps_location**           | [**Location**](Location.md)               |                                                                                                                                   | [optional] |
| **health_log**             | [**List[HealthLog]**](HealthLog.md)       | Not returned by &#x60;GetDevice&#x60;, &#x60;GetDevices&#x60; or &#x60;GetFleetDevices&#x60;; use &#x60;GetDeviceHealthLog&#x60;. | [optional] |
| **last_activity**          | **datetime**                              | When the device was last active in a session. Null if it has never connected.                                                     | [optional] |
| **product_uid**            | **str**                                   | ProductUID the device uses, e.g. &#x60;com.blues.bridge:sensors&#x60;.                                                            |
| **provisioned**            | **datetime**                              | When the device was added to the project.                                                                                         |
| **recent_event_count**     | **List[int]**                             | Not returned by &#x60;GetDevice&#x60;, &#x60;GetDevices&#x60; or &#x60;GetFleetDevices&#x60;.                                     | [optional] |
| **recent_session_count**   | **List[int]**                             | Not returned by &#x60;GetDevice&#x60;, &#x60;GetDevices&#x60; or &#x60;GetFleetDevices&#x60;.                                     | [optional] |
| **recent_session_seconds** | **List[int]**                             | Not returned by &#x60;GetDevice&#x60;, &#x60;GetDevices&#x60; or &#x60;GetFleetDevices&#x60;.                                     | [optional] |
| **recent_when**            | **datetime**                              | Not returned by &#x60;GetDevice&#x60;, &#x60;GetDevices&#x60; or &#x60;GetFleetDevices&#x60;.                                     | [optional] |
| **sensors**                | [**List[DeviceSensor]**](DeviceSensor.md) |                                                                                                                                   | [optional] |
| **serial_number**          | **str**                                   | Serial number, from the &#x60;\_sn&#x60; environment variable if set. Empty if none.                                              | [optional] |
| **sku**                    | **str**                                   | Notecard SKU, e.g. &#x60;NOTE-WBNAW&#x60;.                                                                                        | [optional] |
| **tags**                   | **str**                                   | Comma-separated tags, from the &#x60;\_tags&#x60; environment variable. Empty if none.                                            | [optional] |
| **temperature**            | **float**                                 | Last reported Notecard temperature, in degrees Celsius.                                                                           |
| **tower_info**             | [**DeviceTowerInfo**](DeviceTowerInfo.md) |                                                                                                                                   | [optional] |
| **tower_location**         | [**Location**](Location.md)               |                                                                                                                                   | [optional] |
| **triangulated_location**  | [**Location**](Location.md)               |                                                                                                                                   | [optional] |
| **uid**                    | **str**                                   | DeviceUID, e.g. &#x60;dev:864475040509284&#x60;.                                                                                  |
| **voltage**                | **float**                                 | Last reported supply voltage, in volts.                                                                                           |

## Example

```python
from notehub_py.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print(Device.to_json())

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_from_dict = Device.from_dict(device_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
