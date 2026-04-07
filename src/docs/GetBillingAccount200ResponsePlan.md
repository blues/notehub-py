# GetBillingAccount200ResponsePlan

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
from notehub_py.models.get_billing_account200_response_plan import GetBillingAccount200ResponsePlan

# TODO update the JSON string below
json = "{}"
# create an instance of GetBillingAccount200ResponsePlan from a JSON string
get_billing_account200_response_plan_instance = GetBillingAccount200ResponsePlan.from_json(json)
# print the JSON string representation of the object
print(GetBillingAccount200ResponsePlan.to_json())

# convert the object into a dict
get_billing_account200_response_plan_dict = get_billing_account200_response_plan_instance.to_dict()
# create an instance of GetBillingAccount200ResponsePlan from a dict
get_billing_account200_response_plan_from_dict = GetBillingAccount200ResponsePlan.from_dict(get_billing_account200_response_plan_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
