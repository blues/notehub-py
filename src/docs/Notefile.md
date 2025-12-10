# Notefile

## Properties

| Name         | Type                      | Description                                                         | Notes      |
| ------------ | ------------------------- | ------------------------------------------------------------------- | ---------- |
| **id**       | **str**                   | Notefile id (e.g., \&quot;test.qi\&quot;, \&quot;config.db\&quot;). |
| **notes**    | [**List[Note]**](Note.md) |                                                                     |
| **template** | **str**                   |                                                                     | [optional] |

## Example

```python
from notehub_py.models.notefile import Notefile

# TODO update the JSON string below
json = "{}"
# create an instance of Notefile from a JSON string
notefile_instance = Notefile.from_json(json)
# print the JSON string representation of the object
print(Notefile.to_json())

# convert the object into a dict
notefile_dict = notefile_instance.to_dict()
# create an instance of Notefile from a dict
notefile_from_dict = Notefile.from_dict(notefile_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
