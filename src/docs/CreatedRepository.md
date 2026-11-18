# CreatedRepository

## Properties

| Name             | Type          | Description                                                                                                                     | Notes      |
| ---------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **fleet_uids**   | **List[str]** |                                                                                                                                 | [optional] |
| **name**         | **str**       | Repository name.                                                                                                                | [optional] |
| **password**     | **str**       | The repository key, for &#x60;X-Repository-Key&#x60; and as the database password. Returned only here, never to a scoped token. | [optional] |
| **project_uids** | **List[str]** |                                                                                                                                 | [optional] |
| **uid**          | **str**       | Repository UID, e.g. &#x60;repo:2606f411-dea6-44a0-9743-1130f57d77d8&#x60;.                                                     | [optional] |
| **user**         | **str**       | Read-only database user that goes with &#x60;password&#x60;.                                                                    | [optional] |

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
