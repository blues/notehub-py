# DfuActionRequest

## Properties

| Name         | Type    | Description                                                                                                                                     | Notes      |
| ------------ | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **filename** | **str** | Stored firmware filename to install, as listed by &#x60;GetFirmwareInfo&#x60;. Required for &#x60;update&#x60;; ignored for &#x60;cancel&#x60;. | [optional] |

## Example

```python
from notehub_py.models.dfu_action_request import DfuActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DfuActionRequest from a JSON string
dfu_action_request_instance = DfuActionRequest.from_json(json)
# print the JSON string representation of the object
print(DfuActionRequest.to_json())

# convert the object into a dict
dfu_action_request_dict = dfu_action_request_instance.to_dict()
# create an instance of DfuActionRequest from a dict
dfu_action_request_from_dict = DfuActionRequest.from_dict(dfu_action_request_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
