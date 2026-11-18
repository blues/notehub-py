# MonitorAlertRoutesInner

## Properties

| Name             | Type    | Description                                                                                                                                                   | Notes      |
| ---------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **message_type** | **str** | How &#x60;text&#x60; is read. - &#x60;text&#x60;: plain message text - &#x60;blocks&#x60;: a Slack Block Kit JSON definition                                  | [optional] |
| **text**         | **str** | The message, or Block Kit JSON. Event placeholders such as &#x60;[.body.temp]&#x60; aren&#39;t allowed.                                                       | [optional] |
| **url**          | **str** | The URL of the Slack webhook. Returned as &#x60;(omitted)&#x60;. Sending it back keeps the stored URL if the monitor has only one Slack webhook route.        |
| **channel**      | **str** | The channel to send the message to.                                                                                                                           | [optional] |
| **token**        | **str** | The bearer token for the Slack app. Returned as &#x60;(omitted)&#x60;. Sending it back keeps the stored token if the monitor has only one Slack bearer route. |
| **email**        | **str** | Email address, or several separated by commas.                                                                                                                |
| **account_sid**  | **str** | The Twilio account SID.                                                                                                                                       |
| **auth_token**   | **str** | The Twilio auth token. Returned as &#x60;(omitted)&#x60;. Sending it back keeps the stored token if the monitor has only one Twilio route.                    | [optional] |
| **var_from**     | **str** | The number to send the SMS from, in E.164 format, e.g. &#x60;+15551234567&#x60;.                                                                              | [optional] |
| **message**      | **str** | The text of the SMS. Event placeholders such as &#x60;[.body.temp]&#x60; aren&#39;t allowed.                                                                  | [optional] |
| **to**           | **str** | The number to send the SMS to, in E.164 format.                                                                                                               | [optional] |

## Example

```python
from notehub_py.models.monitor_alert_routes_inner import MonitorAlertRoutesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MonitorAlertRoutesInner from a JSON string
monitor_alert_routes_inner_instance = MonitorAlertRoutesInner.from_json(json)
# print the JSON string representation of the object
print(MonitorAlertRoutesInner.to_json())

# convert the object into a dict
monitor_alert_routes_inner_dict = monitor_alert_routes_inner_instance.to_dict()
# create an instance of MonitorAlertRoutesInner from a dict
monitor_alert_routes_inner_from_dict = MonitorAlertRoutesInner.from_dict(
    monitor_alert_routes_inner_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
