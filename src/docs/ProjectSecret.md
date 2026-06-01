# ProjectSecret

Metadata for a project secret. The value is never returned.

## Properties

| Name            | Type         | Description                                          | Notes      |
| --------------- | ------------ | ---------------------------------------------------- | ---------- |
| **created**     | **datetime** | When the secret was first created.                   |
| **created_by**  | **str**      | The actor who created the secret.                    |
| **modified**    | **datetime** | When the secret was last updated.                    | [optional] |
| **modified_by** | **str**      | The actor who last updated the secret.               | [optional] |
| **name**        | **str**      | The secret name (alphanumeric and underscores only). |

## Example

```python
from notehub_py.models.project_secret import ProjectSecret

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectSecret from a JSON string
project_secret_instance = ProjectSecret.from_json(json)
# print the JSON string representation of the object
print(ProjectSecret.to_json())

# convert the object into a dict
project_secret_dict = project_secret_instance.to_dict()
# create an instance of ProjectSecret from a dict
project_secret_from_dict = ProjectSecret.from_dict(project_secret_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
