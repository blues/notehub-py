# RouteLog

## Properties

| Name          | Type     | Description                                                     | Notes      |
| ------------- | -------- | --------------------------------------------------------------- | ---------- |
| **attn**      | **bool** | True if the attempt failed.                                     | [optional] |
| **var_date**  | **str**  | When the attempt was made, in RFC 3339 format.                  | [optional] |
| **duration**  | **int**  | How long the attempt took, in milliseconds.                     | [optional] |
| **event_uid** | **str**  | EventUID of the event that was sent.                            | [optional] |
| **route_uid** | **str**  | RouteUID of the route.                                          | [optional] |
| **status**    | **str**  | The destination&#39;s response status, such as &#x60;200&#x60;. | [optional] |
| **text**      | **str**  | The destination&#39;s response body, or an error message.       | [optional] |
| **url**       | **str**  | The URL the event was sent to.                                  | [optional] |

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
