# OAuth2Error

## Properties

| Name                  | Type    | Description                              | Notes      |
| --------------------- | ------- | ---------------------------------------- | ---------- |
| **error**             | **str** | RFC 6749 error code.                     |
| **error_description** | **str** | Human-readable explanation of the error. | [optional] |

## Example

```python
from notehub_py.models.o_auth2_error import OAuth2Error

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Error from a JSON string
o_auth2_error_instance = OAuth2Error.from_json(json)
# print the JSON string representation of the object
print(OAuth2Error.to_json())

# convert the object into a dict
o_auth2_error_dict = o_auth2_error_instance.to_dict()
# create an instance of OAuth2Error from a dict
o_auth2_error_from_dict = OAuth2Error.from_dict(o_auth2_error_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
