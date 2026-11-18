# GetOrganization200Response

## Properties

| Name            | Type                                                                    | Description | Notes      |
| --------------- | ----------------------------------------------------------------------- | ----------- | ---------- |
| **contact_uid** | **str**                                                                 |             | [optional] |
| **email**       | **str**                                                                 |             | [optional] |
| **name**        | **str**                                                                 |             | [optional] |
| **owner**       | **str**                                                                 |             | [optional] |
| **plan**        | [**GetOrganization200ResponsePlan**](GetOrganization200ResponsePlan.md) |             | [optional] |
| **suspended**   | **bool**                                                                |             | [optional] |
| **uid**         | **str**                                                                 |             | [optional] |

## Example

```python
from notehub_py.models.get_organization200_response import GetOrganization200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganization200Response from a JSON string
get_organization200_response_instance = GetOrganization200Response.from_json(json)
# print the JSON string representation of the object
print(GetOrganization200Response.to_json())

# convert the object into a dict
get_organization200_response_dict = get_organization200_response_instance.to_dict()
# create an instance of GetOrganization200Response from a dict
get_organization200_response_from_dict = GetOrganization200Response.from_dict(
    get_organization200_response_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
