# ProjectSecret

Metadata for a project secret. The value is never returned.

## Properties

| Name            | Type         | Description                                                                    | Notes      |
| --------------- | ------------ | ------------------------------------------------------------------------------ | ---------- |
| **created**     | **datetime** | When the secret was first created.                                             |
| **created_by**  | **str**      | UID of the user or OAuth client that created the secret.                       |
| **modified**    | **datetime** | When the secret&#39;s value was last set.                                      | [optional] |
| **modified_by** | **str**      | UID of the user or OAuth client that last set the secret&#39;s value.          | [optional] |
| **name**        | **str**      | The secret&#39;s name. Routes and alerts reference it as &#x60;[$$name]&#x60;. |

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
