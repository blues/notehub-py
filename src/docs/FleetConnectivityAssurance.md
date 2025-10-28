# FleetConnectivityAssurance

## Properties

| Name        | Type     | Description                                              | Notes |
| ----------- | -------- | -------------------------------------------------------- | ----- |
| **enabled** | **bool** | Whether Connectivity Assurance is enabled for this fleet |

## Example

```python
from notehub_py.models.fleet_connectivity_assurance import FleetConnectivityAssurance

# TODO update the JSON string below
json = "{}"
# create an instance of FleetConnectivityAssurance from a JSON string
fleet_connectivity_assurance_instance = FleetConnectivityAssurance.from_json(json)
# print the JSON string representation of the object
print(FleetConnectivityAssurance.to_json())

# convert the object into a dict
fleet_connectivity_assurance_dict = fleet_connectivity_assurance_instance.to_dict()
# create an instance of FleetConnectivityAssurance from a dict
fleet_connectivity_assurance_from_dict = FleetConnectivityAssurance.from_dict(fleet_connectivity_assurance_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
