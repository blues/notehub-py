# notehub_py.RouteApi

All URIs are relative to *https://api.notefile.net*

| Method                                                             | HTTP request                                                            | Description |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------- | ----------- |
| [**create_route**](RouteApi.md#create_route)                       | **POST** /v1/projects/{projectOrProductUID}/routes                      |
| [**delete_route**](RouteApi.md#delete_route)                       | **DELETE** /v1/projects/{projectOrProductUID}/routes/{routeUID}         |
| [**get_route**](RouteApi.md#get_route)                             | **GET** /v1/projects/{projectOrProductUID}/routes/{routeUID}            |
| [**get_route_logs_by_route**](RouteApi.md#get_route_logs_by_route) | **GET** /v1/projects/{projectOrProductUID}/routes/{routeUID}/route-logs |
| [**get_routes**](RouteApi.md#get_routes)                           | **GET** /v1/projects/{projectOrProductUID}/routes                       |
| [**update_route**](RouteApi.md#update_route)                       | **PUT** /v1/projects/{projectOrProductUID}/routes/{routeUID}            |

# **create_route**

> NotehubRoute create_route(project_or_product_uid, notehub_route)

Create Route within a Project

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.notehub_route import NotehubRoute
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
    api_instance = notehub_py.RouteApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    notehub_route = {"http":{"disable_http_headers":false,"filter":{},"fleets":["fleet:1042ddc5-3b2c-4cec-b1fb-d3040538094d"],"http_headers":{"X-My-Header":"value"},"throttle_ms":100,"timeout":5000,"transform":{},"url":"https://example.com/ingest"},"label":"Route Label"} # NotehubRoute | Route to be created

    try:
        api_response = api_instance.create_route(project_or_product_uid, notehub_route)
        print("The response of RouteApi->create_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->create_route: %s\n" % e)
```

### Parameters

| Name                       | Type                                | Description         | Notes |
| -------------------------- | ----------------------------------- | ------------------- | ----- |
| **project_or_product_uid** | **str**                             |                     |
| **notehub_route**          | [**NotehubRoute**](NotehubRoute.md) | Route to be created |

### Return type

[**NotehubRoute**](NotehubRoute.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                                | Response headers |
| ----------- | ------------------------------------------ | ---------------- |
| **201**     | Created                                    | -                |
| **0**       | The response body in case of an API error. | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_route**

> delete_route(project_or_product_uid, route_uid)

Delete single route within a project

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
    api_instance = notehub_py.RouteApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    route_uid = 'route:cbd20093cba58392c9f9bbdd0cdeb1a0' # str |

    try:
        api_instance.delete_route(project_or_product_uid, route_uid)
    except Exception as e:
        print("Exception when calling RouteApi->delete_route: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **route_uid**              | **str** |             |

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

# **get_route**

> NotehubRoute get_route(project_or_product_uid, route_uid)

Get single route within a project

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.notehub_route import NotehubRoute
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
    api_instance = notehub_py.RouteApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    route_uid = 'route:cbd20093cba58392c9f9bbdd0cdeb1a0' # str |

    try:
        api_response = api_instance.get_route(project_or_product_uid, route_uid)
        print("The response of RouteApi->get_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->get_route: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **route_uid**              | **str** |             |

### Return type

[**NotehubRoute**](NotehubRoute.md)

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

# **get_route_logs_by_route**

> List[RouteLog] get_route_logs_by_route(project_or_product_uid, route_uid, page_size=page_size, page_num=page_num, device_uid=device_uid, sort_by=sort_by, sort_order=sort_order, start_date=start_date, end_date=end_date, system_files_only=system_files_only, most_recent_only=most_recent_only, files=files)

Get Route Logs by Route UID

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
    api_instance = notehub_py.RouteApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    route_uid = 'route:cbd20093cba58392c9f9bbdd0cdeb1a0' # str |
    page_size = 50 # int |  (optional) (default to 50)
    page_num = 1 # int |  (optional) (default to 1)
    device_uid = ['device_uid_example'] # List[str] | A Device UID. (optional)
    sort_by = 'date' # str |  (optional) (default to 'date')
    sort_order = 'desc' # str |  (optional) (default to 'desc')
    start_date = 1628631763 # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210 # int | End date for filtering results, specified as a Unix timestamp (optional)
    system_files_only = True # bool |  (optional)
    most_recent_only = True # bool |  (optional)
    files = '_health.qo, data.qo' # str |  (optional)

    try:
        api_response = api_instance.get_route_logs_by_route(project_or_product_uid, route_uid, page_size=page_size, page_num=page_num, device_uid=device_uid, sort_by=sort_by, sort_order=sort_order, start_date=start_date, end_date=end_date, system_files_only=system_files_only, most_recent_only=most_recent_only, files=files)
        print("The response of RouteApi->get_route_logs_by_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->get_route_logs_by_route: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                     | Notes                                  |
| -------------------------- | ----------------------- | --------------------------------------------------------------- | -------------------------------------- |
| **project_or_product_uid** | **str**                 |                                                                 |
| **route_uid**              | **str**                 |                                                                 |
| **page_size**              | **int**                 |                                                                 | [optional] [default to 50]             |
| **page_num**               | **int**                 |                                                                 | [optional] [default to 1]              |
| **device_uid**             | [**List[str]**](str.md) | A Device UID.                                                   | [optional]                             |
| **sort_by**                | **str**                 |                                                                 | [optional] [default to &#39;date&#39;] |
| **sort_order**             | **str**                 |                                                                 | [optional] [default to &#39;desc&#39;] |
| **start_date**             | **int**                 | Start date for filtering results, specified as a Unix timestamp | [optional]                             |
| **end_date**               | **int**                 | End date for filtering results, specified as a Unix timestamp   | [optional]                             |
| **system_files_only**      | **bool**                |                                                                 | [optional]                             |
| **most_recent_only**       | **bool**                |                                                                 | [optional]                             |
| **files**                  | **str**                 |                                                                 | [optional]                             |

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

# **get_routes**

> List[NotehubRouteSummary] get_routes(project_or_product_uid)

Get all Routes within a Project

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.notehub_route_summary import NotehubRouteSummary
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
    api_instance = notehub_py.RouteApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |

    try:
        api_response = api_instance.get_routes(project_or_product_uid)
        print("The response of RouteApi->get_routes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->get_routes: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |

### Return type

[**List[NotehubRouteSummary]**](NotehubRouteSummary.md)

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

# **update_route**

> NotehubRoute update_route(project_or_product_uid, route_uid, notehub_route)

Update route by UID

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.notehub_route import NotehubRoute
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
    api_instance = notehub_py.RouteApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    route_uid = 'route:cbd20093cba58392c9f9bbdd0cdeb1a0' # str |
    notehub_route = {
  "http" {
    "filter": {
      "type": "include",
      "system_notefiles": true,
      "files": ["somefile.qo"],
    },
    "throttle_ms": 50,
    "url": "http://new-route.url",
  },
}
 # NotehubRoute | Route settings to be updated

    try:
        api_response = api_instance.update_route(project_or_product_uid, route_uid, notehub_route)
        print("The response of RouteApi->update_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->update_route: %s\n" % e)
```

### Parameters

| Name                       | Type                                | Description                  | Notes |
| -------------------------- | ----------------------------------- | ---------------------------- | ----- |
| **project_or_product_uid** | **str**                             |                              |
| **route_uid**              | **str**                             |                              |
| **notehub_route**          | [**NotehubRoute**](NotehubRoute.md) | Route settings to be updated |

### Return type

[**NotehubRoute**](NotehubRoute.md)

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
