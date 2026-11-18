# GetOrganizationBalanceHistory200Response

## Properties

| Name     | Type                                                                                                                | Description | Notes      |
| -------- | ------------------------------------------------------------------------------------------------------------------- | ----------- | ---------- |
| **data** | [**List[GetOrganizationBalanceHistory200ResponseDataInner]**](GetOrganizationBalanceHistory200ResponseDataInner.md) |             | [optional] |

## Example

```python
from notehub_py.models.get_organization_balance_history200_response import (
    GetOrganizationBalanceHistory200Response,
)

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationBalanceHistory200Response from a JSON string
get_organization_balance_history200_response_instance = (
    GetOrganizationBalanceHistory200Response.from_json(json)
)
# print the JSON string representation of the object
print(GetOrganizationBalanceHistory200Response.to_json())

# convert the object into a dict
get_organization_balance_history200_response_dict = (
    get_organization_balance_history200_response_instance.to_dict()
)
# create an instance of GetOrganizationBalanceHistory200Response from a dict
get_organization_balance_history200_response_from_dict = (
    GetOrganizationBalanceHistory200Response.from_dict(
        get_organization_balance_history200_response_dict
    )
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
