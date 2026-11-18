# NotefileSchema

## Properties

| Name           | Type                                          | Description                                                                                                                                        | Notes |
| -------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **notefile**   | **str**                                       | Notefile name, e.g. &#x60;sensors.qo&#x60;.                                                                                                        |
| **properties** | [**List[SchemaProperty]**](SchemaProperty.md) | Fields seen in this Notefile&#39;s event &#x60;body&#x60;. Event envelope fields such as &#x60;when&#x60; and &#x60;device&#x60; are not included. |

## Example

```python
from notehub_py.models.notefile_schema import NotefileSchema

# TODO update the JSON string below
json = "{}"
# create an instance of NotefileSchema from a JSON string
notefile_schema_instance = NotefileSchema.from_json(json)
# print the JSON string representation of the object
print(NotefileSchema.to_json())

# convert the object into a dict
notefile_schema_dict = notefile_schema_instance.to_dict()
# create an instance of NotefileSchema from a dict
notefile_schema_from_dict = NotefileSchema.from_dict(notefile_schema_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
