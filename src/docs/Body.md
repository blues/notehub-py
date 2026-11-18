# Body

## Properties

| Name     | Type       | Description                                                                                                   | Notes      |
| -------- | ---------- | ------------------------------------------------------------------------------------------------------------- | ---------- |
| **body** | **object** | The JSON object to send to the Notecard. Must not have a &#x60;type&#x60; field, which the Notecard reserves. | [optional] |

## Example

```python
from notehub_py.models.body import Body

# TODO update the JSON string below
json = "{}"
# create an instance of Body from a JSON string
body_instance = Body.from_json(json)
# print the JSON string representation of the object
print(Body.to_json())

# convert the object into a dict
body_dict = body_instance.to_dict()
# create an instance of Body from a dict
body_from_dict = Body.from_dict(body_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
