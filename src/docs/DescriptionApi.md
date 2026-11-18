# notehub_py.DescriptionApi

All URIs are relative to *https://api.notefile.net*

| Method                                                                         | HTTP request                                                                | Description                                    |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------------------- | ---------------------------------------------- |
| [**delete_global_description**](DescriptionApi.md#delete_global_description)   | **DELETE** /v1/description/{descriptionName}                                | Delete a global description record             |
| [**delete_project_description**](DescriptionApi.md#delete_project_description) | **DELETE** /v1/projects/{projectOrProductUID}/description/{descriptionName} | Delete a project description record            |
| [**get_global_description**](DescriptionApi.md#get_global_description)         | **GET** /v1/description/{descriptionName}                                   | Get a global description record                |
| [**get_project_description**](DescriptionApi.md#get_project_description)       | **GET** /v1/projects/{projectOrProductUID}/description/{descriptionName}    | Get a project description record               |
| [**list_global_descriptions**](DescriptionApi.md#list_global_descriptions)     | **GET** /v1/description                                                     | List global description records                |
| [**list_project_descriptions**](DescriptionApi.md#list_project_descriptions)   | **GET** /v1/projects/{projectOrProductUID}/description                      | List a project&#39;s description records       |
| [**set_global_description**](DescriptionApi.md#set_global_description)         | **POST** /v1/description/{descriptionName}                                  | Create or replace a global description record  |
| [**set_project_description**](DescriptionApi.md#set_project_description)       | **POST** /v1/projects/{projectOrProductUID}/description/{descriptionName}   | Create or replace a project description record |

## delete_global_description

> delete_global_description(description_name)

Delete a global description record

Delete one platform-wide description record. Blues staff only; returns 403 for anyone else. Returns 404 if the record doesn't exist.

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
    description_name = "_health.qo"  # str | Record name, 1-128 letters, digits, `.`, `_` or `-`, e.g. `_health.qo`.

    try:
        # Delete a global description record
        api_instance.delete_global_description(description_name)
    except Exception as e:
        print(
            "Exception when calling DescriptionApi->delete_global_description: %s\n" % e
        )
```

### Parameters

| Name                 | Type    | Description                                                                                                       | Notes |
| -------------------- | ------- | ----------------------------------------------------------------------------------------------------------------- | ----- |
| **description_name** | **str** | Record name, 1-128 letters, digits, &#x60;.&#x60;, &#x60;\_&#x60; or &#x60;-&#x60;, e.g. &#x60;\_health.qo&#x60;. |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## delete_project_description

> delete_project_description(project_or_product_uid, description_name)

Delete a project description record

Delete one of a project's description records. Requires the Owner or Developer role. Returns 404 if the record doesn't exist.

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
    description_name = "_health.qo"  # str | Record name, 1-128 letters, digits, `.`, `_` or `-`, e.g. `_health.qo`.

    try:
        # Delete a project description record
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

| Name                       | Type    | Description                                                                                                       | Notes |
| -------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                                                                                   |
| **description_name**       | **str** | Record name, 1-128 letters, digits, &#x60;.&#x60;, &#x60;\_&#x60; or &#x60;-&#x60;, e.g. &#x60;\_health.qo&#x60;. |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_global_description

> bytearray get_global_description(description_name)

Get a global description record

Get the content of one platform-wide description record, served with the Content-Type it was stored with. Any signed-in user can read it. Returns 404 if the record doesn't exist.

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
    description_name = "_health.qo"  # str | Record name, 1-128 letters, digits, `.`, `_` or `-`, e.g. `_health.qo`.

    try:
        # Get a global description record
        api_response = api_instance.get_global_description(description_name)
        print("The response of DescriptionApi->get_global_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DescriptionApi->get_global_description: %s\n" % e)
```

### Parameters

| Name                 | Type    | Description                                                                                                       | Notes |
| -------------------- | ------- | ----------------------------------------------------------------------------------------------------------------- | ----- |
| **description_name** | **str** | Record name, 1-128 letters, digits, &#x60;.&#x60;, &#x60;\_&#x60; or &#x60;-&#x60;, e.g. &#x60;\_health.qo&#x60;. |

### Return type

**bytearray**

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

## get_project_description

> bytearray get_project_description(project_or_product_uid, description_name)

Get a project description record

Get the content of one of a project's description records, served with the Content-Type it was stored with. For the metadata of every record, use `ListProjectDescriptions`. Returns 404 if the record doesn't exist.

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
    description_name = "_health.qo"  # str | Record name, 1-128 letters, digits, `.`, `_` or `-`, e.g. `_health.qo`.

    try:
        # Get a project description record
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

| Name                       | Type    | Description                                                                                                       | Notes |
| -------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                                                                                   |
| **description_name**       | **str** | Record name, 1-128 letters, digits, &#x60;.&#x60;, &#x60;\_&#x60; or &#x60;-&#x60;, e.g. &#x60;\_health.qo&#x60;. |

### Return type

**bytearray**

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

## list_global_descriptions

> DescriptionRecordList list_global_descriptions()

List global description records

List the platform-wide description records that Blues publishes, without their content. Any signed-in user can read them. For a project's own records, use `ListProjectDescriptions`.

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
        # List global description records
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

List a project's description records

List a project's description records by name, with each one's content type, size and change history but not its content. A description record is a named document, such as Markdown, JSON or plain text, that explains the project's data. For Blues' platform-wide records, use `ListGlobalDescriptions`.

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
        # List a project's description records
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

Create or replace a global description record

Store a platform-wide named document that every signed-in user can read, replacing any record with that name. The Content-Type is handled as in `SetProjectDescription`. Blues staff only; returns 403 for anyone else. Returns 400 if the content is over 10 MB or the name isn't valid.

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
    description_name = "_health.qo"  # str | Record name, 1-128 letters, digits, `.`, `_` or `-`, e.g. `_health.qo`.
    body = None  # bytearray | The document to store, up to 10 MB. Send its Content-Type, such as `text/markdown`; Markdown isn't detected.

    try:
        # Create or replace a global description record
        api_response = api_instance.set_global_description(description_name, body)
        print("The response of DescriptionApi->set_global_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DescriptionApi->set_global_description: %s\n" % e)
```

### Parameters

| Name                 | Type          | Description                                                                                                                | Notes |
| -------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------- | ----- |
| **description_name** | **str**       | Record name, 1-128 letters, digits, &#x60;.&#x60;, &#x60;\_&#x60; or &#x60;-&#x60;, e.g. &#x60;\_health.qo&#x60;.          |
| **body**             | **bytearray** | The document to store, up to 10 MB. Send its Content-Type, such as &#x60;text/markdown&#x60;; Markdown isn&#39;t detected. |

### Return type

[**DescriptionRecord**](DescriptionRecord.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json

## set_project_description

> DescriptionRecord set_project_description(project_or_product_uid, description_name, body)

Create or replace a project description record

Store a named document in a project, replacing any record with that name. The request's Content-Type is stored and served back by `GetProjectDescription`; if it's missing or `application/octet-stream`, the type is detected from the content. Requires the Owner or Developer role. Returns 400 if the content is over 10 MB or the name isn't valid.

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
    description_name = "_health.qo"  # str | Record name, 1-128 letters, digits, `.`, `_` or `-`, e.g. `_health.qo`.
    body = None  # bytearray | The document to store, up to 10 MB. Send its Content-Type, such as `text/markdown`; Markdown isn't detected.

    try:
        # Create or replace a project description record
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

| Name                       | Type          | Description                                                                                                                | Notes |
| -------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**       |                                                                                                                            |
| **description_name**       | **str**       | Record name, 1-128 letters, digits, &#x60;.&#x60;, &#x60;\_&#x60; or &#x60;-&#x60;, e.g. &#x60;\_health.qo&#x60;.          |
| **body**                   | **bytearray** | The document to store, up to 10 MB. Send its Content-Type, such as &#x60;text/markdown&#x60;; Markdown isn&#39;t detected. |

### Return type

[**DescriptionRecord**](DescriptionRecord.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json
