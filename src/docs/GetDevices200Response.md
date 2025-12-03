# GetDevices200Response

## Properties

| Name         | Type                          | Description | Notes |
| ------------ | ----------------------------- | ----------- | ----- |
| **devices**  | [**List[Device]**](Device.md) |             |
| **has_more** | **bool**                      |             |

## Example

```python
from notehub_py.models.get_devices200_response import GetDevices200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDevices200Response from a JSON string
get_devices200_response_instance = GetDevices200Response.from_json(json)
# print the JSON string representation of the object
print(GetDevices200Response.to_json())

# convert the object into a dict
get_devices200_response_dict = get_devices200_response_instance.to_dict()
# create an instance of GetDevices200Response from a dict
get_devices200_response_from_dict = GetDevices200Response.from_dict(get_devices200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
