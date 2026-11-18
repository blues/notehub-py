# ProvisionDeviceRequest

## Properties

| Name            | Type          | Description                                                                                                                                    | Notes      |
| --------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **device_sn**   | **str**       | Serial number to give the device. Ignored if the device already has one.                                                                       | [optional] |
| **fleet_uids**  | **List[str]** | FleetUIDs to put a new device in. If omitted or empty, the product&#39;s auto-provision fleets are used. Ignored if the device already exists. | [optional] |
| **product_uid** | **str**       | ProductUID to provision the device under, e.g. &#x60;com.blues.bridge:sensors&#x60;. Must belong to this project.                              |

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
provision_device_request_from_dict = ProvisionDeviceRequest.from_dict(
    provision_device_request_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
