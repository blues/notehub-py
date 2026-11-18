# Fleet

## Properties

| Name                       | Type                                                            | Description                                                                                                                                                 | Notes      |
| -------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **connectivity_assurance** | [**FleetConnectivityAssurance**](FleetConnectivityAssurance.md) |                                                                                                                                                             | [optional] |
| **created**                | **datetime**                                                    | When the fleet was created.                                                                                                                                 |
| **environment_variables**  | **Dict[str, str]**                                              | Environment variables set on this fleet. Not returned by &#x60;GetDeviceFleets&#x60;.                                                                       | [optional] |
| **label**                  | **str**                                                         | Fleet name shown in Notehub.                                                                                                                                |
| **smart_rule**             | **str**                                                         | JSONata expression for smart fleet membership: &#x60;1&#x60; adds the device, &#x60;-1&#x60; removes it, and &#x60;0&#x60; or an error leaves it unchanged. | [optional] |
| **smart_rule_enabled**     | **bool**                                                        | Whether &#x60;smart_rule&#x60; adds and removes devices. Returned only by &#x60;CreateFleet&#x60; and &#x60;UpdateFleet&#x60;.                              | [optional] |
| **uid**                    | **str**                                                         | FleetUID, e.g. &#x60;fleet:1042ddc5-3b2c-4cec-b1fb-d3040538094d&#x60;.                                                                                      |
| **watchdog_mins**          | **int**                                                         | Minutes of inactivity before Notehub generates a watchdog event. &#x60;0&#x60; means no watchdog.                                                           | [optional] |

## Example

```python
from notehub_py.models.fleet import Fleet

# TODO update the JSON string below
json = "{}"
# create an instance of Fleet from a JSON string
fleet_instance = Fleet.from_json(json)
# print the JSON string representation of the object
print(Fleet.to_json())

# convert the object into a dict
fleet_dict = fleet_instance.to_dict()
# create an instance of Fleet from a dict
fleet_from_dict = Fleet.from_dict(fleet_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
