# GetEvents200Response

## Properties

| Name         | Type                        | Description                        | Notes      |
| ------------ | --------------------------- | ---------------------------------- | ---------- |
| **events**   | [**List[Event]**](Event.md) |                                    |
| **has_more** | **bool**                    | True if there are more events      |
| **through**  | **str**                     | The UID of the last event returned | [optional] |

## Example

```python
from notehub_py.models.get_events200_response import GetEvents200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEvents200Response from a JSON string
get_events200_response_instance = GetEvents200Response.from_json(json)
# print the JSON string representation of the object
print(GetEvents200Response.to_json())

# convert the object into a dict
get_events200_response_dict = get_events200_response_instance.to_dict()
# create an instance of GetEvents200Response from a dict
get_events200_response_from_dict = GetEvents200Response.from_dict(get_events200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
