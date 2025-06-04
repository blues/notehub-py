# DeviceSession

## Properties

| Name                   | Type                                  | Description                                                                         | Notes      |
| ---------------------- | ------------------------------------- | ----------------------------------------------------------------------------------- | ---------- |
| **session**            | **str**                               | Session UID                                                                         | [optional] |
| **session_began**      | **int**                               | UNIX timestamp of session start                                                     | [optional] |
| **why_session_opened** | **str**                               | Reason for session opening                                                          | [optional] |
| **session_ended**      | **int**                               | UNIX timestamp of session end                                                       | [optional] |
| **why_session_closed** | **str**                               | Reason for session closing                                                          | [optional] |
| **device**             | **str**                               | Device UID                                                                          | [optional] |
| **sn**                 | **str**                               | Device Serial Number                                                                | [optional] |
| **product**            | **str**                               | Product UID                                                                         | [optional] |
| **fleets**             | **List[str]**                         | Array of Fleet UIDs                                                                 | [optional] |
| **cell**               | **str**                               | Cell ID where the session originated and quality (\&quot;mcc,mnc,lac,cellid\&quot;) | [optional] |
| **scan**               | **bytearray**                         |                                                                                     | [optional] |
| **triangulate**        | **object**                            |                                                                                     | [optional] |
| **rssi**               | **int**                               |                                                                                     | [optional] |
| **sinr**               | **int**                               |                                                                                     | [optional] |
| **rsrp**               | **int**                               |                                                                                     | [optional] |
| **rsrq**               | **int**                               |                                                                                     | [optional] |
| **bars**               | **int**                               |                                                                                     | [optional] |
| **rat**                | **str**                               |                                                                                     | [optional] |
| **bearer**             | **str**                               |                                                                                     | [optional] |
| **ip**                 | **str**                               |                                                                                     | [optional] |
| **bssid**              | **str**                               |                                                                                     | [optional] |
| **ssid**               | **str**                               |                                                                                     | [optional] |
| **iccid**              | **str**                               |                                                                                     | [optional] |
| **apn**                | **str**                               |                                                                                     | [optional] |
| **transport**          | **str**                               | Type of network transport                                                           | [optional] |
| **tower**              | [**TowerLocation**](TowerLocation.md) |                                                                                     | [optional] |
| **tri**                | [**TowerLocation**](TowerLocation.md) |                                                                                     | [optional] |
| **when**               | **int**                               | Last known capture time of a note routed through this session in Unix timestamp     | [optional] |
| **where_when**         | **int**                               | Unix timestamp of last GPS location                                                 | [optional] |
| **where**              | **str**                               | Open Location Code from last GPS location                                           | [optional] |
| **where_lat**          | **float**                             |                                                                                     | [optional] |
| **where_lon**          | **float**                             |                                                                                     | [optional] |
| **where_location**     | **str**                               |                                                                                     | [optional] |
| **where_country**      | **str**                               |                                                                                     | [optional] |
| **where_timezone**     | **str**                               |                                                                                     | [optional] |
| **usage_actual**       | **bool**                              |                                                                                     | [optional] |
| **voltage**            | **float**                             |                                                                                     | [optional] |
| **temp**               | **float**                             |                                                                                     | [optional] |
| **continuous**         | **bool**                              | Was this a continuous connection?                                                   | [optional] |
| **tls**                | **bool**                              | Was TLS used?                                                                       | [optional] |
| **work**               | **int**                               | Unix timestamp of the last time work was done for this session                      | [optional] |
| **events**             | **int**                               | Number of events routed                                                             | [optional] |
| **moved**              | **int**                               |                                                                                     | [optional] |
| **orientation**        | **str**                               |                                                                                     | [optional] |
| **hp_secs_total**      | **int**                               | Total number of seconds in high power mode                                          | [optional] |
| **hp_secs_data**       | **int**                               |                                                                                     | [optional] |
| **hp_secs_gps**        | **int**                               |                                                                                     | [optional] |
| **hp_cycles_total**    | **int**                               |                                                                                     | [optional] |
| **hp_cycles_data**     | **int**                               |                                                                                     | [optional] |
| **hp_cycles_gps**      | **int**                               |                                                                                     | [optional] |
| **period**             | [**DeviceUsage**](DeviceUsage.md)     |                                                                                     | [optional] |
| **power_charging**     | **bool**                              |                                                                                     | [optional] |
| **power_usb**          | **bool**                              |                                                                                     | [optional] |
| **power_primary**      | **bool**                              |                                                                                     | [optional] |
| **power_mah**          | **float**                             |                                                                                     | [optional] |
| **penalty_secs**       | **int**                               | Number of seconds in penalty in the prior session                                   | [optional] |
| **failed_connects**    | **int**                               | Number of failed connection attempts in the prior session                           | [optional] |

## Example

```python
from notehub_py.models.device_session import DeviceSession

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSession from a JSON string
device_session_instance = DeviceSession.from_json(json)
# print the JSON string representation of the object
print(DeviceSession.to_json())

# convert the object into a dict
device_session_dict = device_session_instance.to_dict()
# create an instance of DeviceSession from a dict
device_session_from_dict = DeviceSession.from_dict(device_session_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
