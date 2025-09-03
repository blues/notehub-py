# PersonalAccessTokenCreatedBy

The user that created this key

## Properties

| Name      | Type    | Description | Notes      |
| --------- | ------- | ----------- | ---------- |
| **uid**   | **str** |             | [optional] |
| **email** | **str** |             | [optional] |
| **name**  | **str** |             | [optional] |

## Example

```python
from notehub_py.models.personal_access_token_created_by import PersonalAccessTokenCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalAccessTokenCreatedBy from a JSON string
personal_access_token_created_by_instance = PersonalAccessTokenCreatedBy.from_json(json)
# print the JSON string representation of the object
print(PersonalAccessTokenCreatedBy.to_json())

# convert the object into a dict
personal_access_token_created_by_dict = personal_access_token_created_by_instance.to_dict()
# create an instance of PersonalAccessTokenCreatedBy from a dict
personal_access_token_created_by_from_dict = PersonalAccessTokenCreatedBy.from_dict(personal_access_token_created_by_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
