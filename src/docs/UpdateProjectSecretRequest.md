# UpdateProjectSecretRequest

## Properties

| Name      | Type    | Description                                               | Notes |
| --------- | ------- | --------------------------------------------------------- | ----- |
| **value** | **str** | The new secret value (encrypted at rest, never returned). |

## Example

```python
from notehub_py.models.update_project_secret_request import UpdateProjectSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProjectSecretRequest from a JSON string
update_project_secret_request_instance = UpdateProjectSecretRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProjectSecretRequest.to_json())

# convert the object into a dict
update_project_secret_request_dict = update_project_secret_request_instance.to_dict()
# create an instance of UpdateProjectSecretRequest from a dict
update_project_secret_request_from_dict = UpdateProjectSecretRequest.from_dict(
    update_project_secret_request_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
