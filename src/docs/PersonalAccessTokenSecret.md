# PersonalAccessTokenSecret

## Properties

| Name       | Type    | Description                  | Notes      |
| ---------- | ------- | ---------------------------- | ---------- |
| **secret** | **str** | The secret                   | [optional] |
| **uid**    | **str** | Unique and public identifier | [optional] |

## Example

```python
from notehub_py.models.personal_access_token_secret import PersonalAccessTokenSecret

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalAccessTokenSecret from a JSON string
personal_access_token_secret_instance = PersonalAccessTokenSecret.from_json(json)
# print the JSON string representation of the object
print(PersonalAccessTokenSecret.to_json())

# convert the object into a dict
personal_access_token_secret_dict = personal_access_token_secret_instance.to_dict()
# create an instance of PersonalAccessTokenSecret from a dict
personal_access_token_secret_from_dict = PersonalAccessTokenSecret.from_dict(personal_access_token_secret_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
