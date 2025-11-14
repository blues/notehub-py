# ListPendingNotefiles200Response

## Properties

| Name        | Type       | Description                                                                                                                            | Notes      |
| ----------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **changes** | **int**    | The number of pending changes in the Notefile.                                                                                         | [optional] |
| **info**    | **object** | An object with a key for each Notefile that matched the request parameters, and value object with the changes and total for each file. | [optional] |
| **pending** | **bool**   | Whether there are pending changes.                                                                                                     | [optional] |
| **total**   | **int**    | The total number of files.                                                                                                             | [optional] |

## Example

```python
from notehub_py.models.list_pending_notefiles200_response import ListPendingNotefiles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListPendingNotefiles200Response from a JSON string
list_pending_notefiles200_response_instance = ListPendingNotefiles200Response.from_json(json)
# print the JSON string representation of the object
print(ListPendingNotefiles200Response.to_json())

# convert the object into a dict
list_pending_notefiles200_response_dict = list_pending_notefiles200_response_instance.to_dict()
# create an instance of ListPendingNotefiles200Response from a dict
list_pending_notefiles200_response_from_dict = ListPendingNotefiles200Response.from_dict(list_pending_notefiles200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
