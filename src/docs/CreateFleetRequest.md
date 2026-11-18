# CreateFleetRequest

## Properties

| Name                       | Type                                                            | Description                                                                                                                                                 | Notes      |
| -------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **connectivity_assurance** | [**FleetConnectivityAssurance**](FleetConnectivityAssurance.md) |                                                                                                                                                             | [optional] |
| **label**                  | **str**                                                         | Fleet name shown in Notehub. Required.                                                                                                                      | [optional] |
| **smart_rule**             | **str**                                                         | JSONata expression for smart fleet membership: &#x60;1&#x60; adds the device, &#x60;-1&#x60; removes it, and &#x60;0&#x60; or an error leaves it unchanged. | [optional] |
| **smart_rule_enabled**     | **bool**                                                        | If &#x60;true&#x60;, &#x60;smart_rule&#x60; adds and removes devices. Default &#x60;false&#x60;.                                                            | [optional] |

## Example

```python
from notehub_py.models.create_fleet_request import CreateFleetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFleetRequest from a JSON string
create_fleet_request_instance = CreateFleetRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFleetRequest.to_json())

# convert the object into a dict
create_fleet_request_dict = create_fleet_request_instance.to_dict()
# create an instance of CreateFleetRequest from a dict
create_fleet_request_from_dict = CreateFleetRequest.from_dict(create_fleet_request_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
