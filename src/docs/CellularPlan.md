# CellularPlan

## Properties

| Name              | Type                          | Description                                                                            | Notes      |
| ----------------- | ----------------------------- | -------------------------------------------------------------------------------------- | ---------- |
| **activated**     | **int**                       | Unix timestamp of when the SIM was activated                                           | [optional] |
| **data_usage**    | [**DataUsage**](DataUsage.md) |                                                                                        | [optional] |
| **expires_at**    | **int**                       |                                                                                        | [optional] |
| **iccid**         | **str**                       | The Integrated Circuit Card Identifier of the SIM card                                 | [optional] |
| **imsi**          | **str**                       | IMSI of the SIM card                                                                   | [optional] |
| **last_updated**  | **int**                       | Time this plan information was last updated                                            | [optional] |
| **lifetime_used** | **int**                       | Total bytes used by this SIM                                                           | [optional] |
| **plan_type**     | **str**                       | Description of the SIM plan type including data allowance, region, and validity period | [optional] |

## Example

```python
from notehub_py.models.cellular_plan import CellularPlan

# TODO update the JSON string below
json = "{}"
# create an instance of CellularPlan from a JSON string
cellular_plan_instance = CellularPlan.from_json(json)
# print the JSON string representation of the object
print(CellularPlan.to_json())

# convert the object into a dict
cellular_plan_dict = cellular_plan_instance.to_dict()
# create an instance of CellularPlan from a dict
cellular_plan_from_dict = CellularPlan.from_dict(cellular_plan_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
