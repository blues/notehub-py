# GetProjectSecretsResponse

## Properties

| Name        | Type                                        | Description | Notes |
| ----------- | ------------------------------------------- | ----------- | ----- |
| **secrets** | [**List[ProjectSecret]**](ProjectSecret.md) |             |

## Example

```python
from notehub_py.models.get_project_secrets_response import GetProjectSecretsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectSecretsResponse from a JSON string
get_project_secrets_response_instance = GetProjectSecretsResponse.from_json(json)
# print the JSON string representation of the object
print(GetProjectSecretsResponse.to_json())

# convert the object into a dict
get_project_secrets_response_dict = get_project_secrets_response_instance.to_dict()
# create an instance of GetProjectSecretsResponse from a dict
get_project_secrets_response_from_dict = GetProjectSecretsResponse.from_dict(
    get_project_secrets_response_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
