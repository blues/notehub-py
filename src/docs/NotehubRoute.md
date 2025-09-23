# NotehubRoute

## Properties

| Name           | Type                                            | Description        | Notes                          |
| -------------- | ----------------------------------------------- | ------------------ | ------------------------------ |
| **disabled**   | **bool**                                        | Is route disabled? | [optional] [default to False]  |
| **label**      | **str**                                         | Route Label        | [optional]                     |
| **modified**   | **str**                                         | Last Modified      | [optional]                     |
| **route_type** | **str**                                         | Type of route.     | [optional] [default to 'http'] |
| **var_schema** | [**NotehubRouteSchema**](NotehubRouteSchema.md) |                    | [optional]                     |
| **uid**        | **str**                                         | Route UID          | [optional]                     |

## Example

```python
from notehub_py.models.notehub_route import NotehubRoute

# TODO update the JSON string below
json = "{}"
# create an instance of NotehubRoute from a JSON string
notehub_route_instance = NotehubRoute.from_json(json)
# print the JSON string representation of the object
print(NotehubRoute.to_json())

# convert the object into a dict
notehub_route_dict = notehub_route_instance.to_dict()
# create an instance of NotehubRoute from a dict
notehub_route_from_dict = NotehubRoute.from_dict(notehub_route_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
