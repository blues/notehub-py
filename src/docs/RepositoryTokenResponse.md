# RepositoryTokenResponse

## Properties

| Name           | Type         | Description                                                                                                                  | Notes |
| -------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------- | ----- |
| **database**   | **str**      | Storage service database name scoped to this repository                                                                      |
| **expires_at** | **datetime** | Absolute expiration time of the ephemeral user. The storage service will reject connections and queries after this instant.  |
| **host**       | **str**      | Storage service hostname the caller should connect to                                                                        |
| **password**   | **str**      | Ephemeral password. Returned once; not stored by Notehub. Hold this in memory only and discard after &#x60;expires_at&#x60;. |
| **port**       | **int**      | Storage service port                                                                                                         |
| **username**   | **str**      | Ephemeral storage service username (prefixed with &#x60;u\_&#x60;)                                                           |

## Example

```python
from notehub_py.models.repository_token_response import RepositoryTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryTokenResponse from a JSON string
repository_token_response_instance = RepositoryTokenResponse.from_json(json)
# print the JSON string representation of the object
print(RepositoryTokenResponse.to_json())

# convert the object into a dict
repository_token_response_dict = repository_token_response_instance.to_dict()
# create an instance of RepositoryTokenResponse from a dict
repository_token_response_from_dict = RepositoryTokenResponse.from_dict(
    repository_token_response_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
