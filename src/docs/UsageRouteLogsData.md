# UsageRouteLogsData

## Properties

| Name                  | Type         | Description                                                              | Notes      |
| --------------------- | ------------ | ------------------------------------------------------------------------ | ---------- |
| **failed_routes**     | **int**      |                                                                          |
| **period**            | **datetime** |                                                                          |
| **route**             | **str**      | The route serial number (only present when aggregate is &#39;route&#39;) | [optional] |
| **successful_routes** | **int**      |                                                                          |
| **total_routes**      | **int**      |                                                                          |

## Example

```python
from notehub_py.models.usage_route_logs_data import UsageRouteLogsData

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRouteLogsData from a JSON string
usage_route_logs_data_instance = UsageRouteLogsData.from_json(json)
# print the JSON string representation of the object
print(UsageRouteLogsData.to_json())

# convert the object into a dict
usage_route_logs_data_dict = usage_route_logs_data_instance.to_dict()
# create an instance of UsageRouteLogsData from a dict
usage_route_logs_data_from_dict = UsageRouteLogsData.from_dict(usage_route_logs_data_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
