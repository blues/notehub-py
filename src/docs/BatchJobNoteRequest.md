# BatchJobNoteRequest

A single note.add/note.update/note.delete request against a device's own notefile

## Properties

| Name     | Type                  | Description                                                                                                                                                                      | Notes      |
| -------- | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **body** | **Dict[str, object]** | The note&#39;s JSON body (used by note.add and note.update)                                                                                                                      | [optional] |
| **file** | **str**               | The notefile to operate on (e.g. data.qi, config.dbs)                                                                                                                            |
| **note** | **str**               | The note ID. Required for note.update and note.delete, and for note.add against a database (.dbs/.db) notefile. Must be omitted for note.add against a queue (.qi/.qo) notefile. | [optional] |
| **req**  | **str**               | The note operation to perform                                                                                                                                                    |

## Example

```python
from notehub_py.models.batch_job_note_request import BatchJobNoteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BatchJobNoteRequest from a JSON string
batch_job_note_request_instance = BatchJobNoteRequest.from_json(json)
# print the JSON string representation of the object
print(BatchJobNoteRequest.to_json())

# convert the object into a dict
batch_job_note_request_dict = batch_job_note_request_instance.to_dict()
# create an instance of BatchJobNoteRequest from a dict
batch_job_note_request_from_dict = BatchJobNoteRequest.from_dict(
    batch_job_note_request_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
