# CreateProjectSecretRequest

## Properties

| Name      | Type    | Description                                                          | Notes |
| --------- | ------- | -------------------------------------------------------------------- | ----- |
| **name**  | **str** | The secret name (alphanumeric and underscores only).                 |
| **value** | **str** | The secret value (encrypted at rest, never returned after creation). |

## Example

```python
from notehub_py.models.create_project_secret_request import CreateProjectSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectSecretRequest from a JSON string
create_project_secret_request_instance = CreateProjectSecretRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProjectSecretRequest.to_json())

# convert the object into a dict
create_project_secret_request_dict = create_project_secret_request_instance.to_dict()
# create an instance of CreateProjectSecretRequest from a dict
create_project_secret_request_from_dict = CreateProjectSecretRequest.from_dict(
    create_project_secret_request_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
