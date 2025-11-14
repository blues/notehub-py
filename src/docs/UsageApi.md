# notehub_py.UsageApi

All URIs are relative to *https://api.notefile.net*

| Method                                                   | HTTP request                                              | Description |
| -------------------------------------------------------- | --------------------------------------------------------- | ----------- |
| [**get_data_usage**](UsageApi.md#get_data_usage)         | **GET** /v1/projects/{projectOrProductUID}/usage/data     |
| [**get_events_usage**](UsageApi.md#get_events_usage)     | **GET** /v1/projects/{projectOrProductUID}/usage/events   |
| [**get_sessions_usage**](UsageApi.md#get_sessions_usage) | **GET** /v1/projects/{projectOrProductUID}/usage/sessions |

# **get_data_usage**

> GetDataUsage200Response get_data_usage(project_or_product_uid, period, start_date=start_date, end_date=end_date, device_uid=device_uid, fleet_uid=fleet_uid, aggregate=aggregate)

Get data usage in bytes for a project with time range and period aggregation

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_data_usage200_response import GetDataUsage200Response
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
    api_instance = notehub_py.UsageApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    period = 'period_example' # str | Period type for aggregation
    start_date = 1628631763 # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210 # int | End date for filtering results, specified as a Unix timestamp (optional)
    device_uid = ['device_uid_example'] # List[str] | A Device UID. (optional)
    fleet_uid = ['fleet_uid_example'] # List[str] | Filter by Fleet UID (optional)
    aggregate = 'device' # str | Aggregation level for results (optional) (default to 'device')

    try:
        api_response = api_instance.get_data_usage(project_or_product_uid, period, start_date=start_date, end_date=end_date, device_uid=device_uid, fleet_uid=fleet_uid, aggregate=aggregate)
        print("The response of UsageApi->get_data_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_data_usage: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                     | Notes                                    |
| -------------------------- | ----------------------- | --------------------------------------------------------------- | ---------------------------------------- |
| **project_or_product_uid** | **str**                 |                                                                 |
| **period**                 | **str**                 | Period type for aggregation                                     |
| **start_date**             | **int**                 | Start date for filtering results, specified as a Unix timestamp | [optional]                               |
| **end_date**               | **int**                 | End date for filtering results, specified as a Unix timestamp   | [optional]                               |
| **device_uid**             | [**List[str]**](str.md) | A Device UID.                                                   | [optional]                               |
| **fleet_uid**              | [**List[str]**](str.md) | Filter by Fleet UID                                             | [optional]                               |
| **aggregate**              | **str**                 | Aggregation level for results                                   | [optional] [default to &#39;device&#39;] |

### Return type

[**GetDataUsage200Response**](GetDataUsage200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Response body for Data Usage               | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_usage**

> UsageEventsResponse get_events_usage(project_or_product_uid, period, start_date=start_date, end_date=end_date, device_uid=device_uid, fleet_uid=fleet_uid, aggregate=aggregate)

Get events usage for a project with time range and period aggregation, when endDate is 0 or unspecified the current time is implied

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.usage_events_response import UsageEventsResponse
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
    api_instance = notehub_py.UsageApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    period = 'period_example' # str | Period type for aggregation
    start_date = 1628631763 # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210 # int | End date for filtering results, specified as a Unix timestamp (optional)
    device_uid = ['device_uid_example'] # List[str] | A Device UID. (optional)
    fleet_uid = ['fleet_uid_example'] # List[str] | Filter by Fleet UID (optional)
    aggregate = 'device' # str | Aggregation level for results (optional) (default to 'device')

    try:
        api_response = api_instance.get_events_usage(project_or_product_uid, period, start_date=start_date, end_date=end_date, device_uid=device_uid, fleet_uid=fleet_uid, aggregate=aggregate)
        print("The response of UsageApi->get_events_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_events_usage: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                     | Notes                                    |
| -------------------------- | ----------------------- | --------------------------------------------------------------- | ---------------------------------------- |
| **project_or_product_uid** | **str**                 |                                                                 |
| **period**                 | **str**                 | Period type for aggregation                                     |
| **start_date**             | **int**                 | Start date for filtering results, specified as a Unix timestamp | [optional]                               |
| **end_date**               | **int**                 | End date for filtering results, specified as a Unix timestamp   | [optional]                               |
| **device_uid**             | [**List[str]**](str.md) | A Device UID.                                                   | [optional]                               |
| **fleet_uid**              | [**List[str]**](str.md) | Filter by Fleet UID                                             | [optional]                               |
| **aggregate**              | **str**                 | Aggregation level for results                                   | [optional] [default to &#39;device&#39;] |

### Return type

[**UsageEventsResponse**](UsageEventsResponse.md)

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

# **get_sessions_usage**

> GetSessionsUsage200Response get_sessions_usage(project_or_product_uid, period, start_date=start_date, end_date=end_date, device_uid=device_uid, fleet_uid=fleet_uid, aggregate=aggregate)

Get sessions usage for a project with time range and period aggregation, when endDate is 0 or unspecified the current time is implied

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_sessions_usage200_response import GetSessionsUsage200Response
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
    api_instance = notehub_py.UsageApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    period = 'period_example' # str | Period type for aggregation
    start_date = 1628631763 # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210 # int | End date for filtering results, specified as a Unix timestamp (optional)
    device_uid = ['device_uid_example'] # List[str] | A Device UID. (optional)
    fleet_uid = ['fleet_uid_example'] # List[str] | Filter by Fleet UID (optional)
    aggregate = 'device' # str | Aggregation level for results (optional) (default to 'device')

    try:
        api_response = api_instance.get_sessions_usage(project_or_product_uid, period, start_date=start_date, end_date=end_date, device_uid=device_uid, fleet_uid=fleet_uid, aggregate=aggregate)
        print("The response of UsageApi->get_sessions_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_sessions_usage: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                     | Notes                                    |
| -------------------------- | ----------------------- | --------------------------------------------------------------- | ---------------------------------------- |
| **project_or_product_uid** | **str**                 |                                                                 |
| **period**                 | **str**                 | Period type for aggregation                                     |
| **start_date**             | **int**                 | Start date for filtering results, specified as a Unix timestamp | [optional]                               |
| **end_date**               | **int**                 | End date for filtering results, specified as a Unix timestamp   | [optional]                               |
| **device_uid**             | [**List[str]**](str.md) | A Device UID.                                                   | [optional]                               |
| **fleet_uid**              | [**List[str]**](str.md) | Filter by Fleet UID                                             | [optional]                               |
| **aggregate**              | **str**                 | Aggregation level for results                                   | [optional] [default to &#39;device&#39;] |

### Return type

[**GetSessionsUsage200Response**](GetSessionsUsage200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **200**     | Response body for Session Usage            | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
