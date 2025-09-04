# PersonalAccessTokenInfo

## Properties

| Name            | Type         | Description                                            | Notes      |
| --------------- | ------------ | ------------------------------------------------------ | ---------- |
| **name**        | **str**      |                                                        | [optional] |
| **description** | **str**      |                                                        | [optional] |
| **expires_at**  | **datetime** | New expiration timestamp for the personal access token | [optional] |
| **suspended**   | **bool**     | if true, the token is temporarily suspended            | [optional] |

## Example

```python
from notehub_py.models.personal_access_token_info import PersonalAccessTokenInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalAccessTokenInfo from a JSON string
personal_access_token_info_instance = PersonalAccessTokenInfo.from_json(json)
# print the JSON string representation of the object
print(PersonalAccessTokenInfo.to_json())

# convert the object into a dict
personal_access_token_info_dict = personal_access_token_info_instance.to_dict()
# create an instance of PersonalAccessTokenInfo from a dict
personal_access_token_info_from_dict = PersonalAccessTokenInfo.from_dict(personal_access_token_info_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
