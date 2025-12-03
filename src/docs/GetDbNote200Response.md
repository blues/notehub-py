# GetDbNote200Response

## Properties

| Name        | Type       | Description                                            | Notes      |
| ----------- | ---------- | ------------------------------------------------------ | ---------- |
| **body**    | **object** | The note body                                          | [optional] |
| **payload** | **str**    | The note payload                                       | [optional] |
| **time**    | **int**    | The time the Note was added to the Notecard or Notehub | [optional] |

## Example

```python
from notehub_py.models.get_db_note200_response import GetDbNote200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDbNote200Response from a JSON string
get_db_note200_response_instance = GetDbNote200Response.from_json(json)
# print the JSON string representation of the object
print(GetDbNote200Response.to_json())

# convert the object into a dict
get_db_note200_response_dict = get_db_note200_response_instance.to_dict()
# create an instance of GetDbNote200Response from a dict
get_db_note200_response_from_dict = GetDbNote200Response.from_dict(get_db_note200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
