# TwilioNotification

## Properties

| Name            | Type    | Description                                                                                                                                | Notes      |
| --------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **account_sid** | **str** | The Twilio account SID.                                                                                                                    |
| **auth_token**  | **str** | The Twilio auth token. Returned as &#x60;(omitted)&#x60;. Sending it back keeps the stored token if the monitor has only one Twilio route. | [optional] |
| **var_from**    | **str** | The number to send the SMS from, in E.164 format, e.g. &#x60;+15551234567&#x60;.                                                           | [optional] |
| **message**     | **str** | The text of the SMS. Event placeholders such as &#x60;[.body.temp]&#x60; aren&#39;t allowed.                                               | [optional] |
| **to**          | **str** | The number to send the SMS to, in E.164 format.                                                                                            | [optional] |

## Example

```python
from notehub_py.models.twilio_notification import TwilioNotification

# TODO update the JSON string below
json = "{}"
# create an instance of TwilioNotification from a JSON string
twilio_notification_instance = TwilioNotification.from_json(json)
# print the JSON string representation of the object
print(TwilioNotification.to_json())

# convert the object into a dict
twilio_notification_dict = twilio_notification_instance.to_dict()
# create an instance of TwilioNotification from a dict
twilio_notification_from_dict = TwilioNotification.from_dict(twilio_notification_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
