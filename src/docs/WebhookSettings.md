# WebhookSettings

## Properties

| Name          | Type     | Description                                                                                                                                                                     | Notes      |
| ------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **disabled**  | **bool** | If true, posts to the webhook return an error and create no events.                                                                                                             | [optional] |
| **id**        | **str**  | Webhook ID, also the default notefile name (&#x60;&lt;id&gt;.qo&#x60;). Letters, digits, &#x60;-&#x60; and &#x60;\_&#x60;.                                                      | [optional] |
| **transform** | **str**  | JSONata expression applied to the event, with the post under &#x60;body&#x60;. Its output replaces the event and must set &#x60;body&#x60;. &#x60;$doNotRoute()&#x60; drops it. | [optional] |

## Example

```python
from notehub_py.models.webhook_settings import WebhookSettings

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSettings from a JSON string
webhook_settings_instance = WebhookSettings.from_json(json)
# print the JSON string representation of the object
print(WebhookSettings.to_json())

# convert the object into a dict
webhook_settings_dict = webhook_settings_instance.to_dict()
# create an instance of WebhookSettings from a dict
webhook_settings_from_dict = WebhookSettings.from_dict(webhook_settings_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
