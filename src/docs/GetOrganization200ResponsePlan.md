# GetOrganization200ResponsePlan

## Properties

| Name                | Type         | Description | Notes      |
| ------------------- | ------------ | ----------- | ---------- |
| **current_balance** | **int**      |             | [optional] |
| **end_date**        | **datetime** |             | [optional] |
| **event_capacity**  | **int**      |             | [optional] |
| **start_date**      | **datetime** |             | [optional] |
| **type**            | **str**      |             | [optional] |

## Example

```python
from notehub_py.models.get_organization200_response_plan import (
    GetOrganization200ResponsePlan,
)

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganization200ResponsePlan from a JSON string
get_organization200_response_plan_instance = GetOrganization200ResponsePlan.from_json(
    json
)
# print the JSON string representation of the object
print(GetOrganization200ResponsePlan.to_json())

# convert the object into a dict
get_organization200_response_plan_dict = (
    get_organization200_response_plan_instance.to_dict()
)
# create an instance of GetOrganization200ResponsePlan from a dict
get_organization200_response_plan_from_dict = GetOrganization200ResponsePlan.from_dict(
    get_organization200_response_plan_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
