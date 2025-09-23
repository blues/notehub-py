# UsageRouteLogsResponse

## Properties

| Name     | Type                                                  | Description | Notes |
| -------- | ----------------------------------------------------- | ----------- | ----- |
| **data** | [**List[UsageRouteLogsData]**](UsageRouteLogsData.md) |             |

## Example

```python
from notehub_py.models.usage_route_logs_response import UsageRouteLogsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsageRouteLogsResponse from a JSON string
usage_route_logs_response_instance = UsageRouteLogsResponse.from_json(json)
# print the JSON string representation of the object
print(UsageRouteLogsResponse.to_json())

# convert the object into a dict
usage_route_logs_response_dict = usage_route_logs_response_instance.to_dict()
# create an instance of UsageRouteLogsResponse from a dict
usage_route_logs_response_from_dict = UsageRouteLogsResponse.from_dict(usage_route_logs_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
