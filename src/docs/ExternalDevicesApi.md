# notehub_py.ExternalDevicesApi

All URIs are relative to *https://api.notefile.net*

| Method                                                                         | HTTP request                                                             | Description |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ----------- |
| [**create_event_ext_device**](ExternalDevicesApi.md#create_event_ext_device)   | **POST** /v1/products/{productUID}/ext-devices/{deviceUID}/event         |
| [**ext_device_session_close**](ExternalDevicesApi.md#ext_device_session_close) | **POST** /v1/products/{productUID}/ext-devices/{deviceUID}/session/close |
| [**ext_device_session_open**](ExternalDevicesApi.md#ext_device_session_open)   | **POST** /v1/products/{productUID}/ext-devices/{deviceUID}/session/open  |

# **create_event_ext_device**

> create_event_ext_device(product_uid, device_uid, event)

Creates an event using specified webhook

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.event import Event
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

# Configure Bearer authorization: personalAccessToken
configuration = notehub_py.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ExternalDevicesApi(api_client)
    product_uid = 'com.blues.bridge:sensors' # str |
    device_uid = 'dev:000000000000000' # str |
    event = notehub_py.Event() # Event | Event Object

    try:
        api_instance.create_event_ext_device(product_uid, device_uid, event)
    except Exception as e:
        print("Exception when calling ExternalDevicesApi->create_event_ext_device: %s\n" % e)
```

### Parameters

| Name            | Type                  | Description  | Notes |
| --------------- | --------------------- | ------------ | ----- |
| **product_uid** | **str**               |              |
| **device_uid**  | **str**               |              |
| **event**       | [**Event**](Event.md) | Event Object |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Event Created Successfully                 | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ext_device_session_close**

> ext_device_session_close(product_uid, device_uid, device_session)

Closes the session for the specified device if open

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.device_session import DeviceSession
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

# Configure Bearer authorization: personalAccessToken
configuration = notehub_py.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ExternalDevicesApi(api_client)
    product_uid = 'com.blues.bridge:sensors' # str |
    device_uid = 'dev:000000000000000' # str |
    device_session = notehub_py.DeviceSession() # DeviceSession | Session Object

    try:
        api_instance.ext_device_session_close(product_uid, device_uid, device_session)
    except Exception as e:
        print("Exception when calling ExternalDevicesApi->ext_device_session_close: %s\n" % e)
```

### Parameters

| Name               | Type                                  | Description    | Notes |
| ------------------ | ------------------------------------- | -------------- | ----- |
| **product_uid**    | **str**                               |                |
| **device_uid**     | **str**                               |                |
| **device_session** | [**DeviceSession**](DeviceSession.md) | Session Object |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Session closed                             | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ext_device_session_open**

> ext_device_session_open(product_uid, device_uid, device_session)

Create a Session for the specified device. | If a session is currently open it will be closed and a new one opened.

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.device_session import DeviceSession
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

# Configure Bearer authorization: personalAccessToken
configuration = notehub_py.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.ExternalDevicesApi(api_client)
    product_uid = 'com.blues.bridge:sensors' # str |
    device_uid = 'dev:000000000000000' # str |
    device_session = notehub_py.DeviceSession() # DeviceSession | Session Object

    try:
        api_instance.ext_device_session_open(product_uid, device_uid, device_session)
    except Exception as e:
        print("Exception when calling ExternalDevicesApi->ext_device_session_open: %s\n" % e)
```

### Parameters

| Name               | Type                                  | Description    | Notes |
| ------------------ | ------------------------------------- | -------------- | ----- |
| **product_uid**    | **str**                               |                |
| **device_uid**     | **str**                               |                |
| **device_session** | [**DeviceSession**](DeviceSession.md) | Session Object |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Session Created Successfully               | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
