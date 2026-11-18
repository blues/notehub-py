# GetDevicePublicKeys200Response

## Properties

| Name                   | Type                                                                                                                    | Description                                                                                                                                                                                                                       | Notes      |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **device_public_keys** | [**List[GetDevicePublicKeys200ResponseDevicePublicKeysInner]**](GetDevicePublicKeys200ResponseDevicePublicKeysInner.md) |                                                                                                                                                                                                                                   |
| **has_more**           | **bool**                                                                                                                |                                                                                                                                                                                                                                   |
| **next_cursor**        | **str**                                                                                                                 | Pass this value (epoch microseconds, optionally &#x60;.N&#x60;) as a cursor parameter to start a search from where the last search left off. Returned even when there are no more results, so it can be used to poll for changes. | [optional] |

## Example

```python
from notehub_py.models.get_device_public_keys200_response import (
    GetDevicePublicKeys200Response,
)

# TODO update the JSON string below
json = "{}"
# create an instance of GetDevicePublicKeys200Response from a JSON string
get_device_public_keys200_response_instance = GetDevicePublicKeys200Response.from_json(
    json
)
# print the JSON string representation of the object
print(GetDevicePublicKeys200Response.to_json())

# convert the object into a dict
get_device_public_keys200_response_dict = (
    get_device_public_keys200_response_instance.to_dict()
)
# create an instance of GetDevicePublicKeys200Response from a dict
get_device_public_keys200_response_from_dict = GetDevicePublicKeys200Response.from_dict(
    get_device_public_keys200_response_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
