# notehub_py.AuthorizationApi

All URIs are relative to *https://api.notefile.net*

| Method                                                                           | HTTP request           | Description                                       |
| -------------------------------------------------------------------------------- | ---------------------- | ------------------------------------------------- |
| [**o_auth2_client_credentials**](AuthorizationApi.md#o_auth2_client_credentials) | **POST** /oauth2/token | Get an access token with OAuth client credentials |

## o_auth2_client_credentials

> OAuth2TokenResponse o_auth2_client_credentials(client_id, client_secret, grant_type, scope=scope)

Get an access token with OAuth client credentials

Exchange an OAuth client's ID and secret for a bearer access token, using the OAuth 2.0 client credentials grant. Send the parameters form-encoded, not as JSON. Returns 401 for a bad client ID or secret, and 403 for a scope the client can't have.

### Example

```python
import notehub_py
from notehub_py.models.o_auth2_token_response import OAuth2TokenResponse
from notehub_py.rest import ApiException
from pprint import pprint


# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.AuthorizationApi(api_client)
    client_id = "client_id_example"  # str |
    client_secret = "client_secret_example"  # str |
    grant_type = "grant_type_example"  # str |
    scope = "scope_example"  # str | Space-delimited scopes. (optional)

    try:
        # Get an access token with OAuth client credentials
        api_response = api_instance.o_auth2_client_credentials(
            client_id, client_secret, grant_type, scope=scope
        )
        print("The response of AuthorizationApi->o_auth2_client_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling AuthorizationApi->o_auth2_client_credentials: %s\n"
            % e
        )
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
