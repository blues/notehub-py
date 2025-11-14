# GetNotefile200Response

## Properties

| Name        | Type       | Description                                                                                                       | Notes      |
| ----------- | ---------- | ----------------------------------------------------------------------------------------------------------------- | ---------- |
| **changes** | **int**    | The number of pending changes in the Notefile.                                                                    | [optional] |
| **notes**   | **object** | An object with a key for each note and a value object with the body of each Note and the time the Note was added. | [optional] |
| **total**   | **int**    | The total number of notes.                                                                                        | [optional] |

## Example

```python
from notehub_py.models.get_notefile200_response import GetNotefile200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotefile200Response from a JSON string
get_notefile200_response_instance = GetNotefile200Response.from_json(json)
# print the JSON string representation of the object
print(GetNotefile200Response.to_json())

# convert the object into a dict
get_notefile200_response_dict = get_notefile200_response_instance.to_dict()
# create an instance of GetNotefile200Response from a dict
get_notefile200_response_from_dict = GetNotefile200Response.from_dict(get_notefile200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
