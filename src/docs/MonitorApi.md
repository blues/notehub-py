# notehub_py.MonitorApi

All URIs are relative to *https://api.notefile.net*

| Method                                             | HTTP request                                                        | Description      |
| -------------------------------------------------- | ------------------------------------------------------------------- | ---------------- |
| [**create_monitor**](MonitorApi.md#create_monitor) | **POST** /v1/projects/{projectOrProductUID}/monitors                | Create a monitor |
| [**delete_monitor**](MonitorApi.md#delete_monitor) | **DELETE** /v1/projects/{projectOrProductUID}/monitors/{monitorUID} | Delete a monitor |
| [**get_monitor**](MonitorApi.md#get_monitor)       | **GET** /v1/projects/{projectOrProductUID}/monitors/{monitorUID}    | Get a monitor    |
| [**get_monitors**](MonitorApi.md#get_monitors)     | **GET** /v1/projects/{projectOrProductUID}/monitors                 | List monitors    |
| [**update_monitor**](MonitorApi.md#update_monitor) | **PUT** /v1/projects/{projectOrProductUID}/monitors/{monitorUID}    | Update a monitor |

## create_monitor

> Monitor create_monitor(project_or_product_uid, create_monitor)

Create a monitor

Create a monitor that raises an alert and notifies email, Slack or Twilio when its condition holds. It can watch an event value (`event`, the default), devices going quiet (`heartbeat`), or data usage (`usage`). Requires the Owner or Developer role. Returns 403 if the project's plan doesn't allow the monitor, and 400 for invalid settings.

### Example

```python
import notehub_py
from notehub_py.models.create_monitor import CreateMonitor
from notehub_py.models.monitor import Monitor
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.MonitorApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    create_monitor = (
        notehub_py.CreateMonitor()
    )  # CreateMonitor | Body or payload of monitor to be created

    try:
        # Create a monitor
        api_response = api_instance.create_monitor(
            project_or_product_uid, create_monitor
        )
        print("The response of MonitorApi->create_monitor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorApi->create_monitor: %s\n" % e)
```

### Parameters

| Name                       | Type                                  | Description                              | Notes |
| -------------------------- | ------------------------------------- | ---------------------------------------- | ----- |
| **project_or_product_uid** | **str**                               |                                          |
| **create_monitor**         | [**CreateMonitor**](CreateMonitor.md) | Body or payload of monitor to be created |

### Return type

[**Monitor**](Monitor.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## delete_monitor

> Monitor delete_monitor(project_or_product_uid, monitor_uid)

Delete a monitor

Delete a monitor so it stops raising alerts. Returns an empty monitor object. To pause it instead, set `disabled` with `UpdateMonitor`. Requires the Owner or Developer role. Returns 404 if the monitor never existed; deleting it again succeeds.

### Example

```python
import notehub_py
from notehub_py.models.monitor import Monitor
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.MonitorApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    monitor_uid = "monitor:8bAdf00d-000f-51c-af-01d5eaf00dbad"  # str | MonitorUID, `monitor:` followed by a UUID. List with `GetMonitors`.

    try:
        # Delete a monitor
        api_response = api_instance.delete_monitor(project_or_product_uid, monitor_uid)
        print("The response of MonitorApi->delete_monitor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorApi->delete_monitor: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                             | Notes |
| -------------------------- | ------- | --------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                                                         |
| **monitor_uid**            | **str** | MonitorUID, &#x60;monitor:&#x60; followed by a UUID. List with &#x60;GetMonitors&#x60;. |

### Return type

[**Monitor**](Monitor.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_monitor

> Monitor get_monitor(project_or_product_uid, monitor_uid)

Get a monitor

Get one monitor's settings and whether it's in alert. Slack and Twilio credentials in `alert_routes` come back as `(omitted)`. Returns 404 if the monitor never existed; a deleted monitor is still returned.

### Example

```python
import notehub_py
from notehub_py.models.monitor import Monitor
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.MonitorApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    monitor_uid = "monitor:8bAdf00d-000f-51c-af-01d5eaf00dbad"  # str | MonitorUID, `monitor:` followed by a UUID. List with `GetMonitors`.

    try:
        # Get a monitor
        api_response = api_instance.get_monitor(project_or_product_uid, monitor_uid)
        print("The response of MonitorApi->get_monitor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorApi->get_monitor: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                             | Notes |
| -------------------------- | ------- | --------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                                                         |
| **monitor_uid**            | **str** | MonitorUID, &#x60;monitor:&#x60; followed by a UUID. List with &#x60;GetMonitors&#x60;. |

### Return type

[**Monitor**](Monitor.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_monitors

> List[Monitor] get_monitors(project_or_product_uid)

List monitors

List a project's monitors with their settings and whether each is in alert. For the alerts they've raised, use `GetAlerts`.

### Example

```python
import notehub_py
from notehub_py.models.monitor import Monitor
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.MonitorApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |

    try:
        # List monitors
        api_response = api_instance.get_monitors(project_or_product_uid)
        print("The response of MonitorApi->get_monitors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorApi->get_monitors: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |

### Return type

[**List[Monitor]**](Monitor.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## update_monitor

> Monitor update_monitor(project_or_product_uid, monitor_uid, monitor)

Update a monitor

Replace a monitor's settings with the whole monitor, as `GetMonitor` returns it. Omitted fields are cleared or reset, except `source_type`, `fleet_filter`, `notefile_filter`, `condition_type`, `aggregate_window` and `alert_routes`. Slack and Twilio credentials left as `(omitted)` are kept. Requires the Owner or Developer role. Returns 403 if the plan doesn't allow a new `source_type`.

### Example

```python
import notehub_py
from notehub_py.models.monitor import Monitor
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.MonitorApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    monitor_uid = "monitor:8bAdf00d-000f-51c-af-01d5eaf00dbad"  # str | MonitorUID, `monitor:` followed by a UUID. List with `GetMonitors`.
    monitor = notehub_py.Monitor()  # Monitor | Body or payload of monitor to be created

    try:
        # Update a monitor
        api_response = api_instance.update_monitor(
            project_or_product_uid, monitor_uid, monitor
        )
        print("The response of MonitorApi->update_monitor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MonitorApi->update_monitor: %s\n" % e)
```

### Parameters

| Name                       | Type                      | Description                                                                             | Notes |
| -------------------------- | ------------------------- | --------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**                   |                                                                                         |
| **monitor_uid**            | **str**                   | MonitorUID, &#x60;monitor:&#x60; followed by a UUID. List with &#x60;GetMonitors&#x60;. |
| **monitor**                | [**Monitor**](Monitor.md) | Body or payload of monitor to be created                                                |

### Return type

[**Monitor**](Monitor.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json
