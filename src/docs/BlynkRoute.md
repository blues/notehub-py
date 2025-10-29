# BlynkRoute

## Properties

| Name            | Type                                                    | Description | Notes      |
| --------------- | ------------------------------------------------------- | ----------- | ---------- |
| **filter**      | [**Filter**](Filter.md)                                 |             | [optional] |
| **fleets**      | **List[str]**                                           |             | [optional] |
| **region**      | **str**                                                 |             | [optional] |
| **throttle_ms** | **int**                                                 |             | [optional] |
| **timeout**     | **int**                                                 |             | [optional] |
| **transform**   | [**RouteTransformSettings**](RouteTransformSettings.md) |             | [optional] |

## Example

```python
from notehub_py.models.blynk_route import BlynkRoute

# TODO update the JSON string below
json = "{}"
# create an instance of BlynkRoute from a JSON string
blynk_route_instance = BlynkRoute.from_json(json)
# print the JSON string representation of the object
print(BlynkRoute.to_json())

# convert the object into a dict
blynk_route_dict = blynk_route_instance.to_dict()
# create an instance of BlynkRoute from a dict
blynk_route_from_dict = BlynkRoute.from_dict(blynk_route_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
