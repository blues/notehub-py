# AnalyticsSessionsResponse

## Properties

| Name     | Type                                                        | Description | Notes |
| -------- | ----------------------------------------------------------- | ----------- | ----- |
| **data** | [**List[AnalyticsSessionsData]**](AnalyticsSessionsData.md) |             |

## Example

```python
from notehub_py.models.analytics_sessions_response import AnalyticsSessionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsSessionsResponse from a JSON string
analytics_sessions_response_instance = AnalyticsSessionsResponse.from_json(json)
# print the JSON string representation of the object
print(AnalyticsSessionsResponse.to_json())

# convert the object into a dict
analytics_sessions_response_dict = analytics_sessions_response_instance.to_dict()
# create an instance of AnalyticsSessionsResponse from a dict
analytics_sessions_response_from_dict = AnalyticsSessionsResponse.from_dict(analytics_sessions_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
