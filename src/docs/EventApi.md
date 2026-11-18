# notehub_py.EventApi

All URIs are relative to *https://api.notefile.net*

| Method                                                             | HTTP request                                                            | Description                   |
| ------------------------------------------------------------------ | ----------------------------------------------------------------------- | ----------------------------- |
| [**get_events**](EventApi.md#get_events)                           | **GET** /v1/projects/{projectOrProductUID}/events                       | List events in a project      |
| [**get_fleet_events**](EventApi.md#get_fleet_events)               | **GET** /v1/projects/{projectOrProductUID}/fleets/{fleetUID}/events     | List events in a fleet        |
| [**get_route_logs_by_event**](EventApi.md#get_route_logs_by_event) | **GET** /v1/projects/{projectOrProductUID}/events/{eventUID}/route-logs | Get an event&#39;s route logs |

## get_events

> GetEvents200Response get_events(project_or_product_uid, page_size=page_size, page_num=page_num, cursor=cursor, device_uid=device_uid, sensor_uid=sensor_uid, sort_by=sort_by, sort_order=sort_order, start_date=start_date, end_date=end_date, date_type=date_type, system_files_only=system_files_only, files=files, format=format, serial_number=serial_number, fleet_uid=fleet_uid, session_uid=session_uid, event_uid=event_uid, select_fields=select_fields)

List events in a project

List a project's events, filtered by device, notefile, date, fleet, session and more. Use `cursor` to read events in the order Notehub stored them and to poll for new ones. Set `format=csv` for CSV. For one fleet, use `GetFleetEvents`. Paginated. Returns 403 if the organization is suspended, and 500 if the query times out; narrow the filters and retry.

### Example

```python
import notehub_py
from notehub_py.models.get_events200_response import GetEvents200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.EventApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    page_size = 1000  # int |  (optional) (default to 1000)
    page_num = 1  # int |  (optional) (default to 1)
    cursor = "cursor_example"  # str | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by `.N`. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; `.N` is the serial of the last row read at that microsecond, so nothing repeats or is skipped.  (optional)
    device_uid = ["device_uid_example"]  # List[str] | A DeviceUID. (optional)
    sensor_uid = [
        "sensor_uid_example"
    ]  # List[str] | SensorUID to filter by, matched exactly. Repeat for more than one. (optional)
    sort_by = "captured"  # str |  (optional) (default to 'captured')
    sort_order = "asc"  # str |  (optional) (default to 'asc')
    start_date = 1628631763  # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210  # int | End date for filtering results, specified as a Unix timestamp (optional)
    date_type = "captured"  # str | Which time `startDate` and `endDate` filter on. - `captured`: when the Notecard created the event - `uploaded`: when Notehub received it  (optional) (default to 'captured')
    system_files_only = True  # bool | If true, return only events from system notefiles, such as `_session.qo` and `_health.qo`. (optional)
    files = "_health.qo, data.qo"  # str | Comma-separated notefiles, e.g. `data.qo,_health.qo`. Don't combine with `systemFilesOnly`. (optional)
    format = "json"  # str | Response format. - `json`: a JSON object with `events` - `csv`: CSV, with the columns in `selectFields`  (optional) (default to 'json')
    serial_number = [
        "serial_number_example"
    ]  # List[str] | Serial number to filter by. Repeat for more than one. (optional)
    fleet_uid = ["fleet_uid_example"]  # List[str] | Filter by FleetUID (optional)
    session_uid = [
        "session_uid_example"
    ]  # List[str] | SessionUID to filter by. Repeat for more than one. (optional)
    event_uid = [
        "event_uid_example"
    ]  # List[str] | EventUID to filter by. Repeat for more than one. (optional)
    select_fields = "select_fields_example"  # str | Comma-separated event fields to return, e.g. `device,when,body.temp`. Also sets the CSV columns. (optional)

    try:
        # List events in a project
        api_response = api_instance.get_events(
            project_or_product_uid,
            page_size=page_size,
            page_num=page_num,
            cursor=cursor,
            device_uid=device_uid,
            sensor_uid=sensor_uid,
            sort_by=sort_by,
            sort_order=sort_order,
            start_date=start_date,
            end_date=end_date,
            date_type=date_type,
            system_files_only=system_files_only,
            files=files,
            format=format,
            serial_number=serial_number,
            fleet_uid=fleet_uid,
            session_uid=session_uid,
            event_uid=event_uid,
            select_fields=select_fields,
        )
        print("The response of EventApi->get_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->get_events: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Notes                                      |
| -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **project_or_product_uid** | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **page_size**              | **int**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1000]               |
| **page_num**               | **int**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1]                  |
| **cursor**                 | **str**                 | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by &#x60;.N&#x60;. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; &#x60;.N&#x60; is the serial of the last row read at that microsecond, so nothing repeats or is skipped. | [optional]                                 |
| **device_uid**             | [**List[str]**](str.md) | A DeviceUID.                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [optional]                                 |
| **sensor_uid**             | [**List[str]**](str.md) | SensorUID to filter by, matched exactly. Repeat for more than one.                                                                                                                                                                                                                                                                                                                                                                                                      | [optional]                                 |
| **sort_by**                | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to &#39;captured&#39;] |
| **sort_order**             | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to &#39;asc&#39;]      |
| **start_date**             | **int**                 | Start date for filtering results, specified as a Unix timestamp                                                                                                                                                                                                                                                                                                                                                                                                         | [optional]                                 |
| **end_date**               | **int**                 | End date for filtering results, specified as a Unix timestamp                                                                                                                                                                                                                                                                                                                                                                                                           | [optional]                                 |
| **date_type**              | **str**                 | Which time &#x60;startDate&#x60; and &#x60;endDate&#x60; filter on. - &#x60;captured&#x60;: when the Notecard created the event - &#x60;uploaded&#x60;: when Notehub received it                                                                                                                                                                                                                                                                                        | [optional] [default to &#39;captured&#39;] |
| **system_files_only**      | **bool**                | If true, return only events from system notefiles, such as &#x60;\_session.qo&#x60; and &#x60;\_health.qo&#x60;.                                                                                                                                                                                                                                                                                                                                                        | [optional]                                 |
| **files**                  | **str**                 | Comma-separated notefiles, e.g. &#x60;data.qo,\_health.qo&#x60;. Don&#39;t combine with &#x60;systemFilesOnly&#x60;.                                                                                                                                                                                                                                                                                                                                                    | [optional]                                 |
| **format**                 | **str**                 | Response format. - &#x60;json&#x60;: a JSON object with &#x60;events&#x60; - &#x60;csv&#x60;: CSV, with the columns in &#x60;selectFields&#x60;                                                                                                                                                                                                                                                                                                                         | [optional] [default to &#39;json&#39;]     |
| **serial_number**          | [**List[str]**](str.md) | Serial number to filter by. Repeat for more than one.                                                                                                                                                                                                                                                                                                                                                                                                                   | [optional]                                 |
| **fleet_uid**              | [**List[str]**](str.md) | Filter by FleetUID                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [optional]                                 |
| **session_uid**            | [**List[str]**](str.md) | SessionUID to filter by. Repeat for more than one.                                                                                                                                                                                                                                                                                                                                                                                                                      | [optional]                                 |
| **event_uid**              | [**List[str]**](str.md) | EventUID to filter by. Repeat for more than one.                                                                                                                                                                                                                                                                                                                                                                                                                        | [optional]                                 |
| **select_fields**          | **str**                 | Comma-separated event fields to return, e.g. &#x60;device,when,body.temp&#x60;. Also sets the CSV columns.                                                                                                                                                                                                                                                                                                                                                              | [optional]                                 |

### Return type

[**GetEvents200Response**](GetEvents200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

## get_fleet_events

> GetEvents200Response get_fleet_events(project_or_product_uid, fleet_uid, page_size=page_size, page_num=page_num, cursor=cursor, device_uid=device_uid, sensor_uid=sensor_uid, sort_by=sort_by, sort_order=sort_order, start_date=start_date, end_date=end_date, date_type=date_type, system_files_only=system_files_only, files=files, format=format, serial_number=serial_number, session_uid=session_uid, event_uid=event_uid, select_fields=select_fields)

List events in a fleet

List the events from one fleet, with the same filters, `cursor` and CSV output as `GetEvents`. Paginated. Returns 403 if the organization is suspended, and 500 if the query times out; narrow the filters and retry.

### Example

```python
import notehub_py
from notehub_py.models.get_events200_response import GetEvents200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.EventApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    fleet_uid = "fleet_uid_example"  # str |
    page_size = 1000  # int |  (optional) (default to 1000)
    page_num = 1  # int |  (optional) (default to 1)
    cursor = "cursor_example"  # str | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by `.N`. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; `.N` is the serial of the last row read at that microsecond, so nothing repeats or is skipped.  (optional)
    device_uid = ["device_uid_example"]  # List[str] | A DeviceUID. (optional)
    sensor_uid = [
        "sensor_uid_example"
    ]  # List[str] | SensorUID to filter by, matched exactly. Repeat for more than one. (optional)
    sort_by = "captured"  # str |  (optional) (default to 'captured')
    sort_order = "asc"  # str |  (optional) (default to 'asc')
    start_date = 1628631763  # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210  # int | End date for filtering results, specified as a Unix timestamp (optional)
    date_type = "captured"  # str | Which time `startDate` and `endDate` filter on. - `captured`: when the Notecard created the event - `uploaded`: when Notehub received it  (optional) (default to 'captured')
    system_files_only = True  # bool | If true, return only events from system notefiles, such as `_session.qo` and `_health.qo`. (optional)
    files = "_health.qo, data.qo"  # str | Comma-separated notefiles, e.g. `data.qo,_health.qo`. Don't combine with `systemFilesOnly`. (optional)
    format = "json"  # str | Response format. - `json`: a JSON object with `events` - `csv`: CSV, with the columns in `selectFields`  (optional) (default to 'json')
    serial_number = [
        "serial_number_example"
    ]  # List[str] | Serial number to filter by. Repeat for more than one. (optional)
    session_uid = [
        "session_uid_example"
    ]  # List[str] | SessionUID to filter by. Repeat for more than one. (optional)
    event_uid = [
        "event_uid_example"
    ]  # List[str] | EventUID to filter by. Repeat for more than one. (optional)
    select_fields = "select_fields_example"  # str | Comma-separated event fields to return, e.g. `device,when,body.temp`. Also sets the CSV columns. (optional)

    try:
        # List events in a fleet
        api_response = api_instance.get_fleet_events(
            project_or_product_uid,
            fleet_uid,
            page_size=page_size,
            page_num=page_num,
            cursor=cursor,
            device_uid=device_uid,
            sensor_uid=sensor_uid,
            sort_by=sort_by,
            sort_order=sort_order,
            start_date=start_date,
            end_date=end_date,
            date_type=date_type,
            system_files_only=system_files_only,
            files=files,
            format=format,
            serial_number=serial_number,
            session_uid=session_uid,
            event_uid=event_uid,
            select_fields=select_fields,
        )
        print("The response of EventApi->get_fleet_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->get_fleet_events: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Notes                                      |
| -------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **project_or_product_uid** | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **fleet_uid**              | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **page_size**              | **int**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1000]               |
| **page_num**               | **int**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1]                  |
| **cursor**                 | **str**                 | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by &#x60;.N&#x60;. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; &#x60;.N&#x60; is the serial of the last row read at that microsecond, so nothing repeats or is skipped. | [optional]                                 |
| **device_uid**             | [**List[str]**](str.md) | A DeviceUID.                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [optional]                                 |
| **sensor_uid**             | [**List[str]**](str.md) | SensorUID to filter by, matched exactly. Repeat for more than one.                                                                                                                                                                                                                                                                                                                                                                                                      | [optional]                                 |
| **sort_by**                | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to &#39;captured&#39;] |
| **sort_order**             | **str**                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to &#39;asc&#39;]      |
| **start_date**             | **int**                 | Start date for filtering results, specified as a Unix timestamp                                                                                                                                                                                                                                                                                                                                                                                                         | [optional]                                 |
| **end_date**               | **int**                 | End date for filtering results, specified as a Unix timestamp                                                                                                                                                                                                                                                                                                                                                                                                           | [optional]                                 |
| **date_type**              | **str**                 | Which time &#x60;startDate&#x60; and &#x60;endDate&#x60; filter on. - &#x60;captured&#x60;: when the Notecard created the event - &#x60;uploaded&#x60;: when Notehub received it                                                                                                                                                                                                                                                                                        | [optional] [default to &#39;captured&#39;] |
| **system_files_only**      | **bool**                | If true, return only events from system notefiles, such as &#x60;\_session.qo&#x60; and &#x60;\_health.qo&#x60;.                                                                                                                                                                                                                                                                                                                                                        | [optional]                                 |
| **files**                  | **str**                 | Comma-separated notefiles, e.g. &#x60;data.qo,\_health.qo&#x60;. Don&#39;t combine with &#x60;systemFilesOnly&#x60;.                                                                                                                                                                                                                                                                                                                                                    | [optional]                                 |
| **format**                 | **str**                 | Response format. - &#x60;json&#x60;: a JSON object with &#x60;events&#x60; - &#x60;csv&#x60;: CSV, with the columns in &#x60;selectFields&#x60;                                                                                                                                                                                                                                                                                                                         | [optional] [default to &#39;json&#39;]     |
| **serial_number**          | [**List[str]**](str.md) | Serial number to filter by. Repeat for more than one.                                                                                                                                                                                                                                                                                                                                                                                                                   | [optional]                                 |
| **session_uid**            | [**List[str]**](str.md) | SessionUID to filter by. Repeat for more than one.                                                                                                                                                                                                                                                                                                                                                                                                                      | [optional]                                 |
| **event_uid**              | [**List[str]**](str.md) | EventUID to filter by. Repeat for more than one.                                                                                                                                                                                                                                                                                                                                                                                                                        | [optional]                                 |
| **select_fields**          | **str**                 | Comma-separated event fields to return, e.g. &#x60;device,when,body.temp&#x60;. Also sets the CSV columns.                                                                                                                                                                                                                                                                                                                                                              | [optional]                                 |

### Return type

[**GetEvents200Response**](GetEvents200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv

## get_route_logs_by_event

> List[RouteLog] get_route_logs_by_event(project_or_product_uid, event_uid)

Get an event's route logs

Get the log of every attempt to send one event to each route, with the response status, body and duration. For a route's logs across events, use `GetRouteLogsByRoute`. Returns 404 if the event doesn't exist.

### Example

```python
import notehub_py
from notehub_py.models.route_log import RouteLog
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.EventApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    event_uid = "4506f411-dea6-44a0-9743-1130f57d7747"  # str | EventUID, e.g. `4506f411-dea6-44a0-9743-1130f57d7747`.

    try:
        # Get an event's route logs
        api_response = api_instance.get_route_logs_by_event(
            project_or_product_uid, event_uid
        )
        print("The response of EventApi->get_route_logs_by_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->get_route_logs_by_event: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                      | Notes |
| -------------------------- | ------- | ---------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                                  |
| **event_uid**              | **str** | EventUID, e.g. &#x60;4506f411-dea6-44a0-9743-1130f57d7747&#x60;. |

### Return type

[**List[RouteLog]**](RouteLog.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json
