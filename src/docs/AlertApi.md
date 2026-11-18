# notehub_py.AlertApi

All URIs are relative to *https://api.notefile.net*

| Method                                   | HTTP request                                      | Description |
| ---------------------------------------- | ------------------------------------------------- | ----------- |
| [**get_alerts**](AlertApi.md#get_alerts) | **GET** /v1/projects/{projectOrProductUID}/alerts | List alerts |

## get_alerts

> GetAlerts200Response get_alerts(project_or_product_uid, page_size=page_size, page_num=page_num, cursor=cursor, monitor_uid=monitor_uid)

List alerts

List the alerts a project's monitors have raised, with each one's value, device and the notifications sent. Set `monitorUID` for one monitor's alerts. Paginated.

### Example

```python
import notehub_py
from notehub_py.models.get_alerts200_response import GetAlerts200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.AlertApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    page_size = 1000  # int |  (optional) (default to 1000)
    page_num = 1  # int |  (optional) (default to 1)
    cursor = "cursor_example"  # str | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by `.N`. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; `.N` is the serial of the last row read at that microsecond, so nothing repeats or is skipped.  (optional)
    monitor_uid = (
        "monitor_uid_example"  # str | Return only this monitor's alerts. (optional)
    )

    try:
        # List alerts
        api_response = api_instance.get_alerts(
            project_or_product_uid,
            page_size=page_size,
            page_num=page_num,
            cursor=cursor,
            monitor_uid=monitor_uid,
        )
        print("The response of AlertApi->get_alerts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlertApi->get_alerts: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Notes                        |
| -------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **project_or_product_uid** | **str** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **page_size**              | **int** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1000] |
| **page_num**               | **int** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [optional] [default to 1]    |
| **cursor**                 | **str** | If supplied, results are returned in ascending order of modification time. A cursor is a timestamp: Unix epoch microseconds (UTC), optionally followed by &#x60;.N&#x60;. To start at a time, pass the bare microsecond value (inclusive; e.g. now minus 30 days); 0 starts from the beginning. To resume, pass next_cursor (or X-Next-Cursor) back unchanged; &#x60;.N&#x60; is the serial of the last row read at that microsecond, so nothing repeats or is skipped. | [optional]                   |
| **monitor_uid**            | **str** | Return only this monitor&#39;s alerts.                                                                                                                                                                                                                                                                                                                                                                                                                                  | [optional]                   |

### Return type

[**GetAlerts200Response**](GetAlerts200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json
