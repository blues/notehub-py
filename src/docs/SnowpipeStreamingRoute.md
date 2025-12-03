# SnowpipeStreamingRoute

## Properties

| Name                  | Type                                                    | Description | Notes      |
| --------------------- | ------------------------------------------------------- | ----------- | ---------- |
| **account_name**      | **str**                                                 |             | [optional] |
| **database_name**     | **str**                                                 |             | [optional] |
| **filter**            | [**Filter**](Filter.md)                                 |             | [optional] |
| **fleets**            | **List[str]**                                           |             | [optional] |
| **organization_name** | **str**                                                 |             | [optional] |
| **pem**               | **str**                                                 |             | [optional] |
| **pipe_name**         | **str**                                                 |             | [optional] |
| **private_key_name**  | **str**                                                 |             | [optional] |
| **schema_name**       | **str**                                                 |             | [optional] |
| **timeout**           | **int**                                                 |             | [optional] |
| **transform**         | [**RouteTransformSettings**](RouteTransformSettings.md) |             | [optional] |
| **user_name**         | **str**                                                 |             | [optional] |

## Example

```python
from notehub_py.models.snowpipe_streaming_route import SnowpipeStreamingRoute

# TODO update the JSON string below
json = "{}"
# create an instance of SnowpipeStreamingRoute from a JSON string
snowpipe_streaming_route_instance = SnowpipeStreamingRoute.from_json(json)
# print the JSON string representation of the object
print(SnowpipeStreamingRoute.to_json())

# convert the object into a dict
snowpipe_streaming_route_dict = snowpipe_streaming_route_instance.to_dict()
# create an instance of SnowpipeStreamingRoute from a dict
snowpipe_streaming_route_from_dict = SnowpipeStreamingRoute.from_dict(snowpipe_streaming_route_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
