# Event

## Properties

| Name                   | Type       | Description                                                                                                                                            | Notes      |
| ---------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **app**                | **str**    | App UID (globally unique)                                                                                                                              | [optional] |
| **bars**               | **float**  | Bars. Only available on \_session.qo events.                                                                                                           | [optional] |
| **best_country**       | **str**    | Country                                                                                                                                                | [optional] |
| **best_id**            | **str**    | The device serial number, or the DeviceUID if the serial number is not set                                                                             | [optional] |
| **best_lat**           | **float**  | Latitude                                                                                                                                               | [optional] |
| **best_location**      | **str**    | Location                                                                                                                                               | [optional] |
| **best_location_type** | **str**    | One of \&quot;gps\&quot;, \&quot;triangulated\&quot;, or \&quot;tower\&quot;                                                                           | [optional] |
| **best_location_when** | **float**  | Unix timestamp                                                                                                                                         | [optional] |
| **best_lon**           | **float**  | Longitude                                                                                                                                              | [optional] |
| **best_timezone**      | **str**    | Timezone                                                                                                                                               | [optional] |
| **body**               | **object** | A JSON object containing event details                                                                                                                 | [optional] |
| **bssid**              | **str**    | BSSID. Only available on \_session.qo events.                                                                                                          | [optional] |
| **device**             | **str**    | Device UID (globally unique)                                                                                                                           | [optional] |
| **environment**        | **object** | Routed environment variables beginning with \&quot;$\&quot;. Only available on \_session.qo events.                                                    | [optional] |
| **event**              | **str**    | Event UID (globally unique)                                                                                                                            | [optional] |
| **file**               | **str**    | The notefile associated with this event                                                                                                                | [optional] |
| **moved**              | **float**  | The number of times the device was sensed to have moved between the last session and this session. Only available on \_session.qo events.              | [optional] |
| **note**               | **str**    | The note ID in the notefile                                                                                                                            | [optional] |
| **ordering_code**      | **str**    | Ordering code. Only available on \_session.qo events.                                                                                                  | [optional] |
| **orientation**        | **str**    | The orientation of the device. Only available on \_session.qo events.                                                                                  | [optional] |
| **payload**            | **str**    | A base64-encoded binary payload                                                                                                                        | [optional] |
| **product**            | **str**    | Product UID (globally unique)                                                                                                                          | [optional] |
| **rat**                | **str**    | Rat. Only available on \_session.qo events.                                                                                                            | [optional] |
| **received**           | **float**  | The unix timestamp when the event was received                                                                                                         | [optional] |
| **req**                | **str**    | The notecard request                                                                                                                                   | [optional] |
| **rsrp**               | **float**  | RSRP. Only available on \_session.qo events.                                                                                                           | [optional] |
| **rsrq**               | **float**  | RSRQ. Only available on \_session.qo events.                                                                                                           | [optional] |
| **rssi**               | **float**  | Received Signal Strength Indicator (RSSI) is an estimated measurement of how well a device can receive signals. Only available on \_session.qo events. | [optional] |
| **session**            | **str**    | Session UID (globally unique)                                                                                                                          | [optional] |
| **sinr**               | **float**  | SINR. Only available on \_session.qo events.                                                                                                           | [optional] |
| **sku**                | **str**    | SKU. Only available on \_session.qo events.                                                                                                            | [optional] |
| **sn**                 | **str**    | The device serial number                                                                                                                               | [optional] |
| **ssid**               | **str**    | SSID. Only available on \_session.qo events.                                                                                                           | [optional] |
| **temp**               | **float**  | Device temperature. Only available on \_session.qo events.                                                                                             | [optional] |
| **tls**                | **bool**   | Whether TLS was used on the connection between the device and notehub. Only available on \_session.qo events.                                          | [optional] |
| **tower_country**      | **str**    | Country                                                                                                                                                | [optional] |
| **tower_id**           | **str**    | Tower ID                                                                                                                                               | [optional] |
| **tower_lat**          | **float**  | Latitude                                                                                                                                               | [optional] |
| **tower_location**     | **str**    | Location                                                                                                                                               | [optional] |
| **tower_lon**          | **float**  | Longitude                                                                                                                                              | [optional] |
| **tower_timezone**     | **str**    | Timezone                                                                                                                                               | [optional] |
| **tower_when**         | **float**  | Unix timestamp                                                                                                                                         | [optional] |
| **transport**          | **str**    | The transport used for this event, e.g., \&quot;cellular\&quot;, \&quot;wifi\&quot;, \&quot;, etc.                                                     | [optional] |
| **tri_country**        | **str**    | Country                                                                                                                                                | [optional] |
| **tri_lat**            | **float**  | Latitude                                                                                                                                               | [optional] |
| **tri_location**       | **str**    | Location                                                                                                                                               | [optional] |
| **tri_lon**            | **float**  | Longitude                                                                                                                                              | [optional] |
| **tri_points**         | **float**  | Triangulation points                                                                                                                                   | [optional] |
| **tri_timezone**       | **str**    | Timezone                                                                                                                                               | [optional] |
| **tri_when**           | **float**  | Unix timestamp                                                                                                                                         | [optional] |
| **updates**            | **float**  |                                                                                                                                                        | [optional] |
| **voltage**            | **float**  | Device voltage. Only available on \_session.qo events.                                                                                                 | [optional] |
| **when**               | **float**  | When the event was captured on the device                                                                                                              | [optional] |
| **where_country**      | **str**    | Country                                                                                                                                                | [optional] |
| **where_lat**          | **float**  | Latitude                                                                                                                                               | [optional] |
| **where_location**     | **str**    | Location                                                                                                                                               | [optional] |
| **where_lon**          | **float**  | Longitude                                                                                                                                              | [optional] |
| **where_olc**          | **str**    | Open Location Code                                                                                                                                     | [optional] |
| **where_timezone**     | **str**    | Timezone                                                                                                                                               | [optional] |
| **where_when**         | **float**  | Unix timestamp                                                                                                                                         | [optional] |

## Example

```python
from notehub_py.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
