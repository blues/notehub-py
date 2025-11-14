# GetDeviceLatestEvents200Response

## Properties

| Name              | Type                        | Description                                                                                  | Notes      |
| ----------------- | --------------------------- | -------------------------------------------------------------------------------------------- | ---------- |
| **latest_events** | [**List[Event]**](Event.md) | The set of latest events. Will always include the current \&quot;session.begin\&quot; event. | [optional] |

## Example

```python
from notehub_py.models.get_device_latest_events200_response import GetDeviceLatestEvents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeviceLatestEvents200Response from a JSON string
get_device_latest_events200_response_instance = GetDeviceLatestEvents200Response.from_json(json)
# print the JSON string representation of the object
print(GetDeviceLatestEvents200Response.to_json())

# convert the object into a dict
get_device_latest_events200_response_dict = get_device_latest_events200_response_instance.to_dict()
# create an instance of GetDeviceLatestEvents200Response from a dict
get_device_latest_events200_response_from_dict = GetDeviceLatestEvents200Response.from_dict(get_device_latest_events200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
