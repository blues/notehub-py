# GetRouteLogsUsage200Response

## Properties

| Name           | Type                                                  | Description | Notes |
| -------------- | ----------------------------------------------------- | ----------- | ----- |
| **route_logs** | [**List[UsageRouteLogsData]**](UsageRouteLogsData.md) |             |

## Example

```python
from notehub_py.models.get_route_logs_usage200_response import GetRouteLogsUsage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRouteLogsUsage200Response from a JSON string
get_route_logs_usage200_response_instance = GetRouteLogsUsage200Response.from_json(json)
# print the JSON string representation of the object
print(GetRouteLogsUsage200Response.to_json())

# convert the object into a dict
get_route_logs_usage200_response_dict = get_route_logs_usage200_response_instance.to_dict()
# create an instance of GetRouteLogsUsage200Response from a dict
get_route_logs_usage200_response_from_dict = GetRouteLogsUsage200Response.from_dict(get_route_logs_usage200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
