# notehub_py.EventApi

All URIs are relative to *https://api.notefile.net*

| Method                                                                       | HTTP request                                                               | Description |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ----------- |
| [**get_fleet_events**](EventApi.md#get_fleet_events)                         | **GET** /v1/projects/{projectOrProductUID}/fleets/{fleetUID}/events        |
| [**get_fleet_events_by_cursor**](EventApi.md#get_fleet_events_by_cursor)     | **GET** /v1/projects/{projectOrProductUID}/fleets/{fleetUID}/events-cursor |
| [**get_project_events**](EventApi.md#get_project_events)                     | **GET** /v1/projects/{projectOrProductUID}/events                          |
| [**get_project_events_by_cursor**](EventApi.md#get_project_events_by_cursor) | **GET** /v1/projects/{projectOrProductUID}/events-cursor                   |
| [**get_route_logs_by_event**](EventApi.md#get_route_logs_by_event)           | **GET** /v1/projects/{projectOrProductUID}/events/{eventUID}/route-logs    |

# **get_fleet_events**

> GetProjectEvents200Response get_fleet_events(project_or_product_uid, fleet_uid, page_size=page_size, page_num=page_num, device_uid=device_uid, sort_by=sort_by, sort_order=sort_order, start_date=start_date, end_date=end_date, date_type=date_type, system_files_only=system_files_only, files=files, format=format, serial_number=serial_number, session_uid=session_uid, event_uid=event_uid, select_fields=select_fields)

Get Events of a Fleet

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_project_events200_response import GetProjectEvents200Response
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
    api_instance = notehub_py.EventApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    fleet_uid = 'fleet_uid_example' # str |
    page_size = 50 # int |  (optional) (default to 50)
    page_num = 1 # int |  (optional) (default to 1)
    device_uid = ['device_uid_example'] # List[str] | A Device UID. (optional)
    sort_by = 'captured' # str |  (optional) (default to 'captured')
    sort_order = 'asc' # str |  (optional) (default to 'asc')
    start_date = 1628631763 # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210 # int | End date for filtering results, specified as a Unix timestamp (optional)
    date_type = 'captured' # str | Which date to filter on, either 'captured' or 'uploaded'.  This will apply to the startDate and endDate parameters (optional) (default to 'captured')
    system_files_only = True # bool |  (optional)
    files = '_health.qo, data.qo' # str |  (optional)
    format = 'json' # str | Response format (JSON or CSV) (optional) (default to 'json')
    serial_number = ['serial_number_example'] # List[str] | Filter by Serial Number (optional)
    session_uid = ['session_uid_example'] # List[str] | Filter by Session UID (optional)
    event_uid = ['event_uid_example'] # List[str] | Filter by Event UID (optional)
    select_fields = 'select_fields_example' # str | Comma-separated list of fields to select from JSON payload (e.g., \"field1,field2.subfield,field3\"), this will reflect the columns in the CSV output. (optional)

    try:
        api_response = api_instance.get_fleet_events(project_or_product_uid, fleet_uid, page_size=page_size, page_num=page_num, device_uid=device_uid, sort_by=sort_by, sort_order=sort_order, start_date=start_date, end_date=end_date, date_type=date_type, system_files_only=system_files_only, files=files, format=format, serial_number=serial_number, session_uid=session_uid, event_uid=event_uid, select_fields=select_fields)
        print("The response of EventApi->get_fleet_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->get_fleet_events: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                                                                                                      | Notes                                      |
| -------------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **project_or_product_uid** | **str**                 |                                                                                                                                                                  |
| **fleet_uid**              | **str**                 |                                                                                                                                                                  |
| **page_size**              | **int**                 |                                                                                                                                                                  | [optional] [default to 50]                 |
| **page_num**               | **int**                 |                                                                                                                                                                  | [optional] [default to 1]                  |
| **device_uid**             | [**List[str]**](str.md) | A Device UID.                                                                                                                                                    | [optional]                                 |
| **sort_by**                | **str**                 |                                                                                                                                                                  | [optional] [default to &#39;captured&#39;] |
| **sort_order**             | **str**                 |                                                                                                                                                                  | [optional] [default to &#39;asc&#39;]      |
| **start_date**             | **int**                 | Start date for filtering results, specified as a Unix timestamp                                                                                                  | [optional]                                 |
| **end_date**               | **int**                 | End date for filtering results, specified as a Unix timestamp                                                                                                    | [optional]                                 |
| **date_type**              | **str**                 | Which date to filter on, either &#39;captured&#39; or &#39;uploaded&#39;. This will apply to the startDate and endDate parameters                                | [optional] [default to &#39;captured&#39;] |
| **system_files_only**      | **bool**                |                                                                                                                                                                  | [optional]                                 |
| **files**                  | **str**                 |                                                                                                                                                                  | [optional]                                 |
| **format**                 | **str**                 | Response format (JSON or CSV)                                                                                                                                    | [optional] [default to &#39;json&#39;]     |
| **serial_number**          | [**List[str]**](str.md) | Filter by Serial Number                                                                                                                                          | [optional]                                 |
| **session_uid**            | [**List[str]**](str.md) | Filter by Session UID                                                                                                                                            | [optional]                                 |
| **event_uid**              | [**List[str]**](str.md) | Filter by Event UID                                                                                                                                              | [optional]                                 |
| **select_fields**          | **str**                 | Comma-separated list of fields to select from JSON payload (e.g., \&quot;field1,field2.subfield,field3\&quot;), this will reflect the columns in the CSV output. | [optional]                                 |

### Return type

[**GetProjectEvents200Response**](GetProjectEvents200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description                                  | Response headers                                   |
| ----------- | -------------------------------------------- | -------------------------------------------------- |
| **200**     | The response body from a GET events request. | \* X-Has-More - True if there are more events <br> |
| **0**       | The response body in case of an API error.   | -                                                  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fleet_events_by_cursor**

> GetProjectEventsByCursor200Response get_fleet_events_by_cursor(project_or_product_uid, fleet_uid, limit=limit, cursor=cursor, sort_order=sort_order, system_files_only=system_files_only, files=files, device_uid=device_uid, start_date=start_date, end_date=end_date)

Get Events of a Fleet by cursor

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_project_events_by_cursor200_response import GetProjectEventsByCursor200Response
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
    api_instance = notehub_py.EventApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    fleet_uid = 'fleet_uid_example' # str |
    limit = 50 # int |  (optional) (default to 50)
    cursor = 'cursor_example' # str | A cursor, which can be obtained from the `next_cursor` value from a previous call to this endpoint. The results set returned will include this event as its first result if the given identifier is actually the UID of an event. If this event UID is not found, the parameter is ignored and the results set is the same as if the parameter was not included.  (optional)
    sort_order = 'asc' # str |  (optional) (default to 'asc')
    system_files_only = True # bool |  (optional)
    files = '_health.qo, data.qo' # str |  (optional)
    device_uid = ['device_uid_example'] # List[str] | A Device UID. (optional)
    start_date = 1628631763 # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210 # int | End date for filtering results, specified as a Unix timestamp (optional)

    try:
        api_response = api_instance.get_fleet_events_by_cursor(project_or_product_uid, fleet_uid, limit=limit, cursor=cursor, sort_order=sort_order, system_files_only=system_files_only, files=files, device_uid=device_uid, start_date=start_date, end_date=end_date)
        print("The response of EventApi->get_fleet_events_by_cursor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->get_fleet_events_by_cursor: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                                                                                                                                                                                                                                                                                                                | Notes                                 |
| -------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **project_or_product_uid** | **str**                 |                                                                                                                                                                                                                                                                                                                                                                            |
| **fleet_uid**              | **str**                 |                                                                                                                                                                                                                                                                                                                                                                            |
| **limit**                  | **int**                 |                                                                                                                                                                                                                                                                                                                                                                            | [optional] [default to 50]            |
| **cursor**                 | **str**                 | A cursor, which can be obtained from the &#x60;next_cursor&#x60; value from a previous call to this endpoint. The results set returned will include this event as its first result if the given identifier is actually the UID of an event. If this event UID is not found, the parameter is ignored and the results set is the same as if the parameter was not included. | [optional]                            |
| **sort_order**             | **str**                 |                                                                                                                                                                                                                                                                                                                                                                            | [optional] [default to &#39;asc&#39;] |
| **system_files_only**      | **bool**                |                                                                                                                                                                                                                                                                                                                                                                            | [optional]                            |
| **files**                  | **str**                 |                                                                                                                                                                                                                                                                                                                                                                            | [optional]                            |
| **device_uid**             | [**List[str]**](str.md) | A Device UID.                                                                                                                                                                                                                                                                                                                                                              | [optional]                            |
| **start_date**             | **int**                 | Start date for filtering results, specified as a Unix timestamp                                                                                                                                                                                                                                                                                                            | [optional]                            |
| **end_date**               | **int**                 | End date for filtering results, specified as a Unix timestamp                                                                                                                                                                                                                                                                                                              | [optional]                            |

### Return type

[**GetProjectEventsByCursor200Response**](GetProjectEventsByCursor200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                            | Response headers |
| ----------- | ------------------------------------------------------ | ---------------- |
| **200**     | The response body from a GET events by cursor request. | -                |
| **0**       | The response body in case of an API error.             | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_events**

> GetProjectEvents200Response get_project_events(project_or_product_uid, page_size=page_size, page_num=page_num, device_uid=device_uid, sort_by=sort_by, sort_order=sort_order, start_date=start_date, end_date=end_date, date_type=date_type, system_files_only=system_files_only, files=files, format=format, serial_number=serial_number, fleet_uid=fleet_uid, session_uid=session_uid, event_uid=event_uid, select_fields=select_fields)

Get Events of a Project

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_project_events200_response import GetProjectEvents200Response
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
    api_instance = notehub_py.EventApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    page_size = 50 # int |  (optional) (default to 50)
    page_num = 1 # int |  (optional) (default to 1)
    device_uid = ['device_uid_example'] # List[str] | A Device UID. (optional)
    sort_by = 'captured' # str |  (optional) (default to 'captured')
    sort_order = 'asc' # str |  (optional) (default to 'asc')
    start_date = 1628631763 # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210 # int | End date for filtering results, specified as a Unix timestamp (optional)
    date_type = 'captured' # str | Which date to filter on, either 'captured' or 'uploaded'.  This will apply to the startDate and endDate parameters (optional) (default to 'captured')
    system_files_only = True # bool |  (optional)
    files = '_health.qo, data.qo' # str |  (optional)
    format = 'json' # str | Response format (JSON or CSV) (optional) (default to 'json')
    serial_number = ['serial_number_example'] # List[str] | Filter by Serial Number (optional)
    fleet_uid = ['fleet_uid_example'] # List[str] | Filter by Fleet UID (optional)
    session_uid = ['session_uid_example'] # List[str] | Filter by Session UID (optional)
    event_uid = ['event_uid_example'] # List[str] | Filter by Event UID (optional)
    select_fields = 'select_fields_example' # str | Comma-separated list of fields to select from JSON payload (e.g., \"field1,field2.subfield,field3\"), this will reflect the columns in the CSV output. (optional)

    try:
        api_response = api_instance.get_project_events(project_or_product_uid, page_size=page_size, page_num=page_num, device_uid=device_uid, sort_by=sort_by, sort_order=sort_order, start_date=start_date, end_date=end_date, date_type=date_type, system_files_only=system_files_only, files=files, format=format, serial_number=serial_number, fleet_uid=fleet_uid, session_uid=session_uid, event_uid=event_uid, select_fields=select_fields)
        print("The response of EventApi->get_project_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->get_project_events: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                                                                                                      | Notes                                      |
| -------------------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **project_or_product_uid** | **str**                 |                                                                                                                                                                  |
| **page_size**              | **int**                 |                                                                                                                                                                  | [optional] [default to 50]                 |
| **page_num**               | **int**                 |                                                                                                                                                                  | [optional] [default to 1]                  |
| **device_uid**             | [**List[str]**](str.md) | A Device UID.                                                                                                                                                    | [optional]                                 |
| **sort_by**                | **str**                 |                                                                                                                                                                  | [optional] [default to &#39;captured&#39;] |
| **sort_order**             | **str**                 |                                                                                                                                                                  | [optional] [default to &#39;asc&#39;]      |
| **start_date**             | **int**                 | Start date for filtering results, specified as a Unix timestamp                                                                                                  | [optional]                                 |
| **end_date**               | **int**                 | End date for filtering results, specified as a Unix timestamp                                                                                                    | [optional]                                 |
| **date_type**              | **str**                 | Which date to filter on, either &#39;captured&#39; or &#39;uploaded&#39;. This will apply to the startDate and endDate parameters                                | [optional] [default to &#39;captured&#39;] |
| **system_files_only**      | **bool**                |                                                                                                                                                                  | [optional]                                 |
| **files**                  | **str**                 |                                                                                                                                                                  | [optional]                                 |
| **format**                 | **str**                 | Response format (JSON or CSV)                                                                                                                                    | [optional] [default to &#39;json&#39;]     |
| **serial_number**          | [**List[str]**](str.md) | Filter by Serial Number                                                                                                                                          | [optional]                                 |
| **fleet_uid**              | [**List[str]**](str.md) | Filter by Fleet UID                                                                                                                                              | [optional]                                 |
| **session_uid**            | [**List[str]**](str.md) | Filter by Session UID                                                                                                                                            | [optional]                                 |
| **event_uid**              | [**List[str]**](str.md) | Filter by Event UID                                                                                                                                              | [optional]                                 |
| **select_fields**          | **str**                 | Comma-separated list of fields to select from JSON payload (e.g., \&quot;field1,field2.subfield,field3\&quot;), this will reflect the columns in the CSV output. | [optional]                                 |

### Return type

[**GetProjectEvents200Response**](GetProjectEvents200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

### HTTP response details

| Status code | Description                                  | Response headers                                   |
| ----------- | -------------------------------------------- | -------------------------------------------------- |
| **200**     | The response body from a GET events request. | \* X-Has-More - True if there are more events <br> |
| **0**       | The response body in case of an API error.   | -                                                  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_events_by_cursor**

> GetProjectEventsByCursor200Response get_project_events_by_cursor(project_or_product_uid, limit=limit, cursor=cursor, sort_order=sort_order, system_files_only=system_files_only, files=files, fleet_uid=fleet_uid, device_uid=device_uid)

Get Events of a Project by cursor

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_project_events_by_cursor200_response import GetProjectEventsByCursor200Response
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
    api_instance = notehub_py.EventApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    limit = 50 # int |  (optional) (default to 50)
    cursor = 'cursor_example' # str | A cursor, which can be obtained from the `next_cursor` value from a previous call to this endpoint. The results set returned will include this event as its first result if the given identifier is actually the UID of an event. If this event UID is not found, the parameter is ignored and the results set is the same as if the parameter was not included.  (optional)
    sort_order = 'asc' # str |  (optional) (default to 'asc')
    system_files_only = True # bool |  (optional)
    files = '_health.qo, data.qo' # str |  (optional)
    fleet_uid = 'fleet_uid_example' # str |  (optional)
    device_uid = ['device_uid_example'] # List[str] | A Device UID. (optional)

    try:
        api_response = api_instance.get_project_events_by_cursor(project_or_product_uid, limit=limit, cursor=cursor, sort_order=sort_order, system_files_only=system_files_only, files=files, fleet_uid=fleet_uid, device_uid=device_uid)
        print("The response of EventApi->get_project_events_by_cursor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->get_project_events_by_cursor: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                                                                                                                                                                                                                                                                                                                | Notes                                 |
| -------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **project_or_product_uid** | **str**                 |                                                                                                                                                                                                                                                                                                                                                                            |
| **limit**                  | **int**                 |                                                                                                                                                                                                                                                                                                                                                                            | [optional] [default to 50]            |
| **cursor**                 | **str**                 | A cursor, which can be obtained from the &#x60;next_cursor&#x60; value from a previous call to this endpoint. The results set returned will include this event as its first result if the given identifier is actually the UID of an event. If this event UID is not found, the parameter is ignored and the results set is the same as if the parameter was not included. | [optional]                            |
| **sort_order**             | **str**                 |                                                                                                                                                                                                                                                                                                                                                                            | [optional] [default to &#39;asc&#39;] |
| **system_files_only**      | **bool**                |                                                                                                                                                                                                                                                                                                                                                                            | [optional]                            |
| **files**                  | **str**                 |                                                                                                                                                                                                                                                                                                                                                                            | [optional]                            |
| **fleet_uid**              | **str**                 |                                                                                                                                                                                                                                                                                                                                                                            | [optional]                            |
| **device_uid**             | [**List[str]**](str.md) | A Device UID.                                                                                                                                                                                                                                                                                                                                                              | [optional]                            |

### Return type

[**GetProjectEventsByCursor200Response**](GetProjectEventsByCursor200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description                                            | Response headers |
| ----------- | ------------------------------------------------------ | ---------------- |
| **200**     | The response body from a GET events by cursor request. | -                |
| **0**       | The response body in case of an API error.             | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_route_logs_by_event**

> List[RouteLog] get_route_logs_by_event(project_or_product_uid, event_uid)

Get Route Logs by Event UID

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.route_log import RouteLog
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
    api_instance = notehub_py.EventApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    event_uid = '4506f411-dea6-44a0-9743-1130f57d7747' # str |

    try:
        api_response = api_instance.get_route_logs_by_event(project_or_product_uid, event_uid)
        print("The response of EventApi->get_route_logs_by_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->get_route_logs_by_event: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **event_uid**              | **str** |             |

### Return type

[**List[RouteLog]**](RouteLog.md)

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
