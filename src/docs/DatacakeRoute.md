# DatacakeRoute

## Properties

| Name                     | Type                                                    | Description | Notes      |
| ------------------------ | ------------------------------------------------------- | ----------- | ---------- |
| **disable_http_headers** | **bool**                                                |             | [optional] |
| **filter**               | [**Filter**](Filter.md)                                 |             | [optional] |
| **fleets**               | **List[str]**                                           |             | [optional] |
| **http_headers**         | **Dict[str, str]**                                      |             | [optional] |
| **throttle_ms**          | **int**                                                 |             | [optional] |
| **timeout**              | **int**                                                 |             | [optional] |
| **transform**            | [**RouteTransformSettings**](RouteTransformSettings.md) |             | [optional] |
| **url**                  | **str**                                                 |             | [optional] |

## Example

```python
from notehub_py.models.datacake_route import DatacakeRoute

# TODO update the JSON string below
json = "{}"
# create an instance of DatacakeRoute from a JSON string
datacake_route_instance = DatacakeRoute.from_json(json)
# print the JSON string representation of the object
print(DatacakeRoute.to_json())

# convert the object into a dict
datacake_route_dict = datacake_route_instance.to_dict()
# create an instance of DatacakeRoute from a dict
datacake_route_from_dict = DatacakeRoute.from_dict(datacake_route_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
