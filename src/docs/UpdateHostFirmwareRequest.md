# UpdateHostFirmwareRequest

Request body for updating host firmware metadata. All fields are optional; only provided fields will be updated.

## Properties

| Name        | Type                  | Description                                                               | Notes      |
| ----------- | --------------------- | ------------------------------------------------------------------------- | ---------- |
| **info**    | **Dict[str, object]** | JSON metadata for this firmware. Replaces the stored object when present. | [optional] |
| **notes**   | **str**               | New notes for this firmware. Empty keeps the current notes.               | [optional] |
| **version** | **str**               | New version string. Empty keeps the current version.                      | [optional] |

## Example

```python
from notehub_py.models.update_host_firmware_request import UpdateHostFirmwareRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHostFirmwareRequest from a JSON string
update_host_firmware_request_instance = UpdateHostFirmwareRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateHostFirmwareRequest.to_json())

# convert the object into a dict
update_host_firmware_request_dict = update_host_firmware_request_instance.to_dict()
# create an instance of UpdateHostFirmwareRequest from a dict
update_host_firmware_request_from_dict = UpdateHostFirmwareRequest.from_dict(
    update_host_firmware_request_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
