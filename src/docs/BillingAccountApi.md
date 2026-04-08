# notehub_py.BillingAccountApi

All URIs are relative to *https://api.notefile.net*

| Method                                                                                              | HTTP request                                                     | Description |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ----------- |
| [**get_billing_account**](BillingAccountApi.md#get_billing_account)                                 | **GET** /v1/billing-accounts/{billingAccountUID}                 |
| [**get_billing_account_balance_history**](BillingAccountApi.md#get_billing_account_balance_history) | **GET** /v1/billing-accounts/{billingAccountUID}/balance-history |
| [**get_billing_accounts**](BillingAccountApi.md#get_billing_accounts)                               | **GET** /v1/billing-accounts                                     |

## get_billing_account

> GetBillingAccount200Response get_billing_account(billing_account_uid)

Get Billing Account Information

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_billing_account200_response import GetBillingAccount200Response
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
    api_instance = notehub_py.BillingAccountApi(api_client)
    billing_account_uid = '00000000-0000-0000-000000000001' # str |

    try:
        api_response = api_instance.get_billing_account(billing_account_uid)
        print("The response of BillingAccountApi->get_billing_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingAccountApi->get_billing_account: %s\n" % e)
```

### Parameters

| Name                    | Type    | Description | Notes |
| ----------------------- | ------- | ----------- | ----- |
| **billing_account_uid** | **str** |             |

### Return type

[**GetBillingAccount200Response**](GetBillingAccount200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_billing_account_balance_history

> GetBillingAccountBalanceHistory200Response get_billing_account_balance_history(billing_account_uid, start_date=start_date, end_date=end_date)

Get Billing Account Balance history, only enterprise supported

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_billing_account_balance_history200_response import GetBillingAccountBalanceHistory200Response
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
    api_instance = notehub_py.BillingAccountApi(api_client)
    billing_account_uid = '00000000-0000-0000-000000000001' # str |
    start_date = 1628631763 # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210 # int | End date for filtering results, specified as a Unix timestamp (optional)

    try:
        api_response = api_instance.get_billing_account_balance_history(billing_account_uid, start_date=start_date, end_date=end_date)
        print("The response of BillingAccountApi->get_billing_account_balance_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingAccountApi->get_billing_account_balance_history: %s\n" % e)
```

### Parameters

| Name                    | Type    | Description                                                     | Notes      |
| ----------------------- | ------- | --------------------------------------------------------------- | ---------- |
| **billing_account_uid** | **str** |                                                                 |
| **start_date**          | **int** | Start date for filtering results, specified as a Unix timestamp | [optional] |
| **end_date**            | **int** | End date for filtering results, specified as a Unix timestamp   | [optional] |

### Return type

[**GetBillingAccountBalanceHistory200Response**](GetBillingAccountBalanceHistory200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_billing_accounts

> GetBillingAccounts200Response get_billing_accounts()

Get Billing Accounts accessible by the api_key

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_billing_accounts200_response import GetBillingAccounts200Response
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
    api_instance = notehub_py.BillingAccountApi(api_client)

    try:
        api_response = api_instance.get_billing_accounts()
        print("The response of BillingAccountApi->get_billing_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingAccountApi->get_billing_accounts: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetBillingAccounts200Response**](GetBillingAccounts200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json
