# DeviceDfuStatus

## Properties

| Name                | Type                                                      | Description                                                                                | Notes      |
| ------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ---------- |
| **current**         | [**DeviceDfuHistoryCurrent**](DeviceDfuHistoryCurrent.md) |                                                                                            | [optional] |
| **deleted**         | **bool**                                                  | True if this device has been deleted. Only present when reading with a &#x60;cursor&#x60;. | [optional] |
| **device_uid**      | **str**                                                   | DeviceUID                                                                                  | [optional] |
| **dfu_in_progress** | **bool**                                                  | &#x60;true&#x60; while the device&#39;s latest firmware update hasn&#39;t finished.        | [optional] |
| **status**          | [**DeviceDfuStateMachine**](DeviceDfuStateMachine.md)     |                                                                                            | [optional] |

## Example

```python
from notehub_py.models.device_dfu_status import DeviceDfuStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceDfuStatus from a JSON string
device_dfu_status_instance = DeviceDfuStatus.from_json(json)
# print the JSON string representation of the object
print(DeviceDfuStatus.to_json())

# convert the object into a dict
device_dfu_status_dict = device_dfu_status_instance.to_dict()
# create an instance of DeviceDfuStatus from a dict
device_dfu_status_from_dict = DeviceDfuStatus.from_dict(device_dfu_status_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
