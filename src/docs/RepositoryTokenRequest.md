# RepositoryTokenRequest

## Properties

| Name            | Type    | Description                                                                                                                                              | Notes                          |
| --------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **intent**      | **str** | Access intent for the vended credentials. Only &#x60;read&#x60; is supported today; &#x60;write&#x60; and &#x60;admin&#x60; are reserved for future use. | [optional] [default to 'read'] |
| **ttl_seconds** | **int** | Requested credential lifetime in seconds. Clamped server-side to [60, 3600]. Defaults to 900 (15 minutes) if omitted.                                    | [optional] [default to 900]    |

## Example

```python
from notehub_py.models.repository_token_request import RepositoryTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryTokenRequest from a JSON string
repository_token_request_instance = RepositoryTokenRequest.from_json(json)
# print the JSON string representation of the object
print(RepositoryTokenRequest.to_json())

# convert the object into a dict
repository_token_request_dict = repository_token_request_instance.to_dict()
# create an instance of RepositoryTokenRequest from a dict
repository_token_request_from_dict = RepositoryTokenRequest.from_dict(
    repository_token_request_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
