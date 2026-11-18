# AlertNotificationsInner

## Properties

| Name                  | Type      | Description                                                                                                                                                                                                                    | Notes      |
| --------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **notification_type** | **str**   | How the notification was sent. - &#x60;email&#x60;: by email - &#x60;slack-webhook&#x60;: to a Slack webhook - &#x60;slack-bearer&#x60;: through a Slack app, with a bearer token - &#x60;twilio&#x60;: by SMS, through Twilio | [optional] |
| **recipients**        | **str**   | The recipients of the notification                                                                                                                                                                                             | [optional] |
| **status**            | **float** | The status of the notification                                                                                                                                                                                                 | [optional] |

## Example

```python
from notehub_py.models.alert_notifications_inner import AlertNotificationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AlertNotificationsInner from a JSON string
alert_notifications_inner_instance = AlertNotificationsInner.from_json(json)
# print the JSON string representation of the object
print(AlertNotificationsInner.to_json())

# convert the object into a dict
alert_notifications_inner_dict = alert_notifications_inner_instance.to_dict()
# create an instance of AlertNotificationsInner from a dict
alert_notifications_inner_from_dict = AlertNotificationsInner.from_dict(
    alert_notifications_inner_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
