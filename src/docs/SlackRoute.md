# SlackRoute

## Properties

| Name            | Type                                                    | Description | Notes      |
| --------------- | ------------------------------------------------------- | ----------- | ---------- |
| **bearer**      | **str**                                                 |             | [optional] |
| **blocks**      | **str**                                                 |             | [optional] |
| **channel**     | **str**                                                 |             | [optional] |
| **filter**      | [**Filter**](Filter.md)                                 |             | [optional] |
| **fleets**      | **List[str]**                                           |             | [optional] |
| **text**        | **str**                                                 |             | [optional] |
| **throttle_ms** | **int**                                                 |             | [optional] |
| **timeout**     | **int**                                                 |             | [optional] |
| **transform**   | [**RouteTransformSettings**](RouteTransformSettings.md) |             | [optional] |
| **webhook_url** | **str**                                                 |             | [optional] |

## Example

```python
from notehub_py.models.slack_route import SlackRoute

# TODO update the JSON string below
json = "{}"
# create an instance of SlackRoute from a JSON string
slack_route_instance = SlackRoute.from_json(json)
# print the JSON string representation of the object
print(SlackRoute.to_json())

# convert the object into a dict
slack_route_dict = slack_route_instance.to_dict()
# create an instance of SlackRoute from a dict
slack_route_from_dict = SlackRoute.from_dict(slack_route_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
