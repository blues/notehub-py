# ProvisionDeviceRequest

## Properties

| Name            | Type          | Description                                | Notes      |
| --------------- | ------------- | ------------------------------------------ | ---------- |
| **device_sn**   | **str**       | The serial number to assign to the device. | [optional] |
| **fleet_uids**  | **List[str]** | The fleetUIDs to provision the device to.  | [optional] |
| **product_uid** | **str**       | The ProductUID that the device should use. |

## Example

```python
from notehub_py.models.provision_device_request import ProvisionDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisionDeviceRequest from a JSON string
provision_device_request_instance = ProvisionDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(ProvisionDeviceRequest.to_json())

# convert the object into a dict
provision_device_request_dict = provision_device_request_instance.to_dict()
# create an instance of ProvisionDeviceRequest from a dict
provision_device_request_from_dict = ProvisionDeviceRequest.from_dict(provision_device_request_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
