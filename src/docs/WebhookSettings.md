# WebhookSettings

## Properties

| Name          | Type     | Description                                | Notes      |
| ------------- | -------- | ------------------------------------------ | ---------- |
| **disabled**  | **bool** | Flag indicating if the webhook is disabled | [optional] |
| **id**        | **str**  | Webhook ID                                 | [optional] |
| **transform** | **str**  | Transformation to be applied to the event  | [optional] |

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
