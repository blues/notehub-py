# DeviceDfuHistoryCurrent

Description of the current firmware

## Properties

| Name             | Type    | Description                                                                                 | Notes      |
| ---------------- | ------- | ------------------------------------------------------------------------------------------- | ---------- |
| **builder**      | **str** | Firmware author                                                                             | [optional] |
| **built**        | **str** | Firmware build date                                                                         | [optional] |
| **description**  | **str** | Firmware description                                                                        | [optional] |
| **organization** | **str** | Firmware organization                                                                       | [optional] |
| **product**      | **str** | Firmware product                                                                            | [optional] |
| **version**      | **str** | Firmware version the device runs, or &#x60;Unknown (device has not fully sync&#39;d)&#x60;. | [optional] |

## Example

```python
from notehub_py.models.device_dfu_history_current import DeviceDfuHistoryCurrent

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDfuHistoryCurrent from a JSON string
device_dfu_history_current_instance = DeviceDfuHistoryCurrent.from_json(json)
# print the JSON string representation of the object
print(DeviceDfuHistoryCurrent.to_json())

# convert the object into a dict
device_dfu_history_current_dict = device_dfu_history_current_instance.to_dict()
# create an instance of DeviceDfuHistoryCurrent from a dict
device_dfu_history_current_from_dict = DeviceDfuHistoryCurrent.from_dict(
    device_dfu_history_current_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
