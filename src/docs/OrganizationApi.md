# notehub_py.OrganizationApi

All URIs are relative to *https://api.notefile.net*

| Method                                                                                      | HTTP request                                                | Description |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ----------- |
| [**get_organization**](OrganizationApi.md#get_organization)                                 | **GET** /v1/organizations/{organizationUID}                 |
| [**get_organization_balance_history**](OrganizationApi.md#get_organization_balance_history) | **GET** /v1/organizations/{organizationUID}/balance-history |
| [**get_organizations**](OrganizationApi.md#get_organizations)                               | **GET** /v1/organizations                                   |

## get_organization

> GetBillingAccount200Response get_organization(organization_uid)

Get Organization Information

### Example

```python
import notehub_py
from notehub_py.models.get_billing_account200_response import (
    GetBillingAccount200Response,
)
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.OrganizationApi(api_client)
    organization_uid = "00000000-0000-0000-000000000001"  # str |

    try:
        api_response = api_instance.get_organization(organization_uid)
        print("The response of OrganizationApi->get_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_organization: %s\n" % e)
```

### Parameters

| Name                 | Type    | Description | Notes |
| -------------------- | ------- | ----------- | ----- |
| **organization_uid** | **str** |             |

### Return type

[**GetBillingAccount200Response**](GetBillingAccount200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_organization_balance_history

> GetBillingAccountBalanceHistory200Response get_organization_balance_history(organization_uid, start_date=start_date, end_date=end_date)

Get Organization Balance history

### Example

```python
import notehub_py
from notehub_py.models.get_billing_account_balance_history200_response import (
    GetBillingAccountBalanceHistory200Response,
)
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.OrganizationApi(api_client)
    organization_uid = "00000000-0000-0000-000000000001"  # str |
    start_date = 1628631763  # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210  # int | End date for filtering results, specified as a Unix timestamp (optional)

    try:
        api_response = api_instance.get_organization_balance_history(
            organization_uid, start_date=start_date, end_date=end_date
        )
        print("The response of OrganizationApi->get_organization_balance_history:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling OrganizationApi->get_organization_balance_history: %s\n"
            % e
        )
```

### Parameters

| Name                 | Type    | Description                                                     | Notes      |
| -------------------- | ------- | --------------------------------------------------------------- | ---------- |
| **organization_uid** | **str** |                                                                 |
| **start_date**       | **int** | Start date for filtering results, specified as a Unix timestamp | [optional] |
| **end_date**         | **int** | End date for filtering results, specified as a Unix timestamp   | [optional] |

### Return type

[**GetBillingAccountBalanceHistory200Response**](GetBillingAccountBalanceHistory200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_organizations

> GetOrganizations200Response get_organizations()

Get Organizations accessible by the api_key

### Example

```python
import notehub_py
from notehub_py.models.get_organizations200_response import GetOrganizations200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.OrganizationApi(api_client)

    try:
        api_response = api_instance.get_organizations()
        print("The response of OrganizationApi->get_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_organizations: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetOrganizations200Response**](GetOrganizations200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json
