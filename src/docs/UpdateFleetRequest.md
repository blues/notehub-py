# UpdateFleetRequest

## Properties

| Name                       | Type                                                            | Description                                                                                                                                                 | Notes      |
| -------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **add_devices**            | **List[str]**                                                   | DeviceUIDs to add to the fleet. Each must be in the project and not also in &#x60;removeDevices&#x60;.                                                      | [optional] |
| **connectivity_assurance** | [**FleetConnectivityAssurance**](FleetConnectivityAssurance.md) |                                                                                                                                                             | [optional] |
| **label**                  | **str**                                                         | New fleet name. Empty keeps the current name; a fleet must have one, so &#x60;-&#x60; returns 400.                                                          | [optional] |
| **remove_devices**         | **List[str]**                                                   | DeviceUIDs to remove from the fleet. Each must be in the project and not also in &#x60;addDevices&#x60;.                                                    | [optional] |
| **smart_rule**             | **str**                                                         | JSONata expression for smart fleet membership: &#x60;1&#x60; adds the device, &#x60;-1&#x60; removes it, and &#x60;0&#x60; or an error leaves it unchanged. | [optional] |
| **smart_rule_enabled**     | **bool**                                                        | Whether &#x60;smart_rule&#x60; adds and removes devices. Always send it; omitting it sets &#x60;false&#x60;.                                                | [optional] |
| **watchdog_mins**          | **int**                                                         | Minutes of inactivity before Notehub generates a watchdog event. Omit or &#x60;0&#x60; to keep the current value; a negative value turns it off.            | [optional] |

## Example

```python
from notehub_py.models.update_fleet_request import UpdateFleetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFleetRequest from a JSON string
update_fleet_request_instance = UpdateFleetRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFleetRequest.to_json())

# convert the object into a dict
update_fleet_request_dict = update_fleet_request_instance.to_dict()
# create an instance of UpdateFleetRequest from a dict
update_fleet_request_from_dict = UpdateFleetRequest.from_dict(update_fleet_request_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
