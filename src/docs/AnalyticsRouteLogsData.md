# AnalyticsRouteLogsData

## Properties

| Name                  | Type         | Description | Notes |
| --------------------- | ------------ | ----------- | ----- |
| **period**            | **datetime** |             |
| **successful_routes** | **int**      |             |
| **failed_routes**     | **int**      |             |
| **total_routes**      | **int**      |             |

## Example

```python
from notehub_py.models.analytics_route_logs_data import AnalyticsRouteLogsData

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsRouteLogsData from a JSON string
analytics_route_logs_data_instance = AnalyticsRouteLogsData.from_json(json)
# print the JSON string representation of the object
print(AnalyticsRouteLogsData.to_json())

# convert the object into a dict
analytics_route_logs_data_dict = analytics_route_logs_data_instance.to_dict()
# create an instance of AnalyticsRouteLogsData from a dict
analytics_route_logs_data_from_dict = AnalyticsRouteLogsData.from_dict(analytics_route_logs_data_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
