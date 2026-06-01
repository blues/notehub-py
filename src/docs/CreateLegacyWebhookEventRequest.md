# CreateLegacyWebhookEventRequest

## Properties

| Name        | Type                  | Description                                        | Notes      |
| ----------- | --------------------- | -------------------------------------------------- | ---------- |
| **body**    | **Dict[str, object]** | Arbitrary JSON event body.                         | [optional] |
| **file**    | **str**               | The notefile to which the event should be written. | [optional] |
| **payload** | **str**               | Optional base64-encoded binary payload.            | [optional] |

## Example

```python
from notehub_py.models.create_legacy_webhook_event_request import (
    CreateLegacyWebhookEventRequest,
)

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLegacyWebhookEventRequest from a JSON string
create_legacy_webhook_event_request_instance = (
    CreateLegacyWebhookEventRequest.from_json(json)
)
# print the JSON string representation of the object
print(CreateLegacyWebhookEventRequest.to_json())

# convert the object into a dict
create_legacy_webhook_event_request_dict = (
    create_legacy_webhook_event_request_instance.to_dict()
)
# create an instance of CreateLegacyWebhookEventRequest from a dict
create_legacy_webhook_event_request_from_dict = (
    CreateLegacyWebhookEventRequest.from_dict(create_legacy_webhook_event_request_dict)
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
