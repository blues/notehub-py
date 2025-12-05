# NoteInput

## Properties

| Name        | Type                  | Description                               | Notes      |
| ----------- | --------------------- | ----------------------------------------- | ---------- |
| **body**    | **Dict[str, object]** | Arbitrary user-defined JSON for the note. | [optional] |
| **payload** | **bytearray**         | Optional base64-encoded payload.          | [optional] |

## Example

```python
from notehub_py.models.note_input import NoteInput

# TODO update the JSON string below
json = "{}"
# create an instance of NoteInput from a JSON string
note_input_instance = NoteInput.from_json(json)
# print the JSON string representation of the object
print(NoteInput.to_json())

# convert the object into a dict
note_input_dict = note_input_instance.to_dict()
# create an instance of NoteInput from a dict
note_input_from_dict = NoteInput.from_dict(note_input_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
