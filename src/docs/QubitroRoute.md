# QubitroRoute

## Properties

| Name                    | Type                                                    | Description | Notes      |
| ----------------------- | ------------------------------------------------------- | ----------- | ---------- |
| **filter**              | [**Filter**](Filter.md)                                 |             | [optional] |
| **fleets**              | **List[str]**                                           |             | [optional] |
| **project_id**          | **str**                                                 |             | [optional] |
| **throttle_ms**         | **int**                                                 |             | [optional] |
| **timeout**             | **int**                                                 |             | [optional] |
| **transform**           | [**RouteTransformSettings**](RouteTransformSettings.md) |             | [optional] |
| **webhook_signing_key** | **str**                                                 |             | [optional] |

## Example

```python
from notehub_py.models.qubitro_route import QubitroRoute

# TODO update the JSON string below
json = "{}"
# create an instance of QubitroRoute from a JSON string
qubitro_route_instance = QubitroRoute.from_json(json)
# print the JSON string representation of the object
print(QubitroRoute.to_json())

# convert the object into a dict
qubitro_route_dict = qubitro_route_instance.to_dict()
# create an instance of QubitroRoute from a dict
qubitro_route_from_dict = QubitroRoute.from_dict(qubitro_route_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
