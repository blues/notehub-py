# notehub_py.ExternalDevicesApi

All URIs are relative to *https://api.notefile.net*

| Method                                                                         | HTTP request                                                             | Description                            |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | -------------------------------------- |
| [**create_event_ext_device**](ExternalDevicesApi.md#create_event_ext_device)   | **POST** /v1/products/{productUID}/ext-devices/{deviceUID}/event         | Add an event from an external device   |
| [**ext_device_session_close**](ExternalDevicesApi.md#ext_device_session_close) | **POST** /v1/products/{productUID}/ext-devices/{deviceUID}/session/close | Close an external device&#39;s session |
| [**ext_device_session_open**](ExternalDevicesApi.md#ext_device_session_open)   | **POST** /v1/products/{productUID}/ext-devices/{deviceUID}/session/open  | Open an external device&#39;s session  |

## create_event_ext_device

> create_event_ext_device(product_uid, device_uid, event)

Add an event from an external device

Add an event from a device that isn't a Notecard, adding the device to the project if it's new. The DeviceUID is lower-cased and gets `dev:ext:` unless it has its own sub-prefix, so `dev:123` becomes `dev:ext:123`. Notehub sets `when` to the current time and adds `.qo` to a `file` with no extension. Requires the Owner or Developer role.

### Example

```python
import notehub_py
from notehub_py.models.event import Event
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ExternalDevicesApi(api_client)
    product_uid = "com.blues.bridge:sensors"  # str |
    device_uid = "dev:000000000000000"  # str |
    event = (
        notehub_py.Event()
    )  # Event | The event. `file`, `body` and `payload` are the usual fields.

    try:
        # Add an event from an external device
        api_instance.create_event_ext_device(product_uid, device_uid, event)
    except Exception as e:
        print(
            "Exception when calling ExternalDevicesApi->create_event_ext_device: %s\n"
            % e
        )
```

### Parameters

| Name            | Type                  | Description                                                                                 | Notes |
| --------------- | --------------------- | ------------------------------------------------------------------------------------------- | ----- |
| **product_uid** | **str**               |                                                                                             |
| **device_uid**  | **str**               |                                                                                             |
| **event**       | [**Event**](Event.md) | The event. &#x60;file&#x60;, &#x60;body&#x60; and &#x60;payload&#x60; are the usual fields. |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## ext_device_session_close

> ext_device_session_close(product_uid, device_uid, device_session)

Close an external device's session

Close an external device's session, if one is open, adding the device if it's new. The DeviceUID gets `dev:ext:` as in `CreateEventExtDevice`. Requires the Owner or Developer role.

### Example

```python
import notehub_py
from notehub_py.models.device_session import DeviceSession
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ExternalDevicesApi(api_client)
    product_uid = "com.blues.bridge:sensors"  # str |
    device_uid = "dev:000000000000000"  # str |
    device_session = (
        notehub_py.DeviceSession()
    )  # DeviceSession | Session fields, such as `why_session_opened` or `why_session_closed`.

    try:
        # Close an external device's session
        api_instance.ext_device_session_close(product_uid, device_uid, device_session)
    except Exception as e:
        print(
            "Exception when calling ExternalDevicesApi->ext_device_session_close: %s\n"
            % e
        )
```

### Parameters

| Name               | Type                                  | Description                                                                               | Notes |
| ------------------ | ------------------------------------- | ----------------------------------------------------------------------------------------- | ----- |
| **product_uid**    | **str**                               |                                                                                           |
| **device_uid**     | **str**                               |                                                                                           |
| **device_session** | [**DeviceSession**](DeviceSession.md) | Session fields, such as &#x60;why_session_opened&#x60; or &#x60;why_session_closed&#x60;. |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## ext_device_session_open

> ext_device_session_open(product_uid, device_uid, device_session)

Open an external device's session

Open a session for an external device, adding the device if it's new. An open session is closed first, with `why_session_closed` as the reason. The DeviceUID gets `dev:ext:` as in `CreateEventExtDevice`. Requires the Owner or Developer role. Returns 500 if webhooks are disabled for the project.

### Example

```python
import notehub_py
from notehub_py.models.device_session import DeviceSession
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ExternalDevicesApi(api_client)
    product_uid = "com.blues.bridge:sensors"  # str |
    device_uid = "dev:000000000000000"  # str |
    device_session = (
        notehub_py.DeviceSession()
    )  # DeviceSession | Session fields, such as `why_session_opened` or `why_session_closed`.

    try:
        # Open an external device's session
        api_instance.ext_device_session_open(product_uid, device_uid, device_session)
    except Exception as e:
        print(
            "Exception when calling ExternalDevicesApi->ext_device_session_open: %s\n"
            % e
        )
```

### Parameters

| Name               | Type                                  | Description                                                                               | Notes |
| ------------------ | ------------------------------------- | ----------------------------------------------------------------------------------------- | ----- |
| **product_uid**    | **str**                               |                                                                                           |
| **device_uid**     | **str**                               |                                                                                           |
| **device_session** | [**DeviceSession**](DeviceSession.md) | Session fields, such as &#x60;why_session_opened&#x60; or &#x60;why_session_closed&#x60;. |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json
