# SlackWebHookNotification

## Properties

| Name             | Type    | Description                                                                                                                                            | Notes      |
| ---------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **message_type** | **str** | How &#x60;text&#x60; is read. - &#x60;text&#x60;: plain message text - &#x60;blocks&#x60;: a Slack Block Kit JSON definition                           | [optional] |
| **text**         | **str** | The message, or Block Kit JSON. Event placeholders such as &#x60;[.body.temp]&#x60; aren&#39;t allowed.                                                | [optional] |
| **url**          | **str** | The URL of the Slack webhook. Returned as &#x60;(omitted)&#x60;. Sending it back keeps the stored URL if the monitor has only one Slack webhook route. |

## Example

```python
from notehub_py.models.slack_web_hook_notification import SlackWebHookNotification

# TODO update the JSON string below
json = "{}"
# create an instance of SlackWebHookNotification from a JSON string
slack_web_hook_notification_instance = SlackWebHookNotification.from_json(json)
# print the JSON string representation of the object
print(SlackWebHookNotification.to_json())

# convert the object into a dict
slack_web_hook_notification_dict = slack_web_hook_notification_instance.to_dict()
# create an instance of SlackWebHookNotification from a dict
slack_web_hook_notification_from_dict = SlackWebHookNotification.from_dict(
    slack_web_hook_notification_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
