# notehub_py.AuthorizationApi

All URIs are relative to *https://api.notefile.net*

| Method                                                                           | HTTP request           | Description                                          |
| -------------------------------------------------------------------------------- | ---------------------- | ---------------------------------------------------- |
| [**login**](AuthorizationApi.md#login)                                           | **POST** /auth/login   |
| [**o_auth2_client_credentials**](AuthorizationApi.md#o_auth2_client_credentials) | **POST** /oauth2/token | Issue an OAuth 2.0 access token (Client Credentials) |

# **login**

> Login200Response login(login_request)

Gets an API key from username and password

### Example

```python
import notehub_py
from notehub_py.models.login200_response import Login200Response
from notehub_py.models.login_request import LoginRequest
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
    api_instance = notehub_py.AuthorizationApi(api_client)
    login_request = {"password":"test-password","username":"name@example.com"} # LoginRequest |

    try:
        api_response = api_instance.login(login_request)
        print("The response of AuthorizationApi->login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationApi->login: %s\n" % e)
```

### Parameters

| Name              | Type                                | Description | Notes |
| ----------------- | ----------------------------------- | ----------- | ----- |
| **login_request** | [**LoginRequest**](LoginRequest.md) |             |

### Return type

[**Login200Response**](Login200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description           | Response headers |
| ----------- | --------------------- | ---------------- |
| **200**     | Successful operation  | -                |
| **400**     | Bad Request           | -                |
| **500**     | Internal Server Error | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **o_auth2_client_credentials**

> OAuth2TokenResponse o_auth2_client_credentials(client_id, client_secret, grant_type, scope=scope)

Issue an OAuth 2.0 access token (Client Credentials)

Exchanges client credentials for an access token. Parameters must be sent as application/x-www-form-urlencoded.

### Example

```python
import notehub_py
from notehub_py.models.o_auth2_token_response import OAuth2TokenResponse
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
    api_instance = notehub_py.AuthorizationApi(api_client)
    client_id = 'client_id_example' # str |
    client_secret = 'client_secret_example' # str |
    grant_type = 'grant_type_example' # str |
    scope = 'scope_example' # str | Space-delimited scopes. (optional)

    try:
        # Issue an OAuth 2.0 access token (Client Credentials)
        api_response = api_instance.o_auth2_client_credentials(client_id, client_secret, grant_type, scope=scope)
        print("The response of AuthorizationApi->o_auth2_client_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationApi->o_auth2_client_credentials: %s\n" % e)
```

### Parameters

| Name              | Type    | Description             | Notes      |
| ----------------- | ------- | ----------------------- | ---------- |
| **client_id**     | **str** |                         |
| **client_secret** | **str** |                         |
| **grant_type**    | **str** |                         |
| **scope**         | **str** | Space-delimited scopes. | [optional] |

### Return type

[**OAuth2TokenResponse**](OAuth2TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

### HTTP response details

| Status code | Description                                       | Response headers |
| ----------- | ------------------------------------------------- | ---------------- |
| **200**     | Successful token response                         | -                |
| **400**     | Invalid request (missing or malformed parameters) | -                |
| **401**     | Invalid client authentication                     | -                |
| **403**     | Unauthorized scope                                | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
