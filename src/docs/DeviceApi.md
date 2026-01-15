# notehub_py.DeviceApi

All URIs are relative to *https://api.notefile.net*

| Method                                                                                              | HTTP request                                                                                   | Description                                     |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| [**add_db_note**](DeviceApi.md#add_db_note)                                                         | **POST** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/notes/{notefileID}/{noteID}    |
| [**add_qi_note**](DeviceApi.md#add_qi_note)                                                         | **POST** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/notes/{notefileID}             |
| [**delete_device**](DeviceApi.md#delete_device)                                                     | **DELETE** /v1/projects/{projectOrProductUID}/devices/{deviceUID}                              |
| [**delete_device_environment_variable**](DeviceApi.md#delete_device_environment_variable)           | **DELETE** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/environment_variables/{key}  |
| [**delete_note**](DeviceApi.md#delete_note)                                                         | **DELETE** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/notes/{notefileID}/{noteID}  |
| [**delete_notefiles**](DeviceApi.md#delete_notefiles)                                               | **DELETE** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/files                        |
| [**disable_device**](DeviceApi.md#disable_device)                                                   | **POST** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/disable                        |
| [**disable_device_connectivity_assurance**](DeviceApi.md#disable_device_connectivity_assurance)     | **POST** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/disable-connectivity-assurance |
| [**enable_device**](DeviceApi.md#enable_device)                                                     | **POST** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/enable                         |
| [**enable_device_connectivity_assurance**](DeviceApi.md#enable_device_connectivity_assurance)       | **POST** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/enable-connectivity-assurance  |
| [**get_db_note**](DeviceApi.md#get_db_note)                                                         | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/notes/{notefileID}/{noteID}     |
| [**get_device**](DeviceApi.md#get_device)                                                           | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}                                 |
| [**get_device_environment_hierarchy**](DeviceApi.md#get_device_environment_hierarchy)               | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/environment_hierarchy           | Get environment variable hierarchy for a device |
| [**get_device_environment_variables**](DeviceApi.md#get_device_environment_variables)               | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/environment_variables           |
| [**get_device_environment_variables_by_pin**](DeviceApi.md#get_device_environment_variables_by_pin) | **GET** /v1/products/{productUID}/devices/{deviceUID}/environment_variables_with_pin           |
| [**get_device_health_log**](DeviceApi.md#get_device_health_log)                                     | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/health-log                      |
| [**get_device_latest_events**](DeviceApi.md#get_device_latest_events)                               | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/latest                          |
| [**get_device_plans**](DeviceApi.md#get_device_plans)                                               | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/plans                           |
| [**get_device_public_key**](DeviceApi.md#get_device_public_key)                                     | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/public-key                      |
| [**get_device_public_keys**](DeviceApi.md#get_device_public_keys)                                   | **GET** /v1/projects/{projectOrProductUID}/devices/public-keys                                 |
| [**get_device_sessions**](DeviceApi.md#get_device_sessions)                                         | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/sessions                        |
| [**get_devices**](DeviceApi.md#get_devices)                                                         | **GET** /v1/projects/{projectOrProductUID}/devices                                             |
| [**get_fleet_devices**](DeviceApi.md#get_fleet_devices)                                             | **GET** /v1/projects/{projectOrProductUID}/fleets/{fleetUID}/devices                           |
| [**get_notefile**](DeviceApi.md#get_notefile)                                                       | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/notes/{notefileID}              |
| [**list_notefiles**](DeviceApi.md#list_notefiles)                                                   | **GET** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/files                           |
| [**provision_device**](DeviceApi.md#provision_device)                                               | **POST** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/provision                      |
| [**set_device_environment_variables**](DeviceApi.md#set_device_environment_variables)               | **PUT** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/environment_variables           |
| [**set_device_environment_variables_by_pin**](DeviceApi.md#set_device_environment_variables_by_pin) | **PUT** /v1/products/{productUID}/devices/{deviceUID}/environment_variables_with_pin           |
| [**signal_device**](DeviceApi.md#signal_device)                                                     | **POST** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/signal                         |
| [**update_db_note**](DeviceApi.md#update_db_note)                                                   | **PUT** /v1/projects/{projectOrProductUID}/devices/{deviceUID}/notes/{notefileID}/{noteID}     |

# **add_db_note**

> add_db_note(project_or_product_uid, device_uid, notefile_id, note_id, note_input)

Add a Note to a .db notefile. if noteID is '-' then payload is ignored and empty notefile is created

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.note_input import NoteInput
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |
    notefile_id = 'notefile_id_example' # str |
    note_id = 'note_id_example' # str |
    note_input = notehub_py.NoteInput() # NoteInput | Body or payload of note to be added to the device

    try:
        api_instance.add_db_note(project_or_product_uid, device_uid, notefile_id, note_id, note_input)
    except Exception as e:
        print("Exception when calling DeviceApi->add_db_note: %s\n" % e)
```

### Parameters

| Name                       | Type                          | Description                                       | Notes |
| -------------------------- | ----------------------------- | ------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**                       |                                                   |
| **device_uid**             | **str**                       |                                                   |
| **notefile_id**            | **str**                       |                                                   |
| **note_id**                | **str**                       |                                                   |
| **note_input**             | [**NoteInput**](NoteInput.md) | Body or payload of note to be added to the device |

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
| **200**     | An empty object means success              | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_qi_note**

> add_qi_note(project_or_product_uid, device_uid, notefile_id, note_input)

Adds a Note to a Notefile, creating the Notefile if it doesn't yet exist.

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.note_input import NoteInput
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |
    notefile_id = 'notefile_id_example' # str |
    note_input = notehub_py.NoteInput() # NoteInput | Body or payload of note to be added to the device

    try:
        api_instance.add_qi_note(project_or_product_uid, device_uid, notefile_id, note_input)
    except Exception as e:
        print("Exception when calling DeviceApi->add_qi_note: %s\n" % e)
```

### Parameters

| Name                       | Type                          | Description                                       | Notes |
| -------------------------- | ----------------------------- | ------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**                       |                                                   |
| **device_uid**             | **str**                       |                                                   |
| **notefile_id**            | **str**                       |                                                   |
| **note_input**             | [**NoteInput**](NoteInput.md) | Body or payload of note to be added to the device |

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
| **200**     | An empty object means success              | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**

> delete_device(project_or_product_uid, device_uid)

Delete Device

### Example

- Bearer Authentication (personalAccessToken):

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

# Configure Bearer authorization: personalAccessToken
configuration = notehub_py.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |

    try:
        api_instance.delete_device(project_or_product_uid, device_uid)
    except Exception as e:
        print("Exception when calling DeviceApi->delete_device: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **204**     | Successful operation                       | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_environment_variable**

> EnvironmentVariables delete_device_environment_variable(project_or_product_uid, device_uid, key)

Delete environment variable of a device

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.environment_variables import EnvironmentVariables
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |
    key = 'key_example' # str | The environment variable key to delete.

    try:
        api_response = api_instance.delete_device_environment_variable(project_or_product_uid, device_uid, key)
        print("The response of DeviceApi->delete_device_environment_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->delete_device_environment_variable: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                             | Notes |
| -------------------------- | ------- | --------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                         |
| **device_uid**             | **str** |                                         |
| **key**                    | **str** | The environment variable key to delete. |

### Return type

[**EnvironmentVariables**](EnvironmentVariables.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                              | Response headers |
| ----------- | -------------------------------------------------------- | ---------------- |
| **200**     | The response body from an environment variables request. | -                |
| **0**       | The response body in case of an API error.               | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_note**

> delete_note(project_or_product_uid, device_uid, notefile_id, note_id)

Delete a note from a .db or .qi notefile

### Example

- Bearer Authentication (personalAccessToken):

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

# Configure Bearer authorization: personalAccessToken
configuration = notehub_py.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |
    notefile_id = 'notefile_id_example' # str |
    note_id = 'note_id_example' # str |

    try:
        api_instance.delete_note(project_or_product_uid, device_uid, notefile_id, note_id)
    except Exception as e:
        print("Exception when calling DeviceApi->delete_note: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |
| **notefile_id**            | **str** |             |
| **note_id**                | **str** |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | An empty object means success              | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_notefiles**

> delete_notefiles(project_or_product_uid, device_uid, delete_notefiles_request)

Deletes Notefiles and the Notes they contain.

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.delete_notefiles_request import DeleteNotefilesRequest
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |
    delete_notefiles_request = notehub_py.DeleteNotefilesRequest() # DeleteNotefilesRequest |

    try:
        api_instance.delete_notefiles(project_or_product_uid, device_uid, delete_notefiles_request)
    except Exception as e:
        print("Exception when calling DeviceApi->delete_notefiles: %s\n" % e)
```

### Parameters

| Name                         | Type                                                    | Description | Notes |
| ---------------------------- | ------------------------------------------------------- | ----------- | ----- |
| **project_or_product_uid**   | **str**                                                 |             |
| **device_uid**               | **str**                                                 |             |
| **delete_notefiles_request** | [**DeleteNotefilesRequest**](DeleteNotefilesRequest.md) |             |

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
| **200**     | An empty object means success              | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_device**

> disable_device(project_or_product_uid, device_uid)

Disable Device

### Example

- Bearer Authentication (personalAccessToken):

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

# Configure Bearer authorization: personalAccessToken
configuration = notehub_py.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |

    try:
        api_instance.disable_device(project_or_product_uid, device_uid)
    except Exception as e:
        print("Exception when calling DeviceApi->disable_device: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Successful operation                       | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_device_connectivity_assurance**

> disable_device_connectivity_assurance(project_or_product_uid, device_uid)

Disable Connectivity Assurance

### Example

- Bearer Authentication (personalAccessToken):

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

# Configure Bearer authorization: personalAccessToken
configuration = notehub_py.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |

    try:
        api_instance.disable_device_connectivity_assurance(project_or_product_uid, device_uid)
    except Exception as e:
        print("Exception when calling DeviceApi->disable_device_connectivity_assurance: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Successful operation                       | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_device**

> enable_device(project_or_product_uid, device_uid)

Enable Device

### Example

- Bearer Authentication (personalAccessToken):

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

# Configure Bearer authorization: personalAccessToken
configuration = notehub_py.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |

    try:
        api_instance.enable_device(project_or_product_uid, device_uid)
    except Exception as e:
        print("Exception when calling DeviceApi->enable_device: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Successful operation                       | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_device_connectivity_assurance**

> enable_device_connectivity_assurance(project_or_product_uid, device_uid)

Enable Connectivity Assurance

### Example

- Bearer Authentication (personalAccessToken):

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

# Configure Bearer authorization: personalAccessToken
configuration = notehub_py.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |

    try:
        api_instance.enable_device_connectivity_assurance(project_or_product_uid, device_uid)
    except Exception as e:
        print("Exception when calling DeviceApi->enable_device_connectivity_assurance: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Successful operation                       | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_db_note**

> GetDbNote200Response get_db_note(project_or_product_uid, device_uid, notefile_id, note_id, delete=delete, deleted=deleted)

Get a note from a .db or .qi notefile

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_db_note200_response import GetDbNote200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |
    notefile_id = 'notefile_id_example' # str |
    note_id = 'note_id_example' # str |
    delete = True # bool | Whether to delete the note from the DB notefile (optional)
    deleted = True # bool | Whether to return deleted notes (optional)

    try:
        api_response = api_instance.get_db_note(project_or_product_uid, device_uid, notefile_id, note_id, delete=delete, deleted=deleted)
        print("The response of DeviceApi->get_db_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_db_note: %s\n" % e)
```

### Parameters

| Name                       | Type     | Description                                     | Notes      |
| -------------------------- | -------- | ----------------------------------------------- | ---------- |
| **project_or_product_uid** | **str**  |                                                 |
| **device_uid**             | **str**  |                                                 |
| **notefile_id**            | **str**  |                                                 |
| **note_id**                | **str**  |                                                 |
| **delete**                 | **bool** | Whether to delete the note from the DB notefile | [optional] |
| **deleted**                | **bool** | Whether to return deleted notes                 | [optional] |

### Return type

[**GetDbNote200Response**](GetDbNote200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | The requested note                         | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device**

> Device get_device(project_or_product_uid, device_uid)

Get Device

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.device import Device
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |

    try:
        api_response = api_instance.get_device(project_or_product_uid, device_uid)
        print("The response of DeviceApi->get_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

[**Device**](Device.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Successful operation                       | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_environment_hierarchy**

> EnvTreeJsonNode get_device_environment_hierarchy(project_or_product_uid, device_uid)

Get environment variable hierarchy for a device

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.env_tree_json_node import EnvTreeJsonNode
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |

    try:
        # Get environment variable hierarchy for a device
        api_response = api_instance.get_device_environment_hierarchy(project_or_product_uid, device_uid)
        print("The response of DeviceApi->get_device_environment_hierarchy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_environment_hierarchy: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

[**EnvTreeJsonNode**](EnvTreeJsonNode.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                         | Response headers |
| ----------- | --------------------------------------------------- | ---------------- |
| **200**     | Successfully retrieved device environment hierarchy | -                |
| **404**     | Project or device not found                         | -                |
| **500**     | Server error                                        | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_environment_variables**

> GetDeviceEnvironmentVariablesByPin200Response get_device_environment_variables(project_or_product_uid, device_uid)

Get environment variables of a device

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_device_environment_variables_by_pin200_response import GetDeviceEnvironmentVariablesByPin200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |

    try:
        api_response = api_instance.get_device_environment_variables(project_or_product_uid, device_uid)
        print("The response of DeviceApi->get_device_environment_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_environment_variables: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

[**GetDeviceEnvironmentVariablesByPin200Response**](GetDeviceEnvironmentVariablesByPin200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                        | Response headers |
| ----------- | ------------------------------------------------------------------ | ---------------- |
| **200**     | The response body from a get device environment variables request. | -                |
| **0**       | The response body in case of an API error.                         | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_environment_variables_by_pin**

> GetDeviceEnvironmentVariablesByPin200Response get_device_environment_variables_by_pin(product_uid, device_uid, x_auth_token)

Get environment variables of a device with device pin authorization

### Example

```python
import notehub_py
from notehub_py.models.get_device_environment_variables_by_pin200_response import GetDeviceEnvironmentVariablesByPin200Response
from notehub_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.notefile.net
# See configuration.py for a list of all supported configuration parameters.
configuration = notehub_py.Configuration(
    host = "https://api.notefile.net"
)


# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    product_uid = 'com.blues.bridge:sensors' # str |
    device_uid = 'dev:000000000000000' # str |
    x_auth_token = 'x_auth_token_example' # str | For accessing endpoints by Device pin.

    try:
        api_response = api_instance.get_device_environment_variables_by_pin(product_uid, device_uid, x_auth_token)
        print("The response of DeviceApi->get_device_environment_variables_by_pin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_environment_variables_by_pin: %s\n" % e)
```

### Parameters

| Name             | Type    | Description                            | Notes |
| ---------------- | ------- | -------------------------------------- | ----- |
| **product_uid**  | **str** |                                        |
| **device_uid**   | **str** |                                        |
| **x_auth_token** | **str** | For accessing endpoints by Device pin. |

### Return type

[**GetDeviceEnvironmentVariablesByPin200Response**](GetDeviceEnvironmentVariablesByPin200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                                        | Response headers |
| ----------- | ------------------------------------------------------------------ | ---------------- |
| **200**     | The response body from a get device environment variables request. | -                |
| **0**       | The response body in case of an API error.                         | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_health_log**

> GetDeviceHealthLog200Response get_device_health_log(project_or_product_uid, device_uid, start_date=start_date, end_date=end_date, log_type=log_type)

Get Device Health Log

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_device_health_log200_response import GetDeviceHealthLog200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |
    start_date = 1628631763 # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210 # int | End date for filtering results, specified as a Unix timestamp (optional)
    log_type = ['log_type_example'] # List[str] | Return only specified log types (optional)

    try:
        api_response = api_instance.get_device_health_log(project_or_product_uid, device_uid, start_date=start_date, end_date=end_date, log_type=log_type)
        print("The response of DeviceApi->get_device_health_log:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_health_log: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                     | Notes      |
| -------------------------- | ----------------------- | --------------------------------------------------------------- | ---------- |
| **project_or_product_uid** | **str**                 |                                                                 |
| **device_uid**             | **str**                 |                                                                 |
| **start_date**             | **int**                 | Start date for filtering results, specified as a Unix timestamp | [optional] |
| **end_date**               | **int**                 | End date for filtering results, specified as a Unix timestamp   | [optional] |
| **log_type**               | [**List[str]**](str.md) | Return only specified log types                                 | [optional] |

### Return type

[**GetDeviceHealthLog200Response**](GetDeviceHealthLog200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Successful operation                       | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_latest_events**

> GetDeviceLatestEvents200Response get_device_latest_events(project_or_product_uid, device_uid)

Get Device Latest Events

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_device_latest_events200_response import GetDeviceLatestEvents200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |

    try:
        api_response = api_instance.get_device_latest_events(project_or_product_uid, device_uid)
        print("The response of DeviceApi->get_device_latest_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_latest_events: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

[**GetDeviceLatestEvents200Response**](GetDeviceLatestEvents200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                    | Response headers |
| ----------- | ---------------------------------------------- | ---------------- |
| **200**     | The response body for a Latest Events request. | -                |
| **0**       | The response body in case of an API error.     | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_plans**

> GetDevicePlans200Response get_device_plans(project_or_product_uid, device_uid)

Get Data Plans associated with the device, this include the primary sim, any external sim, as well as any satellite connections.

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_device_plans200_response import GetDevicePlans200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |

    try:
        api_response = api_instance.get_device_plans(project_or_product_uid, device_uid)
        print("The response of DeviceApi->get_device_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_plans: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

[**GetDevicePlans200Response**](GetDevicePlans200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Response body for /plans                   | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_public_key**

> GetDevicePublicKey200Response get_device_public_key(project_or_product_uid, device_uid)

Get Device Public Key

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_device_public_key200_response import GetDevicePublicKey200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |

    try:
        api_response = api_instance.get_device_public_key(project_or_product_uid, device_uid)
        print("The response of DeviceApi->get_device_public_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_public_key: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **device_uid**             | **str** |             |

### Return type

[**GetDevicePublicKey200Response**](GetDevicePublicKey200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Successful operation                       | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_public_keys**

> GetDevicePublicKeys200Response get_device_public_keys(project_or_product_uid, page_size=page_size, page_num=page_num)

Get Device Public Keys of a Project

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_device_public_keys200_response import GetDevicePublicKeys200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    page_size = 50 # int |  (optional) (default to 50)
    page_num = 1 # int |  (optional) (default to 1)

    try:
        api_response = api_instance.get_device_public_keys(project_or_product_uid, page_size=page_size, page_num=page_num)
        print("The response of DeviceApi->get_device_public_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_public_keys: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes                      |
| -------------------------- | ------- | ----------- | -------------------------- |
| **project_or_product_uid** | **str** |             |
| **page_size**              | **int** |             | [optional] [default to 50] |
| **page_num**               | **int** |             | [optional] [default to 1]  |

### Return type

[**GetDevicePublicKeys200Response**](GetDevicePublicKeys200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Successful operation                       | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_sessions**

> GetDeviceSessions200Response get_device_sessions(project_or_product_uid, device_uid, page_size=page_size, page_num=page_num, start_date=start_date, end_date=end_date)

Get Device Sessions

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_device_sessions200_response import GetDeviceSessions200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |
    page_size = 50 # int |  (optional) (default to 50)
    page_num = 1 # int |  (optional) (default to 1)
    start_date = 1628631763 # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210 # int | End date for filtering results, specified as a Unix timestamp (optional)

    try:
        api_response = api_instance.get_device_sessions(project_or_product_uid, device_uid, page_size=page_size, page_num=page_num, start_date=start_date, end_date=end_date)
        print("The response of DeviceApi->get_device_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_device_sessions: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                     | Notes                      |
| -------------------------- | ------- | --------------------------------------------------------------- | -------------------------- |
| **project_or_product_uid** | **str** |                                                                 |
| **device_uid**             | **str** |                                                                 |
| **page_size**              | **int** |                                                                 | [optional] [default to 50] |
| **page_num**               | **int** |                                                                 | [optional] [default to 1]  |
| **start_date**             | **int** | Start date for filtering results, specified as a Unix timestamp | [optional]                 |
| **end_date**               | **int** | End date for filtering results, specified as a Unix timestamp   | [optional]                 |

### Return type

[**GetDeviceSessions200Response**](GetDeviceSessions200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | The response body for a session request.   | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices**

> GetDevices200Response get_devices(project_or_product_uid, page_size=page_size, page_num=page_num, device_uid=device_uid, tag=tag, serial_number=serial_number, fleet_uid=fleet_uid, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku)

Get Devices of a Project

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_devices200_response import GetDevices200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    page_size = 50 # int |  (optional) (default to 50)
    page_num = 1 # int |  (optional) (default to 1)
    device_uid = ['device_uid_example'] # List[str] | A Device UID. (optional)
    tag = ['tag_example'] # List[str] | Tag filter (optional)
    serial_number = ['serial_number_example'] # List[str] | Serial number filter (optional)
    fleet_uid = ['fleet_uid_example'] # List[str] |  (optional)
    notecard_firmware = ['notecard_firmware_example'] # List[str] | Firmware version filter (optional)
    location = ['location_example'] # List[str] | Location filter (optional)
    host_firmware = ['host_firmware_example'] # List[str] | Host firmware filter (optional)
    product_uid = ['product_uid_example'] # List[str] |  (optional)
    sku = ['sku_example'] # List[str] | SKU filter (optional)

    try:
        api_response = api_instance.get_devices(project_or_product_uid, page_size=page_size, page_num=page_num, device_uid=device_uid, tag=tag, serial_number=serial_number, fleet_uid=fleet_uid, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku)
        print("The response of DeviceApi->get_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_devices: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description             | Notes                      |
| -------------------------- | ----------------------- | ----------------------- | -------------------------- |
| **project_or_product_uid** | **str**                 |                         |
| **page_size**              | **int**                 |                         | [optional] [default to 50] |
| **page_num**               | **int**                 |                         | [optional] [default to 1]  |
| **device_uid**             | [**List[str]**](str.md) | A Device UID.           | [optional]                 |
| **tag**                    | [**List[str]**](str.md) | Tag filter              | [optional]                 |
| **serial_number**          | [**List[str]**](str.md) | Serial number filter    | [optional]                 |
| **fleet_uid**              | [**List[str]**](str.md) |                         | [optional]                 |
| **notecard_firmware**      | [**List[str]**](str.md) | Firmware version filter | [optional]                 |
| **location**               | [**List[str]**](str.md) | Location filter         | [optional]                 |
| **host_firmware**          | [**List[str]**](str.md) | Host firmware filter    | [optional]                 |
| **product_uid**            | [**List[str]**](str.md) |                         | [optional]                 |
| **sku**                    | [**List[str]**](str.md) | SKU filter              | [optional]                 |

### Return type

[**GetDevices200Response**](GetDevices200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | List of Devices                            | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fleet_devices**

> GetDevices200Response get_fleet_devices(project_or_product_uid, fleet_uid, page_size=page_size, page_num=page_num, device_uid=device_uid, tag=tag, serial_number=serial_number, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku)

Get Devices of a Fleet within a Project

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_devices200_response import GetDevices200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    fleet_uid = 'fleet_uid_example' # str |
    page_size = 50 # int |  (optional) (default to 50)
    page_num = 1 # int |  (optional) (default to 1)
    device_uid = ['device_uid_example'] # List[str] | A Device UID. (optional)
    tag = ['tag_example'] # List[str] | Tag filter (optional)
    serial_number = ['serial_number_example'] # List[str] | Serial number filter (optional)
    notecard_firmware = ['notecard_firmware_example'] # List[str] | Firmware version filter (optional)
    location = ['location_example'] # List[str] | Location filter (optional)
    host_firmware = ['host_firmware_example'] # List[str] | Host firmware filter (optional)
    product_uid = ['product_uid_example'] # List[str] |  (optional)
    sku = ['sku_example'] # List[str] | SKU filter (optional)

    try:
        api_response = api_instance.get_fleet_devices(project_or_product_uid, fleet_uid, page_size=page_size, page_num=page_num, device_uid=device_uid, tag=tag, serial_number=serial_number, notecard_firmware=notecard_firmware, location=location, host_firmware=host_firmware, product_uid=product_uid, sku=sku)
        print("The response of DeviceApi->get_fleet_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_fleet_devices: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description             | Notes                      |
| -------------------------- | ----------------------- | ----------------------- | -------------------------- |
| **project_or_product_uid** | **str**                 |                         |
| **fleet_uid**              | **str**                 |                         |
| **page_size**              | **int**                 |                         | [optional] [default to 50] |
| **page_num**               | **int**                 |                         | [optional] [default to 1]  |
| **device_uid**             | [**List[str]**](str.md) | A Device UID.           | [optional]                 |
| **tag**                    | [**List[str]**](str.md) | Tag filter              | [optional]                 |
| **serial_number**          | [**List[str]**](str.md) | Serial number filter    | [optional]                 |
| **notecard_firmware**      | [**List[str]**](str.md) | Firmware version filter | [optional]                 |
| **location**               | [**List[str]**](str.md) | Location filter         | [optional]                 |
| **host_firmware**          | [**List[str]**](str.md) | Host firmware filter    | [optional]                 |
| **product_uid**            | [**List[str]**](str.md) |                         | [optional]                 |
| **sku**                    | [**List[str]**](str.md) | SKU filter              | [optional]                 |

### Return type

[**GetDevices200Response**](GetDevices200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | List of Devices                            | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notefile**

> GetNotefile200Response get_notefile(project_or_product_uid, device_uid, notefile_id, max=max, deleted=deleted, delete=delete)

For .qi files, returns the queued up notes. For .db files, returns all notes in the notefile

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_notefile200_response import GetNotefile200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |
    notefile_id = 'notefile_id_example' # str |
    max = 56 # int | The maximum number of Notes to return in the request. (optional)
    deleted = True # bool | true to return deleted notes. (optional)
    delete = True # bool | true to delete the notes returned by the request. (optional)

    try:
        api_response = api_instance.get_notefile(project_or_product_uid, device_uid, notefile_id, max=max, deleted=deleted, delete=delete)
        print("The response of DeviceApi->get_notefile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->get_notefile: %s\n" % e)
```

### Parameters

| Name                       | Type     | Description                                           | Notes      |
| -------------------------- | -------- | ----------------------------------------------------- | ---------- |
| **project_or_product_uid** | **str**  |                                                       |
| **device_uid**             | **str**  |                                                       |
| **notefile_id**            | **str**  |                                                       |
| **max**                    | **int**  | The maximum number of Notes to return in the request. | [optional] |
| **deleted**                | **bool** | true to return deleted notes.                         | [optional] |
| **delete**                 | **bool** | true to delete the notes returned by the request.     | [optional] |

### Return type

[**GetNotefile200Response**](GetNotefile200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | The note changes object                    | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notefiles**

> List[Notefile] list_notefiles(project_or_product_uid, device_uid, files=files, pending=pending)

Lists .qi and .db files for the device

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.notefile import Notefile
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |
    files = ['files_example'] # List[str] | One or more files to obtain change information from. (optional)
    pending = True # bool | show only files that are pending sync to the Notecard (optional)

    try:
        api_response = api_instance.list_notefiles(project_or_product_uid, device_uid, files=files, pending=pending)
        print("The response of DeviceApi->list_notefiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->list_notefiles: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                           | Notes      |
| -------------------------- | ----------------------- | ----------------------------------------------------- | ---------- |
| **project_or_product_uid** | **str**                 |                                                       |
| **device_uid**             | **str**                 |                                                       |
| **files**                  | [**List[str]**](str.md) | One or more files to obtain change information from.  | [optional] |
| **pending**                | **bool**                | show only files that are pending sync to the Notecard | [optional] |

### Return type

[**List[Notefile]**](Notefile.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | All notefiles and their notes              | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provision_device**

> object provision_device(project_or_product_uid, device_uid, provision_device_request)

Provision Device for a Project

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.provision_device_request import ProvisionDeviceRequest
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |
    provision_device_request = notehub_py.ProvisionDeviceRequest() # ProvisionDeviceRequest | Provision a device to a specific ProductUID

    try:
        api_response = api_instance.provision_device(project_or_product_uid, device_uid, provision_device_request)
        print("The response of DeviceApi->provision_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->provision_device: %s\n" % e)
```

### Parameters

| Name                         | Type                                                    | Description                                 | Notes |
| ---------------------------- | ------------------------------------------------------- | ------------------------------------------- | ----- |
| **project_or_product_uid**   | **str**                                                 |                                             |
| **device_uid**               | **str**                                                 |                                             |
| **provision_device_request** | [**ProvisionDeviceRequest**](ProvisionDeviceRequest.md) | Provision a device to a specific ProductUID |

### Return type

**object**

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Successful operation                       | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_device_environment_variables**

> EnvironmentVariables set_device_environment_variables(project_or_product_uid, device_uid, environment_variables)

Set environment variables of a device

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.environment_variables import EnvironmentVariables
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |
    environment_variables = notehub_py.EnvironmentVariables() # EnvironmentVariables | Environment variables to be added to the device

    try:
        api_response = api_instance.set_device_environment_variables(project_or_product_uid, device_uid, environment_variables)
        print("The response of DeviceApi->set_device_environment_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->set_device_environment_variables: %s\n" % e)
```

### Parameters

| Name                       | Type                                                | Description                                     | Notes |
| -------------------------- | --------------------------------------------------- | ----------------------------------------------- | ----- |
| **project_or_product_uid** | **str**                                             |                                                 |
| **device_uid**             | **str**                                             |                                                 |
| **environment_variables**  | [**EnvironmentVariables**](EnvironmentVariables.md) | Environment variables to be added to the device |

### Return type

[**EnvironmentVariables**](EnvironmentVariables.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                                              | Response headers |
| ----------- | -------------------------------------------------------- | ---------------- |
| **200**     | The response body from an environment variables request. | -                |
| **0**       | The response body in case of an API error.               | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_device_environment_variables_by_pin**

> EnvironmentVariables set_device_environment_variables_by_pin(product_uid, device_uid, x_auth_token, environment_variables)

Set environment variables of a device with device pin authorization

### Example

```python
import notehub_py
from notehub_py.models.environment_variables import EnvironmentVariables
from notehub_py.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.notefile.net
# See configuration.py for a list of all supported configuration parameters.
configuration = notehub_py.Configuration(
    host = "https://api.notefile.net"
)


# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DeviceApi(api_client)
    product_uid = 'com.blues.bridge:sensors' # str |
    device_uid = 'dev:000000000000000' # str |
    x_auth_token = 'x_auth_token_example' # str | For accessing endpoints by Device pin.
    environment_variables = notehub_py.EnvironmentVariables() # EnvironmentVariables | Environment variables to be added to the device

    try:
        api_response = api_instance.set_device_environment_variables_by_pin(product_uid, device_uid, x_auth_token, environment_variables)
        print("The response of DeviceApi->set_device_environment_variables_by_pin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->set_device_environment_variables_by_pin: %s\n" % e)
```

### Parameters

| Name                      | Type                                                | Description                                     | Notes |
| ------------------------- | --------------------------------------------------- | ----------------------------------------------- | ----- |
| **product_uid**           | **str**                                             |                                                 |
| **device_uid**            | **str**                                             |                                                 |
| **x_auth_token**          | **str**                                             | For accessing endpoints by Device pin.          |
| **environment_variables** | [**EnvironmentVariables**](EnvironmentVariables.md) | Environment variables to be added to the device |

### Return type

[**EnvironmentVariables**](EnvironmentVariables.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                                              | Response headers |
| ----------- | -------------------------------------------------------- | ---------------- |
| **200**     | The response body from an environment variables request. | -                |
| **0**       | The response body in case of an API error.               | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signal_device**

> SignalDevice200Response signal_device(project_or_product_uid, device_uid, body)

Send a signal from Notehub to a Notecard.

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.body import Body
from notehub_py.models.signal_device200_response import SignalDevice200Response
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |
    body = notehub_py.Body() # Body | Body or payload of signal to be sent to the device

    try:
        api_response = api_instance.signal_device(project_or_product_uid, device_uid, body)
        print("The response of DeviceApi->signal_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->signal_device: %s\n" % e)
```

### Parameters

| Name                       | Type                | Description                                        | Notes |
| -------------------------- | ------------------- | -------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**             |                                                    |
| **device_uid**             | **str**             |                                                    |
| **body**                   | [**Body**](Body.md) | Body or payload of signal to be sent to the device |

### Return type

[**SignalDevice200Response**](SignalDevice200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | A status response.                         | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_db_note**

> update_db_note(project_or_product_uid, device_uid, notefile_id, note_id, note_input)

Update a note in a .db or .qi notefile

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.note_input import NoteInput
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
    api_instance = notehub_py.DeviceApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    device_uid = 'dev:000000000000000' # str |
    notefile_id = 'notefile_id_example' # str |
    note_id = 'note_id_example' # str |
    note_input = notehub_py.NoteInput() # NoteInput | Body or payload of note to be added to the device

    try:
        api_instance.update_db_note(project_or_product_uid, device_uid, notefile_id, note_id, note_input)
    except Exception as e:
        print("Exception when calling DeviceApi->update_db_note: %s\n" % e)
```

### Parameters

| Name                       | Type                          | Description                                       | Notes |
| -------------------------- | ----------------------------- | ------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**                       |                                                   |
| **device_uid**             | **str**                       |                                                   |
| **notefile_id**            | **str**                       |                                                   |
| **note_id**                | **str**                       |                                                   |
| **note_input**             | [**NoteInput**](NoteInput.md) | Body or payload of note to be added to the device |

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
| **200**     | An empty object means success              | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
