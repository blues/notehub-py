# GetWebhooks200Response

## Properties

| Name         | Type                                            | Description | Notes      |
| ------------ | ----------------------------------------------- | ----------- | ---------- |
| **webhooks** | [**List[WebhookSettings]**](WebhookSettings.md) |             | [optional] |

## Example

```python
from notehub_py.models.get_webhooks200_response import GetWebhooks200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhooks200Response from a JSON string
get_webhooks200_response_instance = GetWebhooks200Response.from_json(json)
# print the JSON string representation of the object
print(GetWebhooks200Response.to_json())

# convert the object into a dict
get_webhooks200_response_dict = get_webhooks200_response_instance.to_dict()
# create an instance of GetWebhooks200Response from a dict
get_webhooks200_response_from_dict = GetWebhooks200Response.from_dict(get_webhooks200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
