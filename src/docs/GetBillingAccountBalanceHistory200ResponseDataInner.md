# GetBillingAccountBalanceHistory200ResponseDataInner

## Properties

| Name                          | Type         | Description | Notes |
| ----------------------------- | ------------ | ----------- | ----- |
| **period**                    | **datetime** |             |
| **remaining_event_capacity**  | **int**      |             |
| **total_event_capacity_used** | **int**      |             |

## Example

```python
from notehub_py.models.get_billing_account_balance_history200_response_data_inner import GetBillingAccountBalanceHistory200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetBillingAccountBalanceHistory200ResponseDataInner from a JSON string
get_billing_account_balance_history200_response_data_inner_instance = GetBillingAccountBalanceHistory200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetBillingAccountBalanceHistory200ResponseDataInner.to_json())

# convert the object into a dict
get_billing_account_balance_history200_response_data_inner_dict = get_billing_account_balance_history200_response_data_inner_instance.to_dict()
# create an instance of GetBillingAccountBalanceHistory200ResponseDataInner from a dict
get_billing_account_balance_history200_response_data_inner_from_dict = GetBillingAccountBalanceHistory200ResponseDataInner.from_dict(get_billing_account_balance_history200_response_data_inner_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
