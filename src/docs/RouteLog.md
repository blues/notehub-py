# RouteLog

## Properties

| Name          | Type     | Description                                 | Notes      |
| ------------- | -------- | ------------------------------------------- | ---------- |
| **attn**      | **bool** | If true, an error was returned when routing | [optional] |
| **var_date**  | **str**  | The date of the logs.                       | [optional] |
| **duration**  | **int**  | The duration of the route in milliseconds   | [optional] |
| **event_uid** | **str**  | The event UID.                              | [optional] |
| **route_uid** | **str**  | The route UID.                              | [optional] |
| **status**    | **str**  | The status of the event.                    | [optional] |
| **text**      | **str**  | The response body of the route.             | [optional] |
| **url**       | **str**  | The URL of the route.                       | [optional] |

## Example

```python
from notehub_py.models.route_log import RouteLog

# TODO update the JSON string below
json = "{}"
# create an instance of RouteLog from a JSON string
route_log_instance = RouteLog.from_json(json)
# print the JSON string representation of the object
print(RouteLog.to_json())

# convert the object into a dict
route_log_dict = route_log_instance.to_dict()
# create an instance of RouteLog from a dict
route_log_from_dict = RouteLog.from_dict(route_log_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
