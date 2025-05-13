# SimUsage

## Properties

| Name              | Type    | Description                                  | Notes      |
| ----------------- | ------- | -------------------------------------------- | ---------- |
| **iccid**         | **str** | ICCID of the SIM card                        | [optional] |
| **used**          | **int** | Bytes used on the SIMs current data plan     | [optional] |
| **limit**         | **int** | Limit in bytes of the SIMs current data plan | [optional] |
| **lifetime_used** | **int** | Total number of bytes used by SIM            | [optional] |
| **last_updated**  | **int** | Time this usage information was last updated | [optional] |

## Example

```python
from notehub_py.models.sim_usage import SimUsage

# TODO update the JSON string below
json = "{}"
# create an instance of SimUsage from a JSON string
sim_usage_instance = SimUsage.from_json(json)
# print the JSON string representation of the object
print(SimUsage.to_json())

# convert the object into a dict
sim_usage_dict = sim_usage_instance.to_dict()
# create an instance of SimUsage from a dict
sim_usage_from_dict = SimUsage.from_dict(sim_usage_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
