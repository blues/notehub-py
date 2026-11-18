# SlackBearerNotification

## Properties

| Name             | Type    | Description                                                                                                                                                   | Notes      |
| ---------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **channel**      | **str** | The channel to send the message to.                                                                                                                           | [optional] |
| **message_type** | **str** | How &#x60;text&#x60; is read. - &#x60;text&#x60;: plain message text - &#x60;blocks&#x60;: a Slack Block Kit JSON definition                                  | [optional] |
| **text**         | **str** | The message, or Block Kit JSON. Event placeholders such as &#x60;[.body.temp]&#x60; aren&#39;t allowed.                                                       | [optional] |
| **token**        | **str** | The bearer token for the Slack app. Returned as &#x60;(omitted)&#x60;. Sending it back keeps the stored token if the monitor has only one Slack bearer route. |

## Example

```python
from notehub_py.models.slack_bearer_notification import SlackBearerNotification

# TODO update the JSON string below
json = "{}"
# create an instance of SlackBearerNotification from a JSON string
slack_bearer_notification_instance = SlackBearerNotification.from_json(json)
# print the JSON string representation of the object
print(SlackBearerNotification.to_json())

# convert the object into a dict
slack_bearer_notification_dict = slack_bearer_notification_instance.to_dict()
# create an instance of SlackBearerNotification from a dict
slack_bearer_notification_from_dict = SlackBearerNotification.from_dict(
    slack_bearer_notification_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
