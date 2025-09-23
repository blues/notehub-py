# FirmwareInfo

## Properties

| Name             | Type     | Description                                  | Notes      |
| ---------------- | -------- | -------------------------------------------- | ---------- |
| **built**        | **str**  | The date the firmware was built.             | [optional] |
| **created**      | **str**  | The date the firmware was created.           | [optional] |
| **description**  | **str**  | A description of the firmware.               | [optional] |
| **filename**     | **str**  | The name of the firmware file.               | [optional] |
| **md5**          | **str**  | The MD5 hash of the firmware file.           | [optional] |
| **organization** | **str**  | The organization that owns the firmware.     | [optional] |
| **product**      | **str**  | The product that the firmware is for.        | [optional] |
| **published**    | **bool** | True if the firmware is published.           | [optional] |
| **tags**         | **str**  | A list of tags associated with the firmware. | [optional] |
| **target**       | **str**  | The target device for the firmware.          | [optional] |
| **type**         | **str**  | The type of firmware.                        | [optional] |
| **version**      | **str**  | The version of the firmware.                 | [optional] |

## Example

```python
from notehub_py.models.firmware_info import FirmwareInfo

# TODO update the JSON string below
json = "{}"
# create an instance of FirmwareInfo from a JSON string
firmware_info_instance = FirmwareInfo.from_json(json)
# print the JSON string representation of the object
print(FirmwareInfo.to_json())

# convert the object into a dict
firmware_info_dict = firmware_info_instance.to_dict()
# create an instance of FirmwareInfo from a dict
firmware_info_from_dict = FirmwareInfo.from_dict(firmware_info_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
