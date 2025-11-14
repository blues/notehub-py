# DeleteNotefilesRequest

## Properties

| Name      | Type          | Description                 | Notes      |
| --------- | ------------- | --------------------------- | ---------- |
| **files** | **List[str]** | Name of notefiles to delete | [optional] |

## Example

```python
from notehub_py.models.delete_notefiles_request import DeleteNotefilesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteNotefilesRequest from a JSON string
delete_notefiles_request_instance = DeleteNotefilesRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteNotefilesRequest.to_json())

# convert the object into a dict
delete_notefiles_request_dict = delete_notefiles_request_instance.to_dict()
# create an instance of DeleteNotefilesRequest from a dict
delete_notefiles_request_from_dict = DeleteNotefilesRequest.from_dict(delete_notefiles_request_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
