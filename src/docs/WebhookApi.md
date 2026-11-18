# notehub_py.WebhookApi

All URIs are relative to *https://api.notefile.net*

| Method                                                                                             | HTTP request                                                                       | Description                                           |
| -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------- |
| [**create_legacy_webhook_event**](WebhookApi.md#create_legacy_webhook_event)                       | **POST** /v1/products/{productUID}/devices/{deviceUID}/webhook-event               | Add a note-shaped event from a device (legacy)        |
| [**create_webhook**](WebhookApi.md#create_webhook)                                                 | **POST** /v1/projects/{projectOrProductUID}/webhooks/{webhookUID}                  | Create a webhook                                      |
| [**create_webhook_device_event_by_product**](WebhookApi.md#create_webhook_device_event_by_product) | **POST** /v1/products/{productUID}/webhooks/{webhookUID}/devices/{deviceUID}/event | Send a device&#39;s event through a webhook           |
| [**create_webhook_event_by_product**](WebhookApi.md#create_webhook_event_by_product)               | **POST** /v1/products/{productUID}/webhooks/{webhookUID}/event                     | Send an event through a webhook                       |
| [**delete_webhook**](WebhookApi.md#delete_webhook)                                                 | **DELETE** /v1/projects/{projectOrProductUID}/webhooks/{webhookUID}                | Delete a webhook                                      |
| [**get_webhook**](WebhookApi.md#get_webhook)                                                       | **GET** /v1/projects/{projectOrProductUID}/webhooks/{webhookUID}                   | Get a webhook                                         |
| [**get_webhook_settings_by_product**](WebhookApi.md#get_webhook_settings_by_product)               | **GET** /v1/products/{productUID}/webhooks/{webhookUID}/settings                   | Get a webhook by ProductUID                           |
| [**get_webhooks**](WebhookApi.md#get_webhooks)                                                     | **GET** /v1/projects/{projectOrProductUID}/webhooks                                | List webhooks                                         |
| [**update_legacy_webhook_session**](WebhookApi.md#update_legacy_webhook_session)                   | **PUT** /v1/products/{productUID}/devices/{deviceUID}/webhook-session              | Open or close a webhook device&#39;s session (legacy) |
| [**update_webhook**](WebhookApi.md#update_webhook)                                                 | **PUT** /v1/projects/{projectOrProductUID}/webhooks/{webhookUID}                   | Update a webhook                                      |
| [**update_webhook_settings_by_product**](WebhookApi.md#update_webhook_settings_by_product)         | **PUT** /v1/products/{productUID}/webhooks/{webhookUID}/settings                   | Update a webhook by ProductUID                        |

## create_legacy_webhook_event

> create_legacy_webhook_event(product_uid, device_uid, request_body)

Add a note-shaped event from a device (legacy)

Legacy: add an event from a device, adding the device to the project if it's new. The body is note-shaped: `file`, `body`, an optional base64 `payload`, and other event fields such as `when` and `sn`. No webhook transform applies. New integrations should use `CreateWebhookDeviceEventByProduct`. Requires the Owner or Developer role. Returns 400 if there's no `body` or `payload`.

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
        # Add a note-shaped event from a device (legacy)
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

Create a webhook

Create an inbound webhook that outside services post to with `CreateWebhookEventByProduct`. Its events go to the notefile `<webhookUID>.qo` unless its JSONata `transform` sets `file`. Use a lower-case ID; the event endpoints look it up in lower case. Requires the Owner or Developer role. Returns 409 if the ID is taken, and 400 if it has characters other than letters, digits, `-` and `_`.

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
    webhook_uid = "ttn-uplink"  # str | Webhook ID, e.g. `ttn-uplink`. Use lower case. List with `GetWebhooks`.
    webhook_settings = {
        "disabled": false,
        "id": "ttn-uplink",
        "transform": '{"device":body.end_device_ids.dev_eui,"sn":body.end_device_ids.device_id,"body":body.uplink_message.decoded_payload,"details":body}',
    }  # WebhookSettings |

    try:
        # Create a webhook
        api_instance.create_webhook(
            project_or_product_uid, webhook_uid, webhook_settings
        )
    except Exception as e:
        print("Exception when calling WebhookApi->create_webhook: %s\n" % e)
```

### Parameters

| Name                       | Type                                      | Description                                                                                 | Notes |
| -------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**                                   |                                                                                             |
| **webhook_uid**            | **str**                                   | Webhook ID, e.g. &#x60;ttn-uplink&#x60;. Use lower case. List with &#x60;GetWebhooks&#x60;. |
| **webhook_settings**       | [**WebhookSettings**](WebhookSettings.md) |                                                                                             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## create_webhook_device_event_by_product

> create_webhook_device_event_by_product(product_uid, webhook_uid, device_uid, request_body)

Send a device's event through a webhook

Post JSON to a webhook as one device's event, like `CreateWebhookEventByProduct`, adding the device if it's new. The DeviceUID is lower-cased and gets `dev:ext:` unless it has its own sub-prefix, so `dev:abc` becomes `dev:ext:abc`, not an existing Notecard. Requires the Owner or Developer role. Returns 400 if the transform fails, and 500 if the webhook is disabled.

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
    webhook_uid = "ttn-uplink"  # str | Webhook ID, e.g. `ttn-uplink`. Use lower case. List with `GetWebhooks`.
    device_uid = "dev:000000000000000"  # str |
    request_body = None  # Dict[str, object] | Any JSON object; it becomes the event body, or the transform's input.

    try:
        # Send a device's event through a webhook
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

| Name             | Type                               | Description                                                                                 | Notes |
| ---------------- | ---------------------------------- | ------------------------------------------------------------------------------------------- | ----- |
| **product_uid**  | **str**                            |                                                                                             |
| **webhook_uid**  | **str**                            | Webhook ID, e.g. &#x60;ttn-uplink&#x60;. Use lower case. List with &#x60;GetWebhooks&#x60;. |
| **device_uid**   | **str**                            |                                                                                             |
| **request_body** | [**Dict[str, object]**](object.md) | Any JSON object; it becomes the event body, or the transform&#39;s input.                   |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## create_webhook_event_by_product

> create_webhook_event_by_product(product_uid, webhook_uid, request_body)

Send an event through a webhook

Post JSON to a webhook. The body becomes the event body, in `<webhookUID>.qo`, from `dev:ext:webhook`; a `transform` can change all three, but must set `body`. For a specific device, use `CreateWebhookDeviceEventByProduct`. Requires the Owner or Developer role. Returns 400 if the transform fails or sets no `body`, and 500 if the webhook is disabled.

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
    webhook_uid = "ttn-uplink"  # str | Webhook ID, e.g. `ttn-uplink`. Use lower case. List with `GetWebhooks`.
    request_body = None  # Dict[str, object] | Any JSON object; it becomes the event body, or the transform's input.

    try:
        # Send an event through a webhook
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

| Name             | Type                               | Description                                                                                 | Notes |
| ---------------- | ---------------------------------- | ------------------------------------------------------------------------------------------- | ----- |
| **product_uid**  | **str**                            |                                                                                             |
| **webhook_uid**  | **str**                            | Webhook ID, e.g. &#x60;ttn-uplink&#x60;. Use lower case. List with &#x60;GetWebhooks&#x60;. |
| **request_body** | [**Dict[str, object]**](object.md) | Any JSON object; it becomes the event body, or the transform&#39;s input.                   |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## delete_webhook

> delete_webhook(project_or_product_uid, webhook_uid)

Delete a webhook

Delete a webhook's settings. Posts to its ID are still accepted, just without a transform; to stop accepting them, set `disabled` with `UpdateWebhook` instead. Requires the Owner or Developer role. Returns 404 if the webhook doesn't exist.

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
    webhook_uid = "ttn-uplink"  # str | Webhook ID, e.g. `ttn-uplink`. Use lower case. List with `GetWebhooks`.

    try:
        # Delete a webhook
        api_instance.delete_webhook(project_or_product_uid, webhook_uid)
    except Exception as e:
        print("Exception when calling WebhookApi->delete_webhook: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                                 | Notes |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                                                             |
| **webhook_uid**            | **str** | Webhook ID, e.g. &#x60;ttn-uplink&#x60;. Use lower case. List with &#x60;GetWebhooks&#x60;. |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_webhook

> WebhookSettings get_webhook(project_or_product_uid, webhook_uid)

Get a webhook

Get one webhook's transform and whether it's disabled. Requires the Owner or Developer role. Returns 404 if the webhook doesn't exist.

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
    webhook_uid = "ttn-uplink"  # str | Webhook ID, e.g. `ttn-uplink`. Use lower case. List with `GetWebhooks`.

    try:
        # Get a webhook
        api_response = api_instance.get_webhook(project_or_product_uid, webhook_uid)
        print("The response of WebhookApi->get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebhookApi->get_webhook: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                                 | Notes |
| -------------------------- | ------- | ------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                                                             |
| **webhook_uid**            | **str** | Webhook ID, e.g. &#x60;ttn-uplink&#x60;. Use lower case. List with &#x60;GetWebhooks&#x60;. |

### Return type

[**WebhookSettings**](WebhookSettings.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_webhook_settings_by_product

> WebhookSettings get_webhook_settings_by_product(product_uid, webhook_uid)

Get a webhook by ProductUID

Get one webhook's settings, like `GetWebhook`, but addressed by ProductUID instead of the project. Requires the Owner or Developer role. Returns 500, not 404, if the webhook doesn't exist.

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
    webhook_uid = "ttn-uplink"  # str | Webhook ID, e.g. `ttn-uplink`. Use lower case. List with `GetWebhooks`.

    try:
        # Get a webhook by ProductUID
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

| Name            | Type    | Description                                                                                 | Notes |
| --------------- | ------- | ------------------------------------------------------------------------------------------- | ----- |
| **product_uid** | **str** |                                                                                             |
| **webhook_uid** | **str** | Webhook ID, e.g. &#x60;ttn-uplink&#x60;. Use lower case. List with &#x60;GetWebhooks&#x60;. |

### Return type

[**WebhookSettings**](WebhookSettings.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_webhooks

> GetWebhooks200Response get_webhooks(project_or_product_uid)

List webhooks

List a project's inbound webhooks with their transforms and whether they're disabled. An inbound webhook lets an outside service post data that Notehub turns into events. Requires the Owner or Developer role.

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
        # List webhooks
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

Open or close a webhook device's session (legacy)

Legacy: open, update or close a webhook device's session, adding the device if it's new. The body is a session: set `why_session_opened` to open one, `why_session_closed` to close it, both to close and reopen, or neither to update the open session. Requires the Owner or Developer role. Returns 400 when updating with no session open.

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
    request_body = None  # Dict[str, object] | Session fields, such as `why_session_opened`, `why_session_closed` and signal or location values. (optional)

    try:
        # Open or close a webhook device's session (legacy)
        api_instance.update_legacy_webhook_session(
            product_uid, device_uid, request_body=request_body
        )
    except Exception as e:
        print(
            "Exception when calling WebhookApi->update_legacy_webhook_session: %s\n" % e
        )
```

### Parameters

| Name             | Type                               | Description                                                                                                           | Notes      |
| ---------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------------------- | ---------- |
| **product_uid**  | **str**                            |                                                                                                                       |
| **device_uid**   | **str**                            |                                                                                                                       |
| **request_body** | [**Dict[str, object]**](object.md) | Session fields, such as &#x60;why_session_opened&#x60;, &#x60;why_session_closed&#x60; and signal or location values. | [optional] |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## update_webhook

> update_webhook(project_or_product_uid, webhook_uid, webhook_settings)

Update a webhook

Replace a webhook's settings, creating the webhook if it doesn't exist. Send every field: a missing `transform` is cleared and a missing `disabled` enables the webhook. Requires the Owner or Developer role.

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
    webhook_uid = "ttn-uplink"  # str | Webhook ID, e.g. `ttn-uplink`. Use lower case. List with `GetWebhooks`.
    webhook_settings = {
        "disabled": false,
        "transform": '{"device":body.end_device_ids.dev_eui,"sn":body.end_device_ids.device_id,"body":body.uplink_message.decoded_payload,"details":body}',
    }  # WebhookSettings |

    try:
        # Update a webhook
        api_instance.update_webhook(
            project_or_product_uid, webhook_uid, webhook_settings
        )
    except Exception as e:
        print("Exception when calling WebhookApi->update_webhook: %s\n" % e)
```

### Parameters

| Name                       | Type                                      | Description                                                                                 | Notes |
| -------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**                                   |                                                                                             |
| **webhook_uid**            | **str**                                   | Webhook ID, e.g. &#x60;ttn-uplink&#x60;. Use lower case. List with &#x60;GetWebhooks&#x60;. |
| **webhook_settings**       | [**WebhookSettings**](WebhookSettings.md) |                                                                                             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## update_webhook_settings_by_product

> update_webhook_settings_by_product(product_uid, webhook_uid, webhook_settings)

Update a webhook by ProductUID

Replace a webhook's settings, like `UpdateWebhook`, but addressed by ProductUID. Creates the webhook if it doesn't exist. Requires the Owner or Developer role. Returns 400 if the ID has characters other than letters, digits, `-` and `_`.

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
    webhook_uid = "ttn-uplink"  # str | Webhook ID, e.g. `ttn-uplink`. Use lower case. List with `GetWebhooks`.
    webhook_settings = {
        "disabled": false,
        "transform": '{"device":body.end_device_ids.dev_eui,"sn":body.end_device_ids.device_id,"body":body.uplink_message.decoded_payload,"details":body}',
    }  # WebhookSettings |

    try:
        # Update a webhook by ProductUID
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

| Name                 | Type                                      | Description                                                                                 | Notes |
| -------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------- | ----- |
| **product_uid**      | **str**                                   |                                                                                             |
| **webhook_uid**      | **str**                                   | Webhook ID, e.g. &#x60;ttn-uplink&#x60;. Use lower case. List with &#x60;GetWebhooks&#x60;. |
| **webhook_settings** | [**WebhookSettings**](WebhookSettings.md) |                                                                                             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json
