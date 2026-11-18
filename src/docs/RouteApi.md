# notehub_py.RouteApi

All URIs are relative to *https://api.notefile.net*

| Method                                                             | HTTP request                                                            | Description             |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------- | ----------------------- |
| [**create_route**](RouteApi.md#create_route)                       | **POST** /v1/projects/{projectOrProductUID}/routes                      | Create a route          |
| [**delete_route**](RouteApi.md#delete_route)                       | **DELETE** /v1/projects/{projectOrProductUID}/routes/{routeUID}         | Delete a route          |
| [**get_route**](RouteApi.md#get_route)                             | **GET** /v1/projects/{projectOrProductUID}/routes/{routeUID}            | Get a route             |
| [**get_route_logs_by_route**](RouteApi.md#get_route_logs_by_route) | **GET** /v1/projects/{projectOrProductUID}/routes/{routeUID}/route-logs | List a route&#39;s logs |
| [**get_routes**](RouteApi.md#get_routes)                           | **GET** /v1/projects/{projectOrProductUID}/routes                       | List routes             |
| [**update_route**](RouteApi.md#update_route)                       | **PUT** /v1/projects/{projectOrProductUID}/routes/{routeUID}            | Update a route          |

## create_route

> NotehubRoute create_route(project_or_product_uid, notehub_route)

Create a route

Create a route that sends a project's events to a destination such as a URL, an MQTT broker or a cloud service. Set `type` and fill in the object it names. Omit `fleets` to send every fleet's events. Unknown FleetUIDs are ignored, so `fleets: []` or a list of only unknown UIDs gives a route that sends nothing. Requires the Owner or Developer role. Returns 400 for invalid settings.

### Example

```python
import notehub_py
from notehub_py.models.notehub_route import NotehubRoute
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(
    access_token = "PERSONAL_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.RouteApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    notehub_route = {"http":{"disable_http_headers":false,"filter":{},"fleets":["fleet:1042ddc5-3b2c-4cec-b1fb-d3040538094d"],"http_headers":{"X-My-Header":"value"},"throttle_ms":100,"timeout":5000,"transform":{},"url":"https://example.com/ingest"},"label":"Route Label"} # NotehubRoute | Route to be created

    try:
        # Create a route
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

## delete_route

> delete_route(project_or_product_uid, route_uid)

Delete a route

Delete a route so it stops sending events. To pause it instead, set `disabled` with `UpdateRoute`. Requires the Owner or Developer role.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(
    access_token = "PERSONAL_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.RouteApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    route_uid = 'route:cbd20093cba58392c9f9bbdd0cdeb1a0' # str | RouteUID, e.g. `route:cbd20093cba58392c9f9bbdd0cdeb1a0`. List with `GetRoutes`.

    try:
        # Delete a route
        api_instance.delete_route(project_or_product_uid, route_uid)
    except Exception as e:
        print("Exception when calling RouteApi->delete_route: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                                         | Notes |
| -------------------------- | ------- | --------------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                                                                     |
| **route_uid**              | **str** | RouteUID, e.g. &#x60;route:cbd20093cba58392c9f9bbdd0cdeb1a0&#x60;. List with &#x60;GetRoutes&#x60;. |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_route

> NotehubRoute get_route(project_or_product_uid, route_uid)

Get a route

Get one route's full settings: destination, filter, transform and fleets. Secrets such as passwords and keys come back as `(omitted)`. Requires the Owner or Developer role. Viewers can use `GetRoutes`. Returns 404 if the route doesn't exist.

### Example

```python
import notehub_py
from notehub_py.models.notehub_route import NotehubRoute
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(
    access_token = "PERSONAL_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.RouteApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    route_uid = 'route:cbd20093cba58392c9f9bbdd0cdeb1a0' # str | RouteUID, e.g. `route:cbd20093cba58392c9f9bbdd0cdeb1a0`. List with `GetRoutes`.

    try:
        # Get a route
        api_response = api_instance.get_route(project_or_product_uid, route_uid)
        print("The response of RouteApi->get_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->get_route: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                                         | Notes |
| -------------------------- | ------- | --------------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                                                                     |
| **route_uid**              | **str** | RouteUID, e.g. &#x60;route:cbd20093cba58392c9f9bbdd0cdeb1a0&#x60;. List with &#x60;GetRoutes&#x60;. |

### Return type

[**NotehubRoute**](NotehubRoute.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_route_logs_by_route

> List[RouteLog] get_route_logs_by_route(project_or_product_uid, route_uid, page_size=page_size, page_num=page_num, cursor=cursor, device_uid=device_uid, sort_by=sort_by, sort_order=sort_order, start_date=start_date, end_date=end_date, system_files_only=system_files_only, most_recent_only=most_recent_only, files=files, routing_status=routing_status, response_status=response_status)

List a route's logs

List a route's attempts to send events, newest first, with each one's event, response status, body and duration. Filter by device, notefile, date, success or HTTP status. For one event, use `GetRouteLogsByEvent`. Paginated. Returns 404 if the route doesn't exist.

### Example

```python
import notehub_py
from notehub_py.models.route_log import RouteLog
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(
    access_token = "PERSONAL_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.RouteApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    route_uid = 'route:cbd20093cba58392c9f9bbdd0cdeb1a0' # str | RouteUID, e.g. `route:cbd20093cba58392c9f9bbdd0cdeb1a0`. List with `GetRoutes`.
    page_size = 1000 # int |  (optional) (default to 1000)
    page_num = 1 # int |  (optional) (default to 1)
    cursor = 'cursor_example' # str | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by `.N`. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; `.N` is the serial of the last row read at that microsecond, so nothing repeats or is skipped.  (optional)
    device_uid = ['device_uid_example'] # List[str] | A DeviceUID. (optional)
    sort_by = 'date' # str | Field to sort by. - `date`: when the attempt was made - `event`: the order the events arrived in, then the attempt time  (optional) (default to 'date')
    sort_order = 'desc' # str | Sort direction. - `asc`: oldest first - `desc`: newest first  (optional) (default to 'desc')
    start_date = 1628631763 # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210 # int | End date for filtering results, specified as a Unix timestamp (optional)
    system_files_only = True # bool | If true, return only events from system notefiles, such as `_session.qo` and `_health.qo`. (optional)
    most_recent_only = True # bool | If true, return only the latest attempt for each event. (optional)
    files = '_health.qo, data.qo' # str | Comma-separated notefiles, e.g. `data.qo,_health.qo`. Don't combine with `systemFilesOnly`. (optional)
    routing_status = ['failure'] # List[str] | Return only attempts with this outcome. - `success`: the destination accepted the event - `failure`: the attempt failed  (optional)
    response_status = ['500'] # List[str] | Response status codes to include, e.g. `500`. (optional)

    try:
        # List a route's logs
        api_response = api_instance.get_route_logs_by_route(project_or_product_uid, route_uid, page_size=page_size, page_num=page_num, cursor=cursor, device_uid=device_uid, sort_by=sort_by, sort_order=sort_order, start_date=start_date, end_date=end_date, system_files_only=system_files_only, most_recent_only=most_recent_only, files=files, routing_status=routing_status, response_status=response_status)
        print("The response of RouteApi->get_route_logs_by_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->get_route_logs_by_route: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Notes                                  |
| -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **project_or_product_uid** | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **route_uid**              | **str**                 | RouteUID, e.g. &#x60;route:cbd20093cba58392c9f9bbdd0cdeb1a0&#x60;. List with &#x60;GetRoutes&#x60;.                                                                                                                                                                                                                                                                                                                                                                     |
| **page_size**              | **int**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1000]           |
| **page_num**               | **int**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1]              |
| **cursor**                 | **str**                 | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by &#x60;.N&#x60;. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; &#x60;.N&#x60; is the serial of the last row read at that microsecond, so nothing repeats or is skipped. | [optional]                             |
| **device_uid**             | [**List[str]**](str.md) | A DeviceUID.                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [optional]                             |
| **sort_by**                | **str**                 | Field to sort by. - &#x60;date&#x60;: when the attempt was made - &#x60;event&#x60;: the order the events arrived in, then the attempt time                                                                                                                                                                                                                                                                                                                             | [optional] [default to &#39;date&#39;] |
| **sort_order**             | **str**                 | Sort direction. - &#x60;asc&#x60;: oldest first - &#x60;desc&#x60;: newest first                                                                                                                                                                                                                                                                                                                                                                                        | [optional] [default to &#39;desc&#39;] |
| **start_date**             | **int**                 | Start date for filtering results, specified as a Unix timestamp                                                                                                                                                                                                                                                                                                                                                                                                         | [optional]                             |
| **end_date**               | **int**                 | End date for filtering results, specified as a Unix timestamp                                                                                                                                                                                                                                                                                                                                                                                                           | [optional]                             |
| **system_files_only**      | **bool**                | If true, return only events from system notefiles, such as &#x60;\_session.qo&#x60; and &#x60;\_health.qo&#x60;.                                                                                                                                                                                                                                                                                                                                                        | [optional]                             |
| **most_recent_only**       | **bool**                | If true, return only the latest attempt for each event.                                                                                                                                                                                                                                                                                                                                                                                                                 | [optional]                             |
| **files**                  | **str**                 | Comma-separated notefiles, e.g. &#x60;data.qo,\_health.qo&#x60;. Don&#39;t combine with &#x60;systemFilesOnly&#x60;.                                                                                                                                                                                                                                                                                                                                                    | [optional]                             |
| **routing_status**         | [**List[str]**](str.md) | Return only attempts with this outcome. - &#x60;success&#x60;: the destination accepted the event - &#x60;failure&#x60;: the attempt failed                                                                                                                                                                                                                                                                                                                             | [optional]                             |
| **response_status**        | [**List[str]**](str.md) | Response status codes to include, e.g. &#x60;500&#x60;.                                                                                                                                                                                                                                                                                                                                                                                                                 | [optional]                             |

### Return type

[**List[RouteLog]**](RouteLog.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_routes

> List[NotehubRouteSummary] get_routes(project_or_product_uid)

List routes

List a project's routes with their type and label and whether they're disabled, without their settings. For a route's settings, use `GetRoute`.

### Example

```python
import notehub_py
from notehub_py.models.notehub_route_summary import NotehubRouteSummary
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(
    access_token = "PERSONAL_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.RouteApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |

    try:
        # List routes
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

## update_route

> NotehubRoute update_route(project_or_product_uid, route_uid, notehub_route)

Update a route

Change a route's settings. Fields you leave out keep their values, and a secret sent back as `(omitted)` is kept, but leaving out `notes` clears it. Requires the Owner or Developer role. Returns 404 if the route doesn't exist, and 400 for invalid settings.

### Example

```python
import notehub_py
from notehub_py.models.notehub_route import NotehubRoute
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(
    access_token = "PERSONAL_ACCESS_TOKEN"
)

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.RouteApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    route_uid = 'route:cbd20093cba58392c9f9bbdd0cdeb1a0' # str | RouteUID, e.g. `route:cbd20093cba58392c9f9bbdd0cdeb1a0`. List with `GetRoutes`.
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
        # Update a route
        api_response = api_instance.update_route(project_or_product_uid, route_uid, notehub_route)
        print("The response of RouteApi->update_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RouteApi->update_route: %s\n" % e)
```

### Parameters

| Name                       | Type                                | Description                                                                                         | Notes |
| -------------------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**                             |                                                                                                     |
| **route_uid**              | **str**                             | RouteUID, e.g. &#x60;route:cbd20093cba58392c9f9bbdd0cdeb1a0&#x60;. List with &#x60;GetRoutes&#x60;. |
| **notehub_route**          | [**NotehubRoute**](NotehubRoute.md) | Route settings to be updated                                                                        |

### Return type

[**NotehubRoute**](NotehubRoute.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json
