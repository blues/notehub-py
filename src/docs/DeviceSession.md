# DeviceSession

## Properties

| Name                   | Type                                  | Description                                                                         | Notes      |
| ---------------------- | ------------------------------------- | ----------------------------------------------------------------------------------- | ---------- |
| **apn**                | **str**                               |                                                                                     | [optional] |
| **bars**               | **int**                               |                                                                                     | [optional] |
| **bearer**             | **str**                               |                                                                                     | [optional] |
| **bssid**              | **str**                               |                                                                                     | [optional] |
| **cell**               | **str**                               | Cell ID where the session originated and quality (\&quot;mcc,mnc,lac,cellid\&quot;) | [optional] |
| **continuous**         | **bool**                              | Was this a continuous connection?                                                   | [optional] |
| **device**             | **str**                               | Device UID                                                                          | [optional] |
| **events**             | **int**                               | Number of events routed                                                             | [optional] |
| **failed_connects**    | **int**                               | Number of failed connection attempts in the prior session                           | [optional] |
| **fleets**             | **List[str]**                         | Array of Fleet UIDs                                                                 | [optional] |
| **hp_cycles_data**     | **int**                               |                                                                                     | [optional] |
| **hp_cycles_gps**      | **int**                               |                                                                                     | [optional] |
| **hp_cycles_total**    | **int**                               |                                                                                     | [optional] |
| **hp_secs_data**       | **int**                               |                                                                                     | [optional] |
| **hp_secs_gps**        | **int**                               |                                                                                     | [optional] |
| **hp_secs_total**      | **int**                               | Total number of seconds in high power mode                                          | [optional] |
| **iccid**              | **str**                               |                                                                                     | [optional] |
| **ip**                 | **str**                               |                                                                                     | [optional] |
| **moved**              | **int**                               |                                                                                     | [optional] |
| **orientation**        | **str**                               |                                                                                     | [optional] |
| **penalty_secs**       | **int**                               | Number of seconds in penalty in the prior session                                   | [optional] |
| **period**             | [**DeviceUsage**](DeviceUsage.md)     |                                                                                     | [optional] |
| **power_charging**     | **bool**                              |                                                                                     | [optional] |
| **power_mah**          | **float**                             |                                                                                     | [optional] |
| **power_primary**      | **bool**                              |                                                                                     | [optional] |
| **power_usb**          | **bool**                              |                                                                                     | [optional] |
| **product**            | **str**                               | Product UID                                                                         | [optional] |
| **rat**                | **str**                               |                                                                                     | [optional] |
| **rsrp**               | **int**                               |                                                                                     | [optional] |
| **rsrq**               | **int**                               |                                                                                     | [optional] |
| **rssi**               | **int**                               |                                                                                     | [optional] |
| **scan**               | **bytearray**                         |                                                                                     | [optional] |
| **session**            | **str**                               | Session UID                                                                         | [optional] |
| **session_began**      | **int**                               | UNIX timestamp of session start                                                     | [optional] |
| **session_ended**      | **int**                               | UNIX timestamp of session end                                                       | [optional] |
| **sinr**               | **int**                               |                                                                                     | [optional] |
| **sn**                 | **str**                               | Device Serial Number                                                                | [optional] |
| **ssid**               | **str**                               |                                                                                     | [optional] |
| **temp**               | **float**                             |                                                                                     | [optional] |
| **tls**                | **bool**                              | Was TLS used?                                                                       | [optional] |
| **tower**              | [**TowerLocation**](TowerLocation.md) |                                                                                     | [optional] |
| **transport**          | **str**                               | Type of network transport                                                           | [optional] |
| **tri**                | [**TowerLocation**](TowerLocation.md) |                                                                                     | [optional] |
| **triangulate**        | **object**                            |                                                                                     | [optional] |
| **usage_actual**       | **bool**                              |                                                                                     | [optional] |
| **voltage**            | **float**                             |                                                                                     | [optional] |
| **when**               | **int**                               | Last known capture time of a note routed through this session in Unix timestamp     | [optional] |
| **where**              | **str**                               | Open Location Code from last GPS location                                           | [optional] |
| **where_country**      | **str**                               |                                                                                     | [optional] |
| **where_lat**          | **float**                             |                                                                                     | [optional] |
| **where_location**     | **str**                               |                                                                                     | [optional] |
| **where_lon**          | **float**                             |                                                                                     | [optional] |
| **where_timezone**     | **str**                               |                                                                                     | [optional] |
| **where_when**         | **int**                               | Unix timestamp of last GPS location                                                 | [optional] |
| **why_session_closed** | **str**                               | Reason for session closing                                                          | [optional] |
| **why_session_opened** | **str**                               | Reason for session opening                                                          | [optional] |
| **work**               | **int**                               | Unix timestamp of the last time work was done for this session                      | [optional] |

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
