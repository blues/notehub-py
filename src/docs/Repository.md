# Repository

## Properties

| Name             | Type                                | Description                                                                 | Notes      |
| ---------------- | ----------------------------------- | --------------------------------------------------------------------------- | ---------- |
| **archive**      | [**ArchiveStats**](ArchiveStats.md) |                                                                             | [optional] |
| **fleet_uids**   | **List[str]**                       |                                                                             | [optional] |
| **name**         | **str**                             | Repository name.                                                            | [optional] |
| **project_uids** | **List[str]**                       |                                                                             | [optional] |
| **uid**          | **str**                             | Repository UID, e.g. &#x60;repo:2606f411-dea6-44a0-9743-1130f57d77d8&#x60;. | [optional] |

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
