# GetProjectDevicePublicKeys200Response

## Properties

| Name                   | Type                                                                                                                                  | Description | Notes |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----- |
| **device_public_keys** | [**List[GetProjectDevicePublicKeys200ResponseDevicePublicKeysInner]**](GetProjectDevicePublicKeys200ResponseDevicePublicKeysInner.md) |             |
| **has_more**           | **bool**                                                                                                                              |             |

## Example

```python
from notehub_py.models.get_project_device_public_keys200_response import GetProjectDevicePublicKeys200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectDevicePublicKeys200Response from a JSON string
get_project_device_public_keys200_response_instance = GetProjectDevicePublicKeys200Response.from_json(json)
# print the JSON string representation of the object
print(GetProjectDevicePublicKeys200Response.to_json())

# convert the object into a dict
get_project_device_public_keys200_response_dict = get_project_device_public_keys200_response_instance.to_dict()
# create an instance of GetProjectDevicePublicKeys200Response from a dict
get_project_device_public_keys200_response_from_dict = GetProjectDevicePublicKeys200Response.from_dict(get_project_device_public_keys200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
