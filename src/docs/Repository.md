# Repository

## Properties

| Name             | Type          | Description                                   | Notes      |
| ---------------- | ------------- | --------------------------------------------- | ---------- |
| **fleet_uids**   | **List[str]** |                                               | [optional] |
| **name**         | **str**       | repository name                               | [optional] |
| **project_uids** | **List[str]** |                                               | [optional] |
| **uid**          | **str**       | The unique identifier for the data repository | [optional] |

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
