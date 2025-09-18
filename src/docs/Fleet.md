# Fleet

## Properties

| Name                      | Type               | Description                                                                                                                                                                                                                                                        | Notes      |
| ------------------------- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **created**               | **datetime**       | RFC3339 timestamp in UTC                                                                                                                                                                                                                                           |
| **environment_variables** | **Dict[str, str]** | The environment variables for this device that have been set using the Notehub API or UI.                                                                                                                                                                          | [optional] |
| **label**                 | **str**            | Fleet label                                                                                                                                                                                                                                                        |
| **smart_rule**            | **str**            | JSONata expression that will be evaluated to determine device membership into this fleet, if the expression evaluates to a 1, the device will be included, if it evaluates to -1 it will be removed, and if it evaluates to 0 or errors it will be left unchanged. | [optional] |
| **uid**                   | **str**            | Fleet UID                                                                                                                                                                                                                                                          |
| **watchdog_mins**         | **int**            | A watchdog timer is used to generate an event every N minutes of inactivity. 0 means no watchdog                                                                                                                                                                   | [optional] |

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
