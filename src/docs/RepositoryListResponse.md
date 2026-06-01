# RepositoryListResponse

## Properties

| Name             | Type                                  | Description | Notes |
| ---------------- | ------------------------------------- | ----------- | ----- |
| **repositories** | [**List[Repository]**](Repository.md) |             |

## Example

```python
from notehub_py.models.repository_list_response import RepositoryListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryListResponse from a JSON string
repository_list_response_instance = RepositoryListResponse.from_json(json)
# print the JSON string representation of the object
print(RepositoryListResponse.to_json())

# convert the object into a dict
repository_list_response_dict = repository_list_response_instance.to_dict()
# create an instance of RepositoryListResponse from a dict
repository_list_response_from_dict = RepositoryListResponse.from_dict(
    repository_list_response_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
