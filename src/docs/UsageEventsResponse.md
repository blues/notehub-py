# UsageEventsResponse

## Properties

| Name          | Type                                            | Description                                                                                                | Notes      |
| ------------- | ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------- |
| **data**      | [**List[UsageEventsData]**](UsageEventsData.md) |                                                                                                            |
| **truncated** | **bool**                                        | True if there were more data points than &#x60;limit&#x60;; only the first &#x60;limit&#x60; are returned. | [optional] |

## Example

```python
from notehub_py.models.usage_events_response import UsageEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsageEventsResponse from a JSON string
usage_events_response_instance = UsageEventsResponse.from_json(json)
# print the JSON string representation of the object
print(UsageEventsResponse.to_json())

# convert the object into a dict
usage_events_response_dict = usage_events_response_instance.to_dict()
# create an instance of UsageEventsResponse from a dict
usage_events_response_from_dict = UsageEventsResponse.from_dict(
    usage_events_response_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
