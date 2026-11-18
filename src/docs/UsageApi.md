# notehub_py.UsageApi

All URIs are relative to *https://api.notefile.net*

| Method                                                       | HTTP request                                                | Description                           |
| ------------------------------------------------------------ | ----------------------------------------------------------- | ------------------------------------- |
| [**get_api_usage**](UsageApi.md#get_api_usage)               | **GET** /v1/projects/{projectOrProductUID}/usage/api        | Get billable API usage                |
| [**get_data_usage**](UsageApi.md#get_data_usage)             | **GET** /v1/projects/{projectOrProductUID}/usage/data       | Get cellular and satellite data usage |
| [**get_events_usage**](UsageApi.md#get_events_usage)         | **GET** /v1/projects/{projectOrProductUID}/usage/events     | Get event usage                       |
| [**get_route_logs_usage**](UsageApi.md#get_route_logs_usage) | **GET** /v1/projects/{projectOrProductUID}/usage/route-logs | Get route log usage                   |
| [**get_sessions_usage**](UsageApi.md#get_sessions_usage)     | **GET** /v1/projects/{projectOrProductUID}/usage/sessions   | Get session usage                     |

## get_api_usage

> GetApiUsage200Response get_api_usage(project_or_product_uid, period, start_date=start_date, end_date=end_date, limit=limit)

Get billable API usage

Count a project's billable Notehub API requests per day, week or month, by endpoint. Only requests billed against the project's plan are counted. Returns 400 if `startDate` is after `endDate`.

### Example

```python
import notehub_py
from notehub_py.models.get_api_usage200_response import GetApiUsage200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.UsageApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    period = "period_example"  # str | The length of time each data point covers.
    start_date = 1628631763  # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210  # int | End date for filtering results, specified as a Unix timestamp (optional)
    limit = 200000  # int | The most data points to return. If there are more, `truncated` is true. (optional) (default to 200000)

    try:
        # Get billable API usage
        api_response = api_instance.get_api_usage(
            project_or_product_uid,
            period,
            start_date=start_date,
            end_date=end_date,
            limit=limit,
        )
        print("The response of UsageApi->get_api_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_api_usage: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                       | Notes                          |
| -------------------------- | ------- | --------------------------------------------------------------------------------- | ------------------------------ |
| **project_or_product_uid** | **str** |                                                                                   |
| **period**                 | **str** | The length of time each data point covers.                                        |
| **start_date**             | **int** | Start date for filtering results, specified as a Unix timestamp                   | [optional]                     |
| **end_date**               | **int** | End date for filtering results, specified as a Unix timestamp                     | [optional]                     |
| **limit**                  | **int** | The most data points to return. If there are more, &#x60;truncated&#x60; is true. | [optional] [default to 200000] |

### Return type

[**GetApiUsage200Response**](GetApiUsage200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_data_usage

> GetDataUsage200Response get_data_usage(project_or_product_uid, period, start_date=start_date, end_date=end_date, device_uid=device_uid, fleet_uid=fleet_uid, limit=limit, aggregate=aggregate)

Get cellular and satellite data usage

Get the cellular and satellite data a project's devices used, in bytes. It's counted per day, week or month, by device, fleet or the whole project. If there are more data points than `limit`, the rest are dropped and `truncated` is true. Returns 400 for an unknown device, or if `endDate` is before `startDate`.

### Example

```python
import notehub_py
from notehub_py.models.get_data_usage200_response import GetDataUsage200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.UsageApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    period = "period_example"  # str | The length of time each data point covers.
    start_date = 1628631763  # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210  # int | End date for filtering results, specified as a Unix timestamp (optional)
    device_uid = ["device_uid_example"]  # List[str] | A DeviceUID. (optional)
    fleet_uid = ["fleet_uid_example"]  # List[str] | Filter by FleetUID (optional)
    limit = 200000  # int | The most data points to return. If there are more, `truncated` is true. (optional) (default to 200000)
    aggregate = "device"  # str | How to group the counts, such as per device or one total for the project. (optional) (default to 'device')

    try:
        # Get cellular and satellite data usage
        api_response = api_instance.get_data_usage(
            project_or_product_uid,
            period,
            start_date=start_date,
            end_date=end_date,
            device_uid=device_uid,
            fleet_uid=fleet_uid,
            limit=limit,
            aggregate=aggregate,
        )
        print("The response of UsageApi->get_data_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_data_usage: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                       | Notes                                    |
| -------------------------- | ----------------------- | --------------------------------------------------------------------------------- | ---------------------------------------- |
| **project_or_product_uid** | **str**                 |                                                                                   |
| **period**                 | **str**                 | The length of time each data point covers.                                        |
| **start_date**             | **int**                 | Start date for filtering results, specified as a Unix timestamp                   | [optional]                               |
| **end_date**               | **int**                 | End date for filtering results, specified as a Unix timestamp                     | [optional]                               |
| **device_uid**             | [**List[str]**](str.md) | A DeviceUID.                                                                      | [optional]                               |
| **fleet_uid**              | [**List[str]**](str.md) | Filter by FleetUID                                                                | [optional]                               |
| **limit**                  | **int**                 | The most data points to return. If there are more, &#x60;truncated&#x60; is true. | [optional] [default to 200000]           |
| **aggregate**              | **str**                 | How to group the counts, such as per device or one total for the project.         | [optional] [default to &#39;device&#39;] |

### Return type

[**GetDataUsage200Response**](GetDataUsage200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_events_usage

> UsageEventsResponse get_events_usage(project_or_product_uid, period, start_date=start_date, end_date=end_date, device_uid=device_uid, fleet_uid=fleet_uid, limit=limit, aggregate=aggregate, notefile=notefile, skip_recent_data=skip_recent_data, include_notefiles=include_notefiles)

Get event usage

Count a project's events per day, week or month, by device, fleet or the whole project, optionally per notefile. Summaries lag; with `period=day` and no `endDate`, the latest day is filled in from recent events unless `skipRecentData` is true. Returns 400 if `startDate` is after `endDate`.

### Example

```python
import notehub_py
from notehub_py.models.usage_events_response import UsageEventsResponse
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.UsageApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    period = "period_example"  # str | The length of time each data point covers.
    start_date = 1628631763  # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210  # int | End date for filtering results, specified as a Unix timestamp (optional)
    device_uid = ["device_uid_example"]  # List[str] | A DeviceUID. (optional)
    fleet_uid = ["fleet_uid_example"]  # List[str] | Filter by FleetUID (optional)
    limit = 200000  # int | The most data points to return. If there are more, `truncated` is true. (optional) (default to 200000)
    aggregate = "device"  # str | How to group the counts, such as per device or one total for the project. (optional) (default to 'device')
    notefile = [
        "notefile_example"
    ]  # List[str] | Count only events from these notefiles. (optional)
    skip_recent_data = False  # bool | If true, return only summarized data, without filling in the latest day. Faster for large projects. (optional) (default to False)
    include_notefiles = False  # bool | If true, include event counts for each notefile. (optional) (default to False)

    try:
        # Get event usage
        api_response = api_instance.get_events_usage(
            project_or_product_uid,
            period,
            start_date=start_date,
            end_date=end_date,
            device_uid=device_uid,
            fleet_uid=fleet_uid,
            limit=limit,
            aggregate=aggregate,
            notefile=notefile,
            skip_recent_data=skip_recent_data,
            include_notefiles=include_notefiles,
        )
        print("The response of UsageApi->get_events_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_events_usage: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                                         | Notes                                    |
| -------------------------- | ----------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **project_or_product_uid** | **str**                 |                                                                                                     |
| **period**                 | **str**                 | The length of time each data point covers.                                                          |
| **start_date**             | **int**                 | Start date for filtering results, specified as a Unix timestamp                                     | [optional]                               |
| **end_date**               | **int**                 | End date for filtering results, specified as a Unix timestamp                                       | [optional]                               |
| **device_uid**             | [**List[str]**](str.md) | A DeviceUID.                                                                                        | [optional]                               |
| **fleet_uid**              | [**List[str]**](str.md) | Filter by FleetUID                                                                                  | [optional]                               |
| **limit**                  | **int**                 | The most data points to return. If there are more, &#x60;truncated&#x60; is true.                   | [optional] [default to 200000]           |
| **aggregate**              | **str**                 | How to group the counts, such as per device or one total for the project.                           | [optional] [default to &#39;device&#39;] |
| **notefile**               | [**List[str]**](str.md) | Count only events from these notefiles.                                                             | [optional]                               |
| **skip_recent_data**       | **bool**                | If true, return only summarized data, without filling in the latest day. Faster for large projects. | [optional] [default to False]            |
| **include_notefiles**      | **bool**                | If true, include event counts for each notefile.                                                    | [optional] [default to False]            |

### Return type

[**UsageEventsResponse**](UsageEventsResponse.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_route_logs_usage

> GetRouteLogsUsage200Response get_route_logs_usage(project_or_product_uid, period, start_date=start_date, end_date=end_date, route_uid=route_uid, limit=limit, aggregate=aggregate, skip_recent_data=skip_recent_data)

Get route log usage

Count a project's attempts to send events to routes per day, week or month, by route or for the whole project. If there are more data points than `limit`, the rest are dropped and `truncated` is true.

### Example

```python
import notehub_py
from notehub_py.models.get_route_logs_usage200_response import (
    GetRouteLogsUsage200Response,
)
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.UsageApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    period = "period_example"  # str | The length of time each data point covers.
    start_date = 1628631763  # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210  # int | End date for filtering results, specified as a Unix timestamp (optional)
    route_uid = ["route_uid_example"]  # List[str] | A RouteUID. (optional)
    limit = 200000  # int | The most data points to return. If there are more, `truncated` is true. (optional) (default to 200000)
    aggregate = "route"  # str | How to group the counts, per route or one total for the project. (optional) (default to 'route')
    skip_recent_data = False  # bool | If true, return only summarized data, without filling in the latest day. Faster for large projects. (optional) (default to False)

    try:
        # Get route log usage
        api_response = api_instance.get_route_logs_usage(
            project_or_product_uid,
            period,
            start_date=start_date,
            end_date=end_date,
            route_uid=route_uid,
            limit=limit,
            aggregate=aggregate,
            skip_recent_data=skip_recent_data,
        )
        print("The response of UsageApi->get_route_logs_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_route_logs_usage: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                                         | Notes                                   |
| -------------------------- | ----------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------- |
| **project_or_product_uid** | **str**                 |                                                                                                     |
| **period**                 | **str**                 | The length of time each data point covers.                                                          |
| **start_date**             | **int**                 | Start date for filtering results, specified as a Unix timestamp                                     | [optional]                              |
| **end_date**               | **int**                 | End date for filtering results, specified as a Unix timestamp                                       | [optional]                              |
| **route_uid**              | [**List[str]**](str.md) | A RouteUID.                                                                                         | [optional]                              |
| **limit**                  | **int**                 | The most data points to return. If there are more, &#x60;truncated&#x60; is true.                   | [optional] [default to 200000]          |
| **aggregate**              | **str**                 | How to group the counts, per route or one total for the project.                                    | [optional] [default to &#39;route&#39;] |
| **skip_recent_data**       | **bool**                | If true, return only summarized data, without filling in the latest day. Faster for large projects. | [optional] [default to False]           |

### Return type

[**GetRouteLogsUsage200Response**](GetRouteLogsUsage200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_sessions_usage

> GetSessionsUsage200Response get_sessions_usage(project_or_product_uid, period, start_date=start_date, end_date=end_date, device_uid=device_uid, fleet_uid=fleet_uid, limit=limit, aggregate=aggregate, skip_recent_data=skip_recent_data)

Get session usage

Count a project's device sessions per day, week or month, by device, fleet or the whole project. If there are more data points than `limit`, the rest are dropped and `truncated` is true. Returns 400 if `startDate` is after `endDate`.

### Example

```python
import notehub_py
from notehub_py.models.get_sessions_usage200_response import GetSessionsUsage200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.UsageApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    period = "period_example"  # str | The length of time each data point covers.
    start_date = 1628631763  # int | Start date for filtering results, specified as a Unix timestamp (optional)
    end_date = 1657894210  # int | End date for filtering results, specified as a Unix timestamp (optional)
    device_uid = ["device_uid_example"]  # List[str] | A DeviceUID. (optional)
    fleet_uid = ["fleet_uid_example"]  # List[str] | Filter by FleetUID (optional)
    limit = 200000  # int | The most data points to return. If there are more, `truncated` is true. (optional) (default to 200000)
    aggregate = "device"  # str | How to group the counts, such as per device or one total for the project. (optional) (default to 'device')
    skip_recent_data = False  # bool | If true, return only summarized data, without filling in the latest day. Faster for large projects. (optional) (default to False)

    try:
        # Get session usage
        api_response = api_instance.get_sessions_usage(
            project_or_product_uid,
            period,
            start_date=start_date,
            end_date=end_date,
            device_uid=device_uid,
            fleet_uid=fleet_uid,
            limit=limit,
            aggregate=aggregate,
            skip_recent_data=skip_recent_data,
        )
        print("The response of UsageApi->get_sessions_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsageApi->get_sessions_usage: %s\n" % e)
```

### Parameters

| Name                       | Type                    | Description                                                                                         | Notes                                    |
| -------------------------- | ----------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **project_or_product_uid** | **str**                 |                                                                                                     |
| **period**                 | **str**                 | The length of time each data point covers.                                                          |
| **start_date**             | **int**                 | Start date for filtering results, specified as a Unix timestamp                                     | [optional]                               |
| **end_date**               | **int**                 | End date for filtering results, specified as a Unix timestamp                                       | [optional]                               |
| **device_uid**             | [**List[str]**](str.md) | A DeviceUID.                                                                                        | [optional]                               |
| **fleet_uid**              | [**List[str]**](str.md) | Filter by FleetUID                                                                                  | [optional]                               |
| **limit**                  | **int**                 | The most data points to return. If there are more, &#x60;truncated&#x60; is true.                   | [optional] [default to 200000]           |
| **aggregate**              | **str**                 | How to group the counts, such as per device or one total for the project.                           | [optional] [default to &#39;device&#39;] |
| **skip_recent_data**       | **bool**                | If true, return only summarized data, without filling in the latest day. Faster for large projects. | [optional] [default to False]            |

### Return type

[**GetSessionsUsage200Response**](GetSessionsUsage200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json
