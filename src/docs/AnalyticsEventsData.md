# AnalyticsEventsData

## Properties

| Name                | Type         | Description | Notes |
| ------------------- | ------------ | ----------- | ----- |
| **period**          | **datetime** |             |
| **events**          | **int**      |             |
| **platform_events** | **int**      |             |

## Example

```python
from notehub_py.models.analytics_events_data import AnalyticsEventsData

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsEventsData from a JSON string
analytics_events_data_instance = AnalyticsEventsData.from_json(json)
# print the JSON string representation of the object
print(AnalyticsEventsData.to_json())

# convert the object into a dict
analytics_events_data_dict = analytics_events_data_instance.to_dict()
# create an instance of AnalyticsEventsData from a dict
analytics_events_data_from_dict = AnalyticsEventsData.from_dict(analytics_events_data_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
