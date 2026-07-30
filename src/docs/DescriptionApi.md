# notehub_py.DescriptionApi

All URIs are relative to *https://api.notefile.net*

| Method                                                                         | HTTP request                                                                | Description |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------- | ----------- |
| [**delete_global_description**](DescriptionApi.md#delete_global_description)   | **DELETE** /v1/description/{descriptionName}                                |
| [**delete_project_description**](DescriptionApi.md#delete_project_description) | **DELETE** /v1/projects/{projectOrProductUID}/description/{descriptionName} |
| [**get_global_description**](DescriptionApi.md#get_global_description)         | **GET** /v1/description/{descriptionName}                                   |
| [**get_project_description**](DescriptionApi.md#get_project_description)       | **GET** /v1/projects/{projectOrProductUID}/description/{descriptionName}    |
| [**list_global_descriptions**](DescriptionApi.md#list_global_descriptions)     | **GET** /v1/description                                                     |
| [**list_project_descriptions**](DescriptionApi.md#list_project_descriptions)   | **GET** /v1/projects/{projectOrProductUID}/description                      |
| [**set_global_description**](DescriptionApi.md#set_global_description)         | **POST** /v1/description/{descriptionName}                                  |
| [**set_project_description**](DescriptionApi.md#set_project_description)       | **POST** /v1/projects/{projectOrProductUID}/description/{descriptionName}   |

## delete_global_description

> delete_global_description(description_name)

Delete a global description record by name (Blues staff only).

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DescriptionApi(api_client)
    description_name = "_health.qo"  # str |

    try:
        api_instance.delete_global_description(description_name)
    except Exception as e:
        print(
            "Exception when calling DescriptionApi->delete_global_description: %s\n" % e
        )
```

### Parameters

| Name                 | Type    | Description | Notes |
| -------------------- | ------- | ----------- | ----- |
| **description_name** | **str** |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## delete_project_description

> delete_project_description(project_or_product_uid, description_name)

Delete a project description record by name.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DescriptionApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    description_name = "_health.qo"  # str |

    try:
        api_instance.delete_project_description(
            project_or_product_uid, description_name
        )
    except Exception as e:
        print(
            "Exception when calling DescriptionApi->delete_project_description: %s\n"
            % e
        )
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **description_name**       | **str** |             |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_global_description

> bytearray get_global_description(description_name)

Get a global description record. Returns the raw content with its stored Content-Type.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DescriptionApi(api_client)
    description_name = "_health.qo"  # str |

    try:
        api_response = api_instance.get_global_description(description_name)
        print("The response of DescriptionApi->get_global_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DescriptionApi->get_global_description: %s\n" % e)
```

### Parameters

| Name                 | Type    | Description | Notes |
| -------------------- | ------- | ----------- | ----- |
| **description_name** | **str** |             |

### Return type

**bytearray**

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

## get_project_description

> bytearray get_project_description(project_or_product_uid, description_name)

Get a project description record. Returns the raw content with its stored Content-Type.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DescriptionApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    description_name = "_health.qo"  # str |

    try:
        api_response = api_instance.get_project_description(
            project_or_product_uid, description_name
        )
        print("The response of DescriptionApi->get_project_description:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling DescriptionApi->get_project_description: %s\n" % e
        )
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |
| **description_name**       | **str** |             |

### Return type

**bytearray**

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

## list_global_descriptions

> DescriptionRecordList list_global_descriptions()

List metadata for all global description records.

### Example

```python
import notehub_py
from notehub_py.models.description_record_list import DescriptionRecordList
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DescriptionApi(api_client)

    try:
        api_response = api_instance.list_global_descriptions()
        print("The response of DescriptionApi->list_global_descriptions:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling DescriptionApi->list_global_descriptions: %s\n" % e
        )
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**DescriptionRecordList**](DescriptionRecordList.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## list_project_descriptions

> DescriptionRecordList list_project_descriptions(project_or_product_uid)

List metadata for all description records in a project.

### Example

```python
import notehub_py
from notehub_py.models.description_record_list import DescriptionRecordList
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DescriptionApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |

    try:
        api_response = api_instance.list_project_descriptions(project_or_product_uid)
        print("The response of DescriptionApi->list_project_descriptions:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling DescriptionApi->list_project_descriptions: %s\n" % e
        )
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |

### Return type

[**DescriptionRecordList**](DescriptionRecordList.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## set_global_description

> DescriptionRecord set_global_description(description_name, body)

Create or replace a global description record, Blues staff only (up to 10MB). The request Content-Type is stored and returned on GET; when omitted it is detected (JSON or text).

### Example

```python
import notehub_py
from notehub_py.models.description_record import DescriptionRecord
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DescriptionApi(api_client)
    description_name = "_health.qo"  # str |
    body = None  # bytearray | The description content (up to 10MB). The request Content-Type is stored and returned on GET; when omitted it is detected (JSON or text).

    try:
        api_response = api_instance.set_global_description(description_name, body)
        print("The response of DescriptionApi->set_global_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DescriptionApi->set_global_description: %s\n" % e)
```

### Parameters

| Name                 | Type          | Description                                                                                                                               | Notes |
| -------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **description_name** | **str**       |                                                                                                                                           |
| **body**             | **bytearray** | The description content (up to 10MB). The request Content-Type is stored and returned on GET; when omitted it is detected (JSON or text). |

### Return type

[**DescriptionRecord**](DescriptionRecord.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json

## set_project_description

> DescriptionRecord set_project_description(project_or_product_uid, description_name, body)

Create or replace a project description record (up to 10MB). The request Content-Type is stored and returned on GET; when omitted it is detected (JSON or text).

### Example

```python
import notehub_py
from notehub_py.models.description_record import DescriptionRecord
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.DescriptionApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    description_name = "_health.qo"  # str |
    body = None  # bytearray | The description content (up to 10MB). The request Content-Type is stored and returned on GET; when omitted it is detected (JSON or text).

    try:
        api_response = api_instance.set_project_description(
            project_or_product_uid, description_name, body
        )
        print("The response of DescriptionApi->set_project_description:\n")
        pprint(api_response)
    except Exception as e:
        print(
            "Exception when calling DescriptionApi->set_project_description: %s\n" % e
        )
```

### Parameters

| Name                       | Type          | Description                                                                                                                               | Notes |
| -------------------------- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**       |                                                                                                                                           |
| **description_name**       | **str**       |                                                                                                                                           |
| **body**                   | **bytearray** | The description content (up to 10MB). The request Content-Type is stored and returned on GET; when omitted it is detected (JSON or text). |

### Return type

[**DescriptionRecord**](DescriptionRecord.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json
