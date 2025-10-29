# TwilioRoute

## Properties

| Name            | Type                    | Description | Notes      |
| --------------- | ----------------------- | ----------- | ---------- |
| **account_sid** | **str**                 |             | [optional] |
| **auth_token**  | **str**                 |             | [optional] |
| **filter**      | [**Filter**](Filter.md) |             | [optional] |
| **fleets**      | **List[str]**           |             | [optional] |
| **var_from**    | **str**                 |             | [optional] |
| **message**     | **str**                 |             | [optional] |
| **throttle_ms** | **int**                 |             | [optional] |
| **timeout**     | **int**                 |             | [optional] |
| **to**          | **str**                 |             | [optional] |

## Example

```python
from notehub_py.models.twilio_route import TwilioRoute

# TODO update the JSON string below
json = "{}"
# create an instance of TwilioRoute from a JSON string
twilio_route_instance = TwilioRoute.from_json(json)
# print the JSON string representation of the object
print(TwilioRoute.to_json())

# convert the object into a dict
twilio_route_dict = twilio_route_instance.to_dict()
# create an instance of TwilioRoute from a dict
twilio_route_from_dict = TwilioRoute.from_dict(twilio_route_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
