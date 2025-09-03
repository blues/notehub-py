# AnalyticsEventsResponse

## Properties

| Name     | Type                                                    | Description | Notes |
| -------- | ------------------------------------------------------- | ----------- | ----- |
| **data** | [**List[AnalyticsEventsData]**](AnalyticsEventsData.md) |             |

## Example

```python
from notehub_py.models.analytics_events_response import AnalyticsEventsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsEventsResponse from a JSON string
analytics_events_response_instance = AnalyticsEventsResponse.from_json(json)
# print the JSON string representation of the object
print(AnalyticsEventsResponse.to_json())

# convert the object into a dict
analytics_events_response_dict = analytics_events_response_instance.to_dict()
# create an instance of AnalyticsEventsResponse from a dict
analytics_events_response_from_dict = AnalyticsEventsResponse.from_dict(analytics_events_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
