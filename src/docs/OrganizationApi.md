# notehub_py.OrganizationApi

All URIs are relative to *https://api.notefile.net*

| Method                                                                                      | HTTP request                                                | Description                             |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | --------------------------------------- |
| [**get_organization**](OrganizationApi.md#get_organization)                                 | **GET** /v1/organizations/{organizationUID}                 | Get an organization                     |
| [**get_organization_balance_history**](OrganizationApi.md#get_organization_balance_history) | **GET** /v1/organizations/{organizationUID}/balance-history | Get an organization&#39;s daily balance |
| [**get_organizations**](OrganizationApi.md#get_organizations)                               | **GET** /v1/organizations                                   | List your organizations                 |

## get_organization

> GetOrganization200Response get_organization(organization_uid)

Get an organization

Get an organization's name, owner, contact email and current plan. The plan has its type, event capacity, billing period and remaining balance. For the daily history, use `GetOrganizationBalanceHistory`. Requires the `org_admin`, `billing_manager` or `org_support` role in the organization. Returns 403 if your membership is deactivated.

### Example

```python
import notehub_py
from notehub_py.models.get_organization200_response import GetOrganization200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.OrganizationApi(api_client)
    organization_uid = "00000000-0000-0000-000000000001"  # str | Organization UID. List with `GetOrganizations`.

    try:
        # Get an organization
        api_response = api_instance.get_organization(organization_uid)
        print("The response of OrganizationApi->get_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_organization: %s\n" % e)
```

### Parameters

| Name                 | Type    | Description                                               | Notes |
| -------------------- | ------- | --------------------------------------------------------- | ----- |
| **organization_uid** | **str** | Organization UID. List with &#x60;GetOrganizations&#x60;. |

### Return type

[**GetOrganization200Response**](GetOrganization200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_organization_balance_history

> GetOrganizationBalanceHistory200Response get_organization_balance_history(organization_uid, start_date=start_date, end_date=end_date)

Get an organization's daily balance

Get an organization's events used and remaining event capacity for each day. The range is `startDate` to `endDate`, which default to the start of the billing period and today. Requires the `org_admin`, `billing_manager` or `org_support` role in the organization. Returns 400 if `startDate` is after `endDate`.

### Example

```python
import notehub_py
from notehub_py.models.get_organization_balance_history200_response import (
    GetOrganizationBalanceHistory200Response,
)
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.OrganizationApi(api_client)
    organization_uid = "00000000-0000-0000-000000000001"  # str | Organization UID. List with `GetOrganizations`.
    start_date = 1628631763  # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210  # int | End date for filtering results, specified as a Unix timestamp (optional)

    try:
        # Get an organization's daily balance
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
| **organization_uid** | **str** | Organization UID. List with &#x60;GetOrganizations&#x60;.       |
| **start_date**       | **int** | Start date for filtering results, specified as a Unix timestamp | [optional] |
| **end_date**         | **int** | End date for filtering results, specified as a Unix timestamp   | [optional] |

### Return type

[**GetOrganizationBalanceHistory200Response**](GetOrganizationBalanceHistory200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_organizations

> GetOrganizations200Response get_organizations()

List your organizations

List the organizations you belong to, with your role in each. A scoped token gets an empty list. Returns 401 if your email address isn't verified.

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
        # List your organizations
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
