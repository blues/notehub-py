# AddDeviceToFleetsRequest

## Properties

| Name           | Type          | Description                         | Notes |
| -------------- | ------------- | ----------------------------------- | ----- |
| **fleet_uids** | **List[str]** | The fleetUIDs to add to the device. |

## Example

```python
from notehub_py.models.add_device_to_fleets_request import AddDeviceToFleetsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDeviceToFleetsRequest from a JSON string
add_device_to_fleets_request_instance = AddDeviceToFleetsRequest.from_json(json)
# print the JSON string representation of the object
print(AddDeviceToFleetsRequest.to_json())

# convert the object into a dict
add_device_to_fleets_request_dict = add_device_to_fleets_request_instance.to_dict()
# create an instance of AddDeviceToFleetsRequest from a dict
add_device_to_fleets_request_from_dict = AddDeviceToFleetsRequest.from_dict(add_device_to_fleets_request_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
