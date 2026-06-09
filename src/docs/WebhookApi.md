# notehub_py.WebhookApi

All URIs are relative to *https://api.notefile.net*

| Method                                                                                             | HTTP request                                                                       | Description |
| -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------- |
| [**create_legacy_webhook_event**](WebhookApi.md#create_legacy_webhook_event)                       | **POST** /v1/products/{productUID}/devices/{deviceUID}/webhook-event               |
| [**create_webhook**](WebhookApi.md#create_webhook)                                                 | **POST** /v1/projects/{projectOrProductUID}/webhooks/{webhookUID}                  |
| [**create_webhook_device_event_by_product**](WebhookApi.md#create_webhook_device_event_by_product) | **POST** /v1/products/{productUID}/webhooks/{webhookUID}/devices/{deviceUID}/event |
| [**create_webhook_event_by_product**](WebhookApi.md#create_webhook_event_by_product)               | **POST** /v1/products/{productUID}/webhooks/{webhookUID}/event                     |
| [**delete_webhook**](WebhookApi.md#delete_webhook)                                                 | **DELETE** /v1/projects/{projectOrProductUID}/webhooks/{webhookUID}                |
| [**get_webhook**](WebhookApi.md#get_webhook)                                                       | **GET** /v1/projects/{projectOrProductUID}/webhooks/{webhookUID}                   |
| [**get_webhook_settings_by_product**](WebhookApi.md#get_webhook_settings_by_product)               | **GET** /v1/products/{productUID}/webhooks/{webhookUID}/settings                   |
| [**get_webhooks**](WebhookApi.md#get_webhooks)                                                     | **GET** /v1/projects/{projectOrProductUID}/webhooks                                |
| [**update_legacy_webhook_session**](WebhookApi.md#update_legacy_webhook_session)                   | **PUT** /v1/products/{productUID}/devices/{deviceUID}/webhook-session              |
| [**update_webhook**](WebhookApi.md#update_webhook)                                                 | **PUT** /v1/projects/{projectOrProductUID}/webhooks/{webhookUID}                   |
| [**update_webhook_settings_by_product**](WebhookApi.md#update_webhook_settings_by_product)         | **PUT** /v1/products/{productUID}/webhooks/{webhookUID}/settings                   |

## create_legacy_webhook_event

> create_legacy_webhook_event(product_uid, device_uid, request_body)

Legacy endpoint for sending an event from a webhook, associated with the given device (provisioning it if necessary). The request body is a Note-shaped object containing the notefile name, body, and optional payload.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.WebhookApi(api_client)
    product_uid = "com.blues.bridge:sensors"  # str |
    device_uid = "dev:000000000000000"  # str |
    request_body = {
        "body": {"key": "value"},
        "file": "data.qo",
        "payload": "SGVsbG8sIFdvcmxkIQ==",
    }  # Dict[str, object] | A Note-shaped event. Typically contains the notefile name (file), a JSON body, and an optional base64-encoded payload, but any additional Note fields (e.g. when, sn, where_lat, where_lon) are accepted and honored.

    try:
        api_instance.create_legacy_webhook_event(product_uid, device_uid, request_body)
    except Exception as e:
        print(
            "Exception when calling WebhookApi->create_legacy_webhook_event: %s\n" % e
        )
```

### Parameters

| Name             | Type                               | Description                                                                                                                                                                                                           | Notes |
| ---------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **product_uid**  | **str**                            |                                                                                                                                                                                                                       |
| **device_uid**   | **str**                            |                                                                                                                                                                                                                       |
| **request_body** | [**Dict[str, object]**](object.md) | A Note-shaped event. Typically contains the notefile name (file), a JSON body, and an optional base64-encoded payload, but any additional Note fields (e.g. when, sn, where_lat, where_lon) are accepted and honored. |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## create_webhook

> create_webhook(project_or_product_uid, webhook_uid, webhook_settings)

Creates a webhook for the specified product with the given name. The name | must be unique within the project.

### Example

```python
import notehub_py
from notehub_py.models.webhook_settings import WebhookSettings
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.WebhookApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    webhook_uid = "Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8"  # str | Webhook UID
    webhook_settings = {
        "settings": {
            "disabled": false,
            "id": "Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
            "transform": '{"device":body.end_device_ids.dev_eui,"sn":body.end_device_ids.device_id,"body":body.uplink_message.decoded_payload,"details":body}',
        }
    }  # WebhookSettings |

    try:
        api_instance.create_webhook(
            project_or_product_uid, webhook_uid, webhook_settings
        )
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

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## create_webhook_device_event_by_product

> create_webhook_device_event_by_product(product_uid, webhook_uid, device_uid, request_body)

Sends an event to be processed by the specified webhook, addressed by productUID, associated with the given device (provisioning it if necessary). The entire request body becomes the event body. The webhook's configured JSONata transform, if any, is applied before routing.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.WebhookApi(api_client)
    product_uid = "com.blues.bridge:sensors"  # str |
    webhook_uid = "Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8"  # str | Webhook UID
    device_uid = "dev:000000000000000"  # str |
    request_body = None  # Dict[str, object] | The event body (arbitrary JSON)

    try:
        api_instance.create_webhook_device_event_by_product(
            product_uid, webhook_uid, device_uid, request_body
        )
    except Exception as e:
        print(
            "Exception when calling WebhookApi->create_webhook_device_event_by_product: %s\n"
            % e
        )
```

### Parameters

| Name             | Type                               | Description                     | Notes |
| ---------------- | ---------------------------------- | ------------------------------- | ----- |
| **product_uid**  | **str**                            |                                 |
| **webhook_uid**  | **str**                            | Webhook UID                     |
| **device_uid**   | **str**                            |                                 |
| **request_body** | [**Dict[str, object]**](object.md) | The event body (arbitrary JSON) |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## create_webhook_event_by_product

> create_webhook_event_by_product(product_uid, webhook_uid, request_body)

Sends an event to be processed by the specified webhook, addressed by productUID. The entire request body becomes the event body. The webhook's configured JSONata transform, if any, is applied before routing. The event is not associated with a specific device.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.WebhookApi(api_client)
    product_uid = "com.blues.bridge:sensors"  # str |
    webhook_uid = "Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8"  # str | Webhook UID
    request_body = None  # Dict[str, object] | The event body (arbitrary JSON)

    try:
        api_instance.create_webhook_event_by_product(
            product_uid, webhook_uid, request_body
        )
    except Exception as e:
        print(
            "Exception when calling WebhookApi->create_webhook_event_by_product: %s\n"
            % e
        )
```

### Parameters

| Name             | Type                               | Description                     | Notes |
| ---------------- | ---------------------------------- | ------------------------------- | ----- |
| **product_uid**  | **str**                            |                                 |
| **webhook_uid**  | **str**                            | Webhook UID                     |
| **request_body** | [**Dict[str, object]**](object.md) | The event body (arbitrary JSON) |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## delete_webhook

> delete_webhook(project_or_product_uid, webhook_uid)

Deletes the specified webhook

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.WebhookApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    webhook_uid = "Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8"  # str | Webhook UID

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

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_webhook

> WebhookSettings get_webhook(project_or_product_uid, webhook_uid)

Retrieves the configuration settings for the specified webhook

### Example

```python
import notehub_py
from notehub_py.models.webhook_settings import WebhookSettings
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.WebhookApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    webhook_uid = "Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8"  # str | Webhook UID

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

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_webhook_settings_by_product

> WebhookSettings get_webhook_settings_by_product(product_uid, webhook_uid)

Retrieves the configuration settings for the specified webhook, addressed by productUID.

### Example

```python
import notehub_py
from notehub_py.models.webhook_settings import WebhookSettings
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.WebhookApi(api_client)
    product_uid = "com.blues.bridge:sensors"  # str |
    webhook_uid = "Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8"  # str | Webhook UID

    try:
        api_response = api_instance.get_webhook_settings_by_product(
            product_uid, webhook_uid
        )
        print("The response of WebhookApi->get_webhook_settings_by_product:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling WebhookApi->get_webhook_settings_by_product: %s\n"
            % e
        )
```

### Parameters

| Name            | Type    | Description | Notes |
| --------------- | ------- | ----------- | ----- |
| **product_uid** | **str** |             |
| **webhook_uid** | **str** | Webhook UID |

### Return type

[**WebhookSettings**](WebhookSettings.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_webhooks

> GetWebhooks200Response get_webhooks(project_or_product_uid)

Retrieves all webhooks for the specified project

### Example

```python
import notehub_py
from notehub_py.models.get_webhooks200_response import GetWebhooks200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.WebhookApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |

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

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## update_legacy_webhook_session

> update_legacy_webhook_session(product_uid, device_uid, request_body=request_body)

Legacy endpoint for opening or updating a webhook session for the given device (provisioning the device if necessary). Used by external services that need to maintain a callable session against a device behind a webhook.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.WebhookApi(api_client)
    product_uid = "com.blues.bridge:sensors"  # str |
    device_uid = "dev:000000000000000"  # str |
    request_body = None  # Dict[str, object] | Optional session metadata. (optional)

    try:
        api_instance.update_legacy_webhook_session(
            product_uid, device_uid, request_body=request_body
        )
    except Exception as e:
        print(
            "Exception when calling WebhookApi->update_legacy_webhook_session: %s\n" % e
        )
```

### Parameters

| Name             | Type                               | Description                | Notes      |
| ---------------- | ---------------------------------- | -------------------------- | ---------- |
| **product_uid**  | **str**                            |                            |
| **device_uid**   | **str**                            |                            |
| **request_body** | [**Dict[str, object]**](object.md) | Optional session metadata. | [optional] |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## update_webhook

> update_webhook(project_or_product_uid, webhook_uid, webhook_settings)

Updates the configuration settings for the specified webhook. | Webhook will be created if it does not exist. Update body will completely replace the existing settings.

### Example

```python
import notehub_py
from notehub_py.models.webhook_settings import WebhookSettings
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.WebhookApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    webhook_uid = "Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8"  # str | Webhook UID
    webhook_settings = {
        "disabled": false,
        "transform": '{"device":body.end_device_ids.dev_eui,"sn":body.end_device_ids.device_id,"body":body.uplink_message.decoded_payload,"details":body}',
    }  # WebhookSettings |

    try:
        api_instance.update_webhook(
            project_or_product_uid, webhook_uid, webhook_settings
        )
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

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## update_webhook_settings_by_product

> update_webhook_settings_by_product(product_uid, webhook_uid, webhook_settings)

Updates the configuration settings for the specified webhook, addressed by productUID. Update body will completely replace the existing settings.

### Example

```python
import notehub_py
from notehub_py.models.webhook_settings import WebhookSettings
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.WebhookApi(api_client)
    product_uid = "com.blues.bridge:sensors"  # str |
    webhook_uid = "Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8"  # str | Webhook UID
    webhook_settings = {
        "disabled": false,
        "transform": '{"device":body.end_device_ids.dev_eui,"sn":body.end_device_ids.device_id,"body":body.uplink_message.decoded_payload,"details":body}',
    }  # WebhookSettings |

    try:
        api_instance.update_webhook_settings_by_product(
            product_uid, webhook_uid, webhook_settings
        )
    except Exception as e:
        print(
            "Exception when calling WebhookApi->update_webhook_settings_by_product: %s\n"
            % e
        )
```

### Parameters

| Name                 | Type                                      | Description | Notes |
| -------------------- | ----------------------------------------- | ----------- | ----- |
| **product_uid**      | **str**                                   |             |
| **webhook_uid**      | **str**                                   | Webhook UID |
| **webhook_settings** | [**WebhookSettings**](WebhookSettings.md) |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json
