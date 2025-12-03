# GetEventsByCursor200Response

## Properties

| Name            | Type                        | Description                                                                                                                                                                                                                     | Notes |
| --------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **events**      | [**List[Event]**](Event.md) |                                                                                                                                                                                                                                 |
| **has_more**    | **bool**                    | True if there are more events                                                                                                                                                                                                   |
| **next_cursor** | **str**                     | The cursor value of the next result, which is intended to be used as the \&quot;cursor\&quot; parameter value of the next call to this method. An empty string is returned if there are no more results after this results set. |

## Example

```python
from notehub_py.models.get_events_by_cursor200_response import GetEventsByCursor200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventsByCursor200Response from a JSON string
get_events_by_cursor200_response_instance = GetEventsByCursor200Response.from_json(json)
# print the JSON string representation of the object
print(GetEventsByCursor200Response.to_json())

# convert the object into a dict
get_events_by_cursor200_response_dict = get_events_by_cursor200_response_instance.to_dict()
# create an instance of GetEventsByCursor200Response from a dict
get_events_by_cursor200_response_from_dict = GetEventsByCursor200Response.from_dict(get_events_by_cursor200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
