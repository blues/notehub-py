# GetOrganizationBalanceHistory200ResponseDataInner

## Properties

| Name                          | Type         | Description | Notes |
| ----------------------------- | ------------ | ----------- | ----- |
| **period**                    | **datetime** |             |
| **remaining_event_capacity**  | **int**      |             |
| **total_event_capacity_used** | **int**      |             |

## Example

```python
from notehub_py.models.get_organization_balance_history200_response_data_inner import (
    GetOrganizationBalanceHistory200ResponseDataInner,
)

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationBalanceHistory200ResponseDataInner from a JSON string
get_organization_balance_history200_response_data_inner_instance = (
    GetOrganizationBalanceHistory200ResponseDataInner.from_json(json)
)
# print the JSON string representation of the object
print(GetOrganizationBalanceHistory200ResponseDataInner.to_json())

# convert the object into a dict
get_organization_balance_history200_response_data_inner_dict = (
    get_organization_balance_history200_response_data_inner_instance.to_dict()
)
# create an instance of GetOrganizationBalanceHistory200ResponseDataInner from a dict
get_organization_balance_history200_response_data_inner_from_dict = (
    GetOrganizationBalanceHistory200ResponseDataInner.from_dict(
        get_organization_balance_history200_response_data_inner_dict
    )
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
