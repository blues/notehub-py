# Note

## Properties

| Name        | Type                  | Description                                                              | Notes      |
| ----------- | --------------------- | ------------------------------------------------------------------------ | ---------- |
| **body**    | **Dict[str, object]** | Arbitrary user-defined JSON for the note.                                |
| **edge**    | **bool**              | True if originated from an edge source.                                  | [optional] |
| **id**      | **str**               | Note name/identifier (e.g., \&quot;1:435\&quot;, \&quot;my_note\&quot;). |
| **payload** | **bytearray**         | Optional base64-encoded payload.                                         | [optional] |
| **pending** | **bool**              | True if the note is pending delivery or processing.                      | [optional] |
| **time**    | **int**               | Unix epoch seconds.                                                      |
| **where**   | **str**               | Optional location/metadata string.                                       | [optional] |

## Example

```python
from notehub_py.models.note import Note

# TODO update the JSON string below
json = "{}"
# create an instance of Note from a JSON string
note_instance = Note.from_json(json)
# print the JSON string representation of the object
print(Note.to_json())

# convert the object into a dict
note_dict = note_instance.to_dict()
# create an instance of Note from a dict
note_from_dict = Note.from_dict(note_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
