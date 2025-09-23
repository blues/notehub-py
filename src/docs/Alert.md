# Alert

## Properties

| Name              | Type                                                            | Description                                  | Notes      |
| ----------------- | --------------------------------------------------------------- | -------------------------------------------- | ---------- |
| **alert_source**  | **str**                                                         | The source of the alert                      | [optional] |
| **created_at**    | **int**                                                         | The time the alert was created               | [optional] |
| **data**          | [**List[AlertDataInner]**](AlertDataInner.md)                   |                                              | [optional] |
| **device_uid**    | **str**                                                         | Device UID                                   | [optional] |
| **field_name**    | **str**                                                         | The field name that triggered the alert      | [optional] |
| **monitor_name**  | **str**                                                         | Monitor Name                                 | [optional] |
| **monitor_type**  | **str**                                                         | The type of monitor that triggered the alert | [optional] |
| **monitor_uid**   | **str**                                                         | Monitor UID                                  | [optional] |
| **notifications** | [**List[AlertNotificationsInner]**](AlertNotificationsInner.md) |                                              | [optional] |
| **resolved**      | **bool**                                                        | If true, the alert has been resolved         | [optional] |
| **source**        | **str**                                                         | The UID of the source of the alert           | [optional] |
| **uid**           | **str**                                                         | Alert UID                                    | [optional] |
| **value**         | **float**                                                       | The value that triggered the alert           | [optional] |
| **version**       | **int**                                                         | The version of the alert                     | [optional] |

## Example

```python
from notehub_py.models.alert import Alert

# TODO update the JSON string below
json = "{}"
# create an instance of Alert from a JSON string
alert_instance = Alert.from_json(json)
# print the JSON string representation of the object
print(Alert.to_json())

# convert the object into a dict
alert_dict = alert_instance.to_dict()
# create an instance of Alert from a dict
alert_from_dict = Alert.from_dict(alert_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
