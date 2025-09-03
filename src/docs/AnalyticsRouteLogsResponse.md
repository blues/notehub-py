# AnalyticsRouteLogsResponse

## Properties

| Name     | Type                                                          | Description | Notes |
| -------- | ------------------------------------------------------------- | ----------- | ----- |
| **data** | [**List[AnalyticsRouteLogsData]**](AnalyticsRouteLogsData.md) |             |

## Example

```python
from notehub_py.models.analytics_route_logs_response import AnalyticsRouteLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsRouteLogsResponse from a JSON string
analytics_route_logs_response_instance = AnalyticsRouteLogsResponse.from_json(json)
# print the JSON string representation of the object
print(AnalyticsRouteLogsResponse.to_json())

# convert the object into a dict
analytics_route_logs_response_dict = analytics_route_logs_response_instance.to_dict()
# create an instance of AnalyticsRouteLogsResponse from a dict
analytics_route_logs_response_from_dict = AnalyticsRouteLogsResponse.from_dict(analytics_route_logs_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
