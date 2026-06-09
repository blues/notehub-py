# CreatedRepository

## Properties

| Name             | Type          | Description                                                                                                                                                         | Notes      |
| ---------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **fleet_uids**   | **List[str]** |                                                                                                                                                                     | [optional] |
| **name**         | **str**       | repository name                                                                                                                                                     | [optional] |
| **password**     | **str**       | read-only password for the database, also used as X-Repository-Token header for subsequent API calls. This value is only served once when the repository is created | [optional] |
| **project_uids** | **List[str]** |                                                                                                                                                                     | [optional] |
| **uid**          | **str**       | The unique identifier for the data repository                                                                                                                       | [optional] |
| **user**         | **str**       | read-only user for database                                                                                                                                         | [optional] |

## Example

```python
from notehub_py.models.created_repository import CreatedRepository

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedRepository from a JSON string
created_repository_instance = CreatedRepository.from_json(json)
# print the JSON string representation of the object
print(CreatedRepository.to_json())

# convert the object into a dict
created_repository_dict = created_repository_instance.to_dict()
# create an instance of CreatedRepository from a dict
created_repository_from_dict = CreatedRepository.from_dict(created_repository_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
