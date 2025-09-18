# CreateUpdateRepository

## Properties

| Name             | Type          | Description | Notes      |
| ---------------- | ------------- | ----------- | ---------- |
| **fleet_uids**   | **List[str]** |             | [optional] |
| **name**         | **str**       |             | [optional] |
| **project_uids** | **List[str]** |             | [optional] |

## Example

```python
from notehub_py.models.create_update_repository import CreateUpdateRepository

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUpdateRepository from a JSON string
create_update_repository_instance = CreateUpdateRepository.from_json(json)
# print the JSON string representation of the object
print(CreateUpdateRepository.to_json())

# convert the object into a dict
create_update_repository_dict = create_update_repository_instance.to_dict()
# create an instance of CreateUpdateRepository from a dict
create_update_repository_from_dict = CreateUpdateRepository.from_dict(create_update_repository_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
