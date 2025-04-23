# Repository

## Properties

| Name             | Type          | Description                                   | Notes      |
| ---------------- | ------------- | --------------------------------------------- | ---------- |
| **uid**          | **str**       | The unique identifier for the data repository | [optional] |
| **name**         | **str**       | repository name                               | [optional] |
| **fleet_uids**   | **List[str]** |                                               | [optional] |
| **project_uids** | **List[str]** |                                               | [optional] |

## Example

```python
from notehub_py.models.repository import Repository

# TODO update the JSON string below
json = "{}"
# create an instance of Repository from a JSON string
repository_instance = Repository.from_json(json)
# print the JSON string representation of the object
print(Repository.to_json())

# convert the object into a dict
repository_dict = repository_instance.to_dict()
# create an instance of Repository from a dict
repository_from_dict = Repository.from_dict(repository_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
