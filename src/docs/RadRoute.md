# RadRoute

## Properties

| Name              | Type          | Description | Notes      |
| ----------------- | ------------- | ----------- | ---------- |
| **client_id**     | **str**       |             | [optional] |
| **client_secret** | **str**       |             | [optional] |
| **data_feed_key** | **str**       |             | [optional] |
| **event_id**      | **int**       |             | [optional] |
| **fleets**        | **List[str]** |             | [optional] |
| **test_api**      | **bool**      |             | [optional] |
| **throttle_ms**   | **int**       |             | [optional] |

## Example

```python
from notehub_py.models.rad_route import RadRoute

# TODO update the JSON string below
json = "{}"
# create an instance of RadRoute from a JSON string
rad_route_instance = RadRoute.from_json(json)
# print the JSON string representation of the object
print(RadRoute.to_json())

# convert the object into a dict
rad_route_dict = rad_route_instance.to_dict()
# create an instance of RadRoute from a dict
rad_route_from_dict = RadRoute.from_dict(rad_route_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
