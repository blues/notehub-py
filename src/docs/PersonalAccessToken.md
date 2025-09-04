# PersonalAccessToken

## Properties

| Name            | Type                                                                | Description                           | Notes      |
| --------------- | ------------------------------------------------------------------- | ------------------------------------- | ---------- |
| **uid**         | **str**                                                             | Unique and public identifier          | [optional] |
| **name**        | **str**                                                             | Name for this API Key                 | [optional] |
| **description** | **str**                                                             | Optional description for this API Key | [optional] |
| **created_by**  | [**PersonalAccessTokenCreatedBy**](PersonalAccessTokenCreatedBy.md) |                                       | [optional] |
| **expires_at**  | **datetime**                                                        | When the key expires                  | [optional] |
| **created_at**  | **datetime**                                                        | When the key was created              | [optional] |
| **last_used**   | **datetime**                                                        | When it was last used, if ever        | [optional] |
| **suspended**   | **bool**                                                            | if true, this token cannot be used    | [optional] |

## Example

```python
from notehub_py.models.personal_access_token import PersonalAccessToken

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalAccessToken from a JSON string
personal_access_token_instance = PersonalAccessToken.from_json(json)
# print the JSON string representation of the object
print(PersonalAccessToken.to_json())

# convert the object into a dict
personal_access_token_dict = personal_access_token_instance.to_dict()
# create an instance of PersonalAccessToken from a dict
personal_access_token_from_dict = PersonalAccessToken.from_dict(personal_access_token_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
