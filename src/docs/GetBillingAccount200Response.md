# GetBillingAccount200Response

## Properties

| Name            | Type                                                                        | Description | Notes      |
| --------------- | --------------------------------------------------------------------------- | ----------- | ---------- |
| **contact_uid** | **str**                                                                     |             | [optional] |
| **email**       | **str**                                                                     |             | [optional] |
| **name**        | **str**                                                                     |             | [optional] |
| **owner**       | **str**                                                                     |             | [optional] |
| **plan**        | [**GetBillingAccount200ResponsePlan**](GetBillingAccount200ResponsePlan.md) |             | [optional] |
| **suspended**   | **bool**                                                                    |             | [optional] |
| **uid**         | **str**                                                                     |             | [optional] |

## Example

```python
from notehub_py.models.get_billing_account200_response import (
    GetBillingAccount200Response,
)

# TODO update the JSON string below
json = "{}"
# create an instance of GetBillingAccount200Response from a JSON string
get_billing_account200_response_instance = GetBillingAccount200Response.from_json(json)
# print the JSON string representation of the object
print(GetBillingAccount200Response.to_json())

# convert the object into a dict
get_billing_account200_response_dict = (
    get_billing_account200_response_instance.to_dict()
)
# create an instance of GetBillingAccount200Response from a dict
get_billing_account200_response_from_dict = GetBillingAccount200Response.from_dict(
    get_billing_account200_response_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
