# AnalyticsSessionsData

## Properties

| Name               | Type         | Description | Notes |
| ------------------ | ------------ | ----------- | ----- |
| **period**         | **datetime** |             |
| **sessions**       | **int**      |             |
| **unique_devices** | **int**      |             |
| **total_bytes**    | **int**      |             |

## Example

```python
from notehub_py.models.analytics_sessions_data import AnalyticsSessionsData

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsSessionsData from a JSON string
analytics_sessions_data_instance = AnalyticsSessionsData.from_json(json)
# print the JSON string representation of the object
print(AnalyticsSessionsData.to_json())

# convert the object into a dict
analytics_sessions_data_dict = analytics_sessions_data_instance.to_dict()
# create an instance of AnalyticsSessionsData from a dict
analytics_sessions_data_from_dict = AnalyticsSessionsData.from_dict(analytics_sessions_data_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
