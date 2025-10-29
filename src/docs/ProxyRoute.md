# ProxyRoute

## Properties

| Name             | Type                                                    | Description | Notes      |
| ---------------- | ------------------------------------------------------- | ----------- | ---------- |
| **alias**        | **str**                                                 |             | [optional] |
| **fleets**       | **List[str]**                                           |             | [optional] |
| **http_headers** | **Dict[str, str]**                                      |             | [optional] |
| **timeout**      | **int**                                                 |             | [optional] |
| **transform**    | [**RouteTransformSettings**](RouteTransformSettings.md) |             | [optional] |
| **url**          | **str**                                                 |             | [optional] |

## Example

```python
from notehub_py.models.proxy_route import ProxyRoute

# TODO update the JSON string below
json = "{}"
# create an instance of ProxyRoute from a JSON string
proxy_route_instance = ProxyRoute.from_json(json)
# print the JSON string representation of the object
print(ProxyRoute.to_json())

# convert the object into a dict
proxy_route_dict = proxy_route_instance.to_dict()
# create an instance of ProxyRoute from a dict
proxy_route_from_dict = ProxyRoute.from_dict(proxy_route_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
