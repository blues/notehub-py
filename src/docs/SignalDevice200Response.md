# SignalDevice200Response

## Properties

| Name          | Type     | Description                                   | Notes      |
| ------------- | -------- | --------------------------------------------- | ---------- |
| **connected** | **bool** | true if the Notecard is connected to Notehub. | [optional] |

## Example

```python
from notehub_py.models.signal_device200_response import SignalDevice200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SignalDevice200Response from a JSON string
signal_device200_response_instance = SignalDevice200Response.from_json(json)
# print the JSON string representation of the object
print(SignalDevice200Response.to_json())

# convert the object into a dict
signal_device200_response_dict = signal_device200_response_instance.to_dict()
# create an instance of SignalDevice200Response from a dict
signal_device200_response_from_dict = SignalDevice200Response.from_dict(signal_device200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
