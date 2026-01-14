# SatellitePlan

## Properties

| Name                       | Type                                            | Description                                                 | Notes      |
| -------------------------- | ----------------------------------------------- | ----------------------------------------------------------- | ---------- |
| **activated**              | **int**                                         | Activation date of the satellite plan as Unix timestamp     |
| **last_session_at**        | **int**                                         | When this Starnote last had a session                       | [optional] |
| **minimum_billable_bytes** | **int**                                         | Minimum billable bytes                                      | [optional] |
| **ntn_provider**           | **str**                                         | Non-Terrestrial Network provider name                       |
| **psid**                   | **str**                                         | Provider-specific identifier for the satellite subscription |
| **satellite_data_usage**   | [**SatelliteDataUsage**](SatelliteDataUsage.md) |                                                             | [optional] |

## Example

```python
from notehub_py.models.satellite_plan import SatellitePlan

# TODO update the JSON string below
json = "{}"
# create an instance of SatellitePlan from a JSON string
satellite_plan_instance = SatellitePlan.from_json(json)
# print the JSON string representation of the object
print(SatellitePlan.to_json())

# convert the object into a dict
satellite_plan_dict = satellite_plan_instance.to_dict()
# create an instance of SatellitePlan from a dict
satellite_plan_from_dict = SatellitePlan.from_dict(satellite_plan_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
