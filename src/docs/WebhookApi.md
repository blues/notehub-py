# notehub_py.WebhookApi

All URIs are relative to *https://api.notefile.net*

| Method                                             | HTTP request                                                        | Description |
| -------------------------------------------------- | ------------------------------------------------------------------- | ----------- |
| [**create_webhook**](WebhookApi.md#create_webhook) | **POST** /v1/projects/{projectOrProductUID}/webhooks/{webhookUID}   |
| [**delete_webhook**](WebhookApi.md#delete_webhook) | **DELETE** /v1/projects/{projectOrProductUID}/webhooks/{webhookUID} |
| [**get_webhook**](WebhookApi.md#get_webhook)       | **GET** /v1/projects/{projectOrProductUID}/webhooks/{webhookUID}    |
| [**get_webhooks**](WebhookApi.md#get_webhooks)     | **GET** /v1/projects/{projectOrProductUID}/webhooks                 |
| [**update_webhook**](WebhookApi.md#update_webhook) | **PUT** /v1/projects/{projectOrProductUID}/webhooks/{webhookUID}    |

# **create_webhook**

> create_webhook(project_or_product_uid, webhook_uid, webhook_settings)

Creates a webhook for the specified product with the given name. The name | must be unique within the project.

### Example

- Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.webhook_settings import WebhookSettings
from notehub_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.notefile.net
# See configuration.py for a list of all supported configuration parameters.
configuration = notehub_py.Configuration(
    host = "https://api.notefile.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.WebhookApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    webhook_uid = 'Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8' # str | Webhook UID
    webhook_settings = {"settings":{"disabled":false,"id":"Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8","transform":"{\"device\":body.end_device_ids.dev_eui,\"sn\":body.end_device_ids.device_id,\"body\":body.uplink_message.decoded_payload,\"details\":body}"}} # WebhookSettings |

    try:
        api_instance.create_webhook(project_or_product_uid, webhook_uid, webhook_settings)
    except Exception as e:
        print("Exception when calling WebhookApi->create_webhook: %s\n" % e)
```

### Parameters

| Name                       | Type                                      | Description | Notes |
| -------------------------- | ----------------------------------------- | ----------- | ----- |
| **project_or_product_uid** | **str**                                   |             |
| **webhook_uid**            | **str**                                   | Webhook UID |
| **webhook_settings**       | [**WebhookSettings**](WebhookSettings.md) |             |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Webhook created successfully               | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**

> delete_webhook(project_or_product_uid, webhook_uid)

Deletes the specified webhook

### Example

- Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.notefile.net
# See configuration.py for a list of all supported configuration parameters.
configuration = notehub_py.Configuration(
    host = "https://api.notefile.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.WebhookApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    webhook_uid = 'Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8' # str | Webhook UID

    try:
        api_instance.delete_webhook(project_or_product_uid, webhook_uid)
    except Exception as e:
        print("Exception when calling WebhookApi->delete_webhook: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **webhook_uid**            | **str** | Webhook UID |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Webhook deleted successfully               | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**

> WebhookSettings get_webhook(project_or_product_uid, webhook_uid)

Retrieves the configuration settings for the specified webhook

### Example

- Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.webhook_settings import WebhookSettings
from notehub_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.notefile.net
# See configuration.py for a list of all supported configuration parameters.
configuration = notehub_py.Configuration(
    host = "https://api.notefile.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.WebhookApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    webhook_uid = 'Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8' # str | Webhook UID

    try:
        api_response = api_instance.get_webhook(project_or_product_uid, webhook_uid)
        print("The response of WebhookApi->get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->get_webhook: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **webhook_uid**            | **str** | Webhook UID |

### Return type

[**WebhookSettings**](WebhookSettings.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Webhook settings retrieved successfully    | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhooks**

> GetWebhooks200Response get_webhooks(project_or_product_uid)

Retrieves all webhooks for the specified project

### Example

- Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.get_webhooks200_response import GetWebhooks200Response
from notehub_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.notefile.net
# See configuration.py for a list of all supported configuration parameters.
configuration = notehub_py.Configuration(
    host = "https://api.notefile.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.WebhookApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |

    try:
        api_response = api_instance.get_webhooks(project_or_product_uid)
        print("The response of WebhookApi->get_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->get_webhooks: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |

### Return type

[**GetWebhooks200Response**](GetWebhooks200Response.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Webhooks retrieved successfully            | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**

> update_webhook(project_or_product_uid, webhook_uid, webhook_settings)

Updates the configuration settings for the specified webhook. | Webhook will be created if it does not exist. Update body will completely replace the existing settings.

### Example

- Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.webhook_settings import WebhookSettings
from notehub_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.notefile.net
# See configuration.py for a list of all supported configuration parameters.
configuration = notehub_py.Configuration(
    host = "https://api.notefile.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.WebhookApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    webhook_uid = 'Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8' # str | Webhook UID
    webhook_settings = {"disabled":false,"transform":"{\"device\":body.end_device_ids.dev_eui,\"sn\":body.end_device_ids.device_id,\"body\":body.uplink_message.decoded_payload,\"details\":body}"} # WebhookSettings |

    try:
        api_instance.update_webhook(project_or_product_uid, webhook_uid, webhook_settings)
    except Exception as e:
        print("Exception when calling WebhookApi->update_webhook: %s\n" % e)
```

### Parameters

| Name                       | Type                                      | Description | Notes |
| -------------------------- | ----------------------------------------- | ----------- | ----- |
| **project_or_product_uid** | **str**                                   |             |
| **webhook_uid**            | **str**                                   | Webhook UID |
| **webhook_settings**       | [**WebhookSettings**](WebhookSettings.md) |             |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Webhook updated successfully               | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
