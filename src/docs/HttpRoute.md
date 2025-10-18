# HttpRoute

## Properties

| Name                     | Type                                                    | Description                                      | Notes      |
| ------------------------ | ------------------------------------------------------- | ------------------------------------------------ | ---------- |
| **disable_http_headers** | **bool**                                                |                                                  | [optional] |
| **filter**               | [**Filter**](Filter.md)                                 |                                                  | [optional] |
| **fleets**               | **List[str]**                                           | If non-empty, applies only to the listed fleets. | [optional] |
| **http_headers**         | **Dict[str, str]**                                      |                                                  | [optional] |
| **throttle_ms**          | **int**                                                 |                                                  | [optional] |
| **timeout**              | **int**                                                 |                                                  | [optional] |
| **transform**            | [**RouteTransformSettings**](RouteTransformSettings.md) |                                                  | [optional] |
| **url**                  | **str**                                                 |                                                  | [optional] |

## Example

```python
from notehub_py.models.http_route import HttpRoute

# TODO update the JSON string below
json = "{}"
# create an instance of HttpRoute from a JSON string
http_route_instance = HttpRoute.from_json(json)
# print the JSON string representation of the object
print(HttpRoute.to_json())

# convert the object into a dict
http_route_dict = http_route_instance.to_dict()
# create an instance of HttpRoute from a dict
http_route_from_dict = HttpRoute.from_dict(http_route_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
