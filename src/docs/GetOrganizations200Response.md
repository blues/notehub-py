# GetOrganizations200Response

## Properties

| Name              | Type                                      | Description | Notes      |
| ----------------- | ----------------------------------------- | ----------- | ---------- |
| **organizations** | [**List[Organization]**](Organization.md) |             | [optional] |

## Example

```python
from notehub_py.models.get_organizations200_response import GetOrganizations200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizations200Response from a JSON string
get_organizations200_response_instance = GetOrganizations200Response.from_json(json)
# print the JSON string representation of the object
print(GetOrganizations200Response.to_json())

# convert the object into a dict
get_organizations200_response_dict = get_organizations200_response_instance.to_dict()
# create an instance of GetOrganizations200Response from a dict
get_organizations200_response_from_dict = GetOrganizations200Response.from_dict(
    get_organizations200_response_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
