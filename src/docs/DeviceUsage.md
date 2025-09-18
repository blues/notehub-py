# DeviceUsage

## Properties

| Name                     | Type    | Description         | Notes      |
| ------------------------ | ------- | ------------------- | ---------- |
| **bytes_rcvd**           | **int** |                     | [optional] |
| **bytes_rcvd_secondary** | **int** |                     | [optional] |
| **bytes_sent**           | **int** |                     | [optional] |
| **bytes_sent_secondary** | **int** |                     | [optional] |
| **duration**             | **int** | Duration in seconds | [optional] |
| **notes_rcvd**           | **int** |                     | [optional] |
| **notes_sent**           | **int** |                     | [optional] |
| **sessions_tcp**         | **int** |                     | [optional] |
| **sessions_tls**         | **int** |                     | [optional] |
| **since**                | **int** | Unix timestamp      | [optional] |

## Example

```python
from notehub_py.models.device_usage import DeviceUsage

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceUsage from a JSON string
device_usage_instance = DeviceUsage.from_json(json)
# print the JSON string representation of the object
print(DeviceUsage.to_json())

# convert the object into a dict
device_usage_dict = device_usage_instance.to_dict()
# create an instance of DeviceUsage from a dict
device_usage_from_dict = DeviceUsage.from_dict(device_usage_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
