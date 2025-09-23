# OAuth2TokenResponse

## Properties

| Name             | Type    | Description                              | Notes      |
| ---------------- | ------- | ---------------------------------------- | ---------- |
| **access_token** | **str** | The issued access token                  |
| **expires_in**   | **int** | Lifetime in seconds of the access token. |
| **scope**        | **str** | Granted scopes (space-delimited).        | [optional] |
| **token_type**   | **str** | Usually &#39;bearer&#39;                 |

## Example

```python
from notehub_py.models.o_auth2_token_response import OAuth2TokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2TokenResponse from a JSON string
o_auth2_token_response_instance = OAuth2TokenResponse.from_json(json)
# print the JSON string representation of the object
print(OAuth2TokenResponse.to_json())

# convert the object into a dict
o_auth2_token_response_dict = o_auth2_token_response_instance.to_dict()
# create an instance of OAuth2TokenResponse from a dict
o_auth2_token_response_from_dict = OAuth2TokenResponse.from_dict(o_auth2_token_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
