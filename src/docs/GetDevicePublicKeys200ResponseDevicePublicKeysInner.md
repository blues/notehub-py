# GetDevicePublicKeys200ResponseDevicePublicKeysInner

## Properties

| Name        | Type     | Description                                                                                | Notes      |
| ----------- | -------- | ------------------------------------------------------------------------------------------ | ---------- |
| **deleted** | **bool** | True if this device has been deleted. Only present when reading with a &#x60;cursor&#x60;. | [optional] |
| **key**     | **str**  | The Notecard&#39;s public key in PEM format. Empty if it hasn&#39;t reported one.          | [optional] |
| **uid**     | **str**  | DeviceUID, e.g. &#x60;dev:864475040509284&#x60;.                                           | [optional] |

## Example

```python
from notehub_py.models.get_device_public_keys200_response_device_public_keys_inner import (
    GetDevicePublicKeys200ResponseDevicePublicKeysInner,
)

# TODO update the JSON string below
json = "{}"
# create an instance of GetDevicePublicKeys200ResponseDevicePublicKeysInner from a JSON string
get_device_public_keys200_response_device_public_keys_inner_instance = (
    GetDevicePublicKeys200ResponseDevicePublicKeysInner.from_json(json)
)
# print the JSON string representation of the object
print(GetDevicePublicKeys200ResponseDevicePublicKeysInner.to_json())

# convert the object into a dict
get_device_public_keys200_response_device_public_keys_inner_dict = (
    get_device_public_keys200_response_device_public_keys_inner_instance.to_dict()
)
# create an instance of GetDevicePublicKeys200ResponseDevicePublicKeysInner from a dict
get_device_public_keys200_response_device_public_keys_inner_from_dict = (
    GetDevicePublicKeys200ResponseDevicePublicKeysInner.from_dict(
        get_device_public_keys200_response_device_public_keys_inner_dict
    )
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
