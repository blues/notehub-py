# GoogleRoute

## Properties

| Name            | Type                                                    | Description | Notes      |
| --------------- | ------------------------------------------------------- | ----------- | ---------- |
| **filter**      | [**Filter**](Filter.md)                                 |             | [optional] |
| **fleets**      | **List[str]**                                           |             | [optional] |
| **throttle_ms** | **int**                                                 |             | [optional] |
| **timeout**     | **int**                                                 |             | [optional] |
| **token**       | **str**                                                 |             | [optional] |
| **transform**   | [**RouteTransformSettings**](RouteTransformSettings.md) |             | [optional] |
| **url**         | **str**                                                 |             | [optional] |

## Example

```python
from notehub_py.models.google_route import GoogleRoute

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleRoute from a JSON string
google_route_instance = GoogleRoute.from_json(json)
# print the JSON string representation of the object
print(GoogleRoute.to_json())

# convert the object into a dict
google_route_dict = google_route_instance.to_dict()
# create an instance of GoogleRoute from a dict
google_route_from_dict = GoogleRoute.from_dict(google_route_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
