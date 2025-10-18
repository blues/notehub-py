# MqttRoute

## Properties

| Name                 | Type                                                    | Description | Notes      |
| -------------------- | ------------------------------------------------------- | ----------- | ---------- |
| **broker**           | **str**                                                 |             | [optional] |
| **certificate**      | **str**                                                 |             | [optional] |
| **certificate_name** | **str**                                                 |             | [optional] |
| **filter**           | [**Filter**](Filter.md)                                 |             | [optional] |
| **fleets**           | **List[str]**                                           |             | [optional] |
| **key**              | **str**                                                 |             | [optional] |
| **password**         | **str**                                                 |             | [optional] |
| **port**             | **str**                                                 |             | [optional] |
| **private_key_name** | **str**                                                 |             | [optional] |
| **throttle_ms**      | **int**                                                 |             | [optional] |
| **timeout**          | **int**                                                 |             | [optional] |
| **topic**            | **str**                                                 |             | [optional] |
| **transform**        | [**RouteTransformSettings**](RouteTransformSettings.md) |             | [optional] |
| **username**         | **str**                                                 |             | [optional] |

## Example

```python
from notehub_py.models.mqtt_route import MqttRoute

# TODO update the JSON string below
json = "{}"
# create an instance of MqttRoute from a JSON string
mqtt_route_instance = MqttRoute.from_json(json)
# print the JSON string representation of the object
print(MqttRoute.to_json())

# convert the object into a dict
mqtt_route_dict = mqtt_route_instance.to_dict()
# create an instance of MqttRoute from a dict
mqtt_route_from_dict = MqttRoute.from_dict(mqtt_route_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
