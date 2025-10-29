# AwsRoute

## Properties

| Name                         | Type                                                    | Description | Notes      |
| ---------------------------- | ------------------------------------------------------- | ----------- | ---------- |
| **access_key_id**            | **str**                                                 |             | [optional] |
| **access_key_secret**        | **str**                                                 |             | [optional] |
| **channel**                  | **str**                                                 |             | [optional] |
| **disable_http_headers**     | **bool**                                                |             | [optional] |
| **filter**                   | [**Filter**](Filter.md)                                 |             | [optional] |
| **fleets**                   | **List[str]**                                           |             | [optional] |
| **http_headers**             | **Dict[str, str]**                                      |             | [optional] |
| **message_deduplication_id** | **str**                                                 |             | [optional] |
| **message_group_id**         | **str**                                                 |             | [optional] |
| **region**                   | **str**                                                 |             | [optional] |
| **throttle_ms**              | **int**                                                 |             | [optional] |
| **timeout**                  | **int**                                                 |             | [optional] |
| **transform**                | [**RouteTransformSettings**](RouteTransformSettings.md) |             | [optional] |
| **url**                      | **str**                                                 |             | [optional] |

## Example

```python
from notehub_py.models.aws_route import AwsRoute

# TODO update the JSON string below
json = "{}"
# create an instance of AwsRoute from a JSON string
aws_route_instance = AwsRoute.from_json(json)
# print the JSON string representation of the object
print(AwsRoute.to_json())

# convert the object into a dict
aws_route_dict = aws_route_instance.to_dict()
# create an instance of AwsRoute from a dict
aws_route_from_dict = AwsRoute.from_dict(aws_route_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
