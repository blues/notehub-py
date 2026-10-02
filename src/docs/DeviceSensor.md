# DeviceSensor

A sensor attached to a device

## Properties

| Name                   | Type         | Description                                                         | Notes      |
| ---------------------- | ------------ | ------------------------------------------------------------------- | ---------- |
| **last_activity_date** | **datetime** | UTC midnight of the most recent day on which this sensor was active | [optional] |
| **sensor_uid**         | **str**      | Unique identifier of the sensor                                     |

## Example

```python
from notehub_py.models.device_sensor import DeviceSensor

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceSensor from a JSON string
device_sensor_instance = DeviceSensor.from_json(json)
# print the JSON string representation of the object
print(DeviceSensor.to_json())

# convert the object into a dict
device_sensor_dict = device_sensor_instance.to_dict()
# create an instance of DeviceSensor from a dict
device_sensor_from_dict = DeviceSensor.from_dict(device_sensor_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
