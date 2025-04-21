# notehub_py.RepositoryApi

All URIs are relative to *https://api.notefile.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_repository**](RepositoryApi.md#create_repository) | **POST** /v1/repositories | 
[**create_repository_dataset**](RepositoryApi.md#create_repository_dataset) | **PUT** /v1/repositories/{repositoryUID}/datasets | 
[**delete_repository**](RepositoryApi.md#delete_repository) | **DELETE** /v1/repositories/{repositoryUID} | 
[**delete_repository_dataset**](RepositoryApi.md#delete_repository_dataset) | **DELETE** /v1/repositories/{repositoryUID}/datasets/{name} | 
[**get_repository**](RepositoryApi.md#get_repository) | **GET** /v1/repositories/{repositoryUID} | 
[**get_repository_data**](RepositoryApi.md#get_repository_data) | **GET** /v1/repositories/{repositoryUID}/data | 
[**get_repository_dataset**](RepositoryApi.md#get_repository_dataset) | **GET** /v1/repositories/{repositoryUID}/datasets/{name} | 
[**put_repository**](RepositoryApi.md#put_repository) | **PUT** /v1/repositories/{repositoryUID} | 
[**query_repository_dataset**](RepositoryApi.md#query_repository_dataset) | **GET** /v1/repositories/{repositoryUID}/datasets/{name}/query | 
[**query_repository_sql**](RepositoryApi.md#query_repository_sql) | **POST** /v1/repositories/{repositoryUID}/sql | 


# **create_repository**
> Repository create_repository(create_update_repository)



Create a new repository

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.create_update_repository import CreateUpdateRepository
from notehub_py.models.repository import Repository
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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.RepositoryApi(api_client)
    create_update_repository = notehub_py.CreateUpdateRepository() # CreateUpdateRepository | 

    try:
        api_response = api_instance.create_repository(create_update_repository)
        print("The response of RepositoryApi->create_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->create_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_update_repository** | [**CreateUpdateRepository**](CreateUpdateRepository.md)|  | 

### Return type

[**Repository**](Repository.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Repository created successfully |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repository_dataset**
> DataSet create_repository_dataset(repository_uid, x_repository_key, data_set)



Create a new dataset within a repository

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.data_set import DataSet
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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.RepositoryApi(api_client)
    repository_uid = 'rid:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    x_repository_key = 'x_repository_key_example' # str | The secret key used to access this repository
    data_set = notehub_py.DataSet() # DataSet | 

    try:
        api_response = api_instance.create_repository_dataset(repository_uid, x_repository_key, data_set)
        print("The response of RepositoryApi->create_repository_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->create_repository_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_uid** | **str**|  | 
 **x_repository_key** | **str**| The secret key used to access this repository | 
 **data_set** | [**DataSet**](DataSet.md)|  | 

### Return type

[**DataSet**](DataSet.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Dataset created successfully |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repository**
> delete_repository(repository_uid, x_repository_key)



Delete a repository

### Example

* Api Key Authentication (api_key):

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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.RepositoryApi(api_client)
    repository_uid = 'rid:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    x_repository_key = 'x_repository_key_example' # str | The secret key used to access this repository

    try:
        api_instance.delete_repository(repository_uid, x_repository_key)
    except Exception as e:
        print("Exception when calling RepositoryApi->delete_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_uid** | **str**|  | 
 **x_repository_key** | **str**| The secret key used to access this repository | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset deleted successfully |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_repository_dataset**
> delete_repository_dataset(repository_uid, name, x_repository_key)



Delete a dataset

### Example

* Api Key Authentication (api_key):

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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.RepositoryApi(api_client)
    repository_uid = 'rid:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    name = 'name_example' # str | The name of the data set
    x_repository_key = 'x_repository_key_example' # str | The secret key used to access this repository

    try:
        api_instance.delete_repository_dataset(repository_uid, name, x_repository_key)
    except Exception as e:
        print("Exception when calling RepositoryApi->delete_repository_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_uid** | **str**|  | 
 **name** | **str**| The name of the data set | 
 **x_repository_key** | **str**| The secret key used to access this repository | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset deleted successfully |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository**
> Repository get_repository(repository_uid, x_repository_key)



Get repository information

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.repository import Repository
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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.RepositoryApi(api_client)
    repository_uid = 'rid:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    x_repository_key = 'x_repository_key_example' # str | The secret key used to access this repository

    try:
        api_response = api_instance.get_repository(repository_uid, x_repository_key)
        print("The response of RepositoryApi->get_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->get_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_uid** | **str**|  | 
 **x_repository_key** | **str**| The secret key used to access this repository | 

### Return type

[**Repository**](Repository.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset updated successfully |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository_data**
> bytearray get_repository_data(x_repository_key, repository_uid, start, end=end)



Get event and session data from a repository in NDJSON format.

### Example

* Api Key Authentication (api_key):

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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.RepositoryApi(api_client)
    x_repository_key = 'x_repository_key_example' # str | The secret key used to access this repository
    repository_uid = 'rid:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    start = 'start_example' # str | Start of the time range, as an ISO-8601 date or relative to now (e.g. -1y). Relative dates follow the Postgres INTERVAL format.
    end = 'end_example' # str | End of the time range, as an ISO-8601 date or relative to now. If omitted, current time is used. (optional)

    try:
        api_response = api_instance.get_repository_data(x_repository_key, repository_uid, start, end=end)
        print("The response of RepositoryApi->get_repository_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->get_repository_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_repository_key** | **str**| The secret key used to access this repository | 
 **repository_uid** | **str**|  | 
 **start** | **str**| Start of the time range, as an ISO-8601 date or relative to now (e.g. -1y). Relative dates follow the Postgres INTERVAL format. | 
 **end** | **str**| End of the time range, as an ISO-8601 date or relative to now. If omitted, current time is used. | [optional] 

### Return type

**bytearray**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful request returning NDJSON encoded event and session objects. |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_repository_dataset**
> DataSet get_repository_dataset(repository_uid, name, x_repository_key)



Get the details of a dataset

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.data_set import DataSet
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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.RepositoryApi(api_client)
    repository_uid = 'rid:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    name = 'name_example' # str | The name of the data set
    x_repository_key = 'x_repository_key_example' # str | The secret key used to access this repository

    try:
        api_response = api_instance.get_repository_dataset(repository_uid, name, x_repository_key)
        print("The response of RepositoryApi->get_repository_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->get_repository_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_uid** | **str**|  | 
 **name** | **str**| The name of the data set | 
 **x_repository_key** | **str**| The secret key used to access this repository | 

### Return type

[**DataSet**](DataSet.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset details |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_repository**
> Repository put_repository(repository_uid, x_repository_key, create_update_repository)



Update a repository

### Example

* Api Key Authentication (api_key):

```python
import notehub_py
from notehub_py.models.create_update_repository import CreateUpdateRepository
from notehub_py.models.repository import Repository
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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.RepositoryApi(api_client)
    repository_uid = 'rid:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    x_repository_key = 'x_repository_key_example' # str | The secret key used to access this repository
    create_update_repository = notehub_py.CreateUpdateRepository() # CreateUpdateRepository | 

    try:
        api_response = api_instance.put_repository(repository_uid, x_repository_key, create_update_repository)
        print("The response of RepositoryApi->put_repository:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->put_repository: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_uid** | **str**|  | 
 **x_repository_key** | **str**| The secret key used to access this repository | 
 **create_update_repository** | [**CreateUpdateRepository**](CreateUpdateRepository.md)|  | 

### Return type

[**Repository**](Repository.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Dataset updated successfully |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_repository_dataset**
> bytearray query_repository_dataset(x_repository_key, repository_uid, name, start, end=end, select=select, where=where, aggregate_window=aggregate_window, location_near=location_near, location_near_radius=location_near_radius, limit=limit, order_by=order_by, distinct=distinct)



Query a dataset with support for time ranges, field selection, filtering, and location-based queries

### Example

* Api Key Authentication (api_key):

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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.RepositoryApi(api_client)
    x_repository_key = 'x_repository_key_example' # str | The secret key used to access this repository
    repository_uid = 'rid:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    name = 'name_example' # str | The name of the data set
    start = 'start_example' # str | Start of the time range, as an ISO-8601 date or relative to now (e.g. -1y). Relative dates follow the Postgres INTERVAL format.
    end = 'end_example' # str | End of the time range, as an ISO-8601 date or relative to now. If omitted, current time is used. (optional)
    select = 'select_example' # str | Comma separated list of fields to include. Supports aggregate functions (avg, sum, min, max, count, most_recent). (optional)
    where = 'where_example' # str | Additional filters using boolean logic mini-language (e.g. and.(device.eq.dev:123,temp.gt.100)) (optional)
    aggregate_window = 'aggregate_window_example' # str | Aggregate results into buckets for a time duration, expressed in Postgres INTERVAL format (optional)
    location_near = '42.393125,-71.185015' # str | Latitude and Longitude for location-based filtering, location_near_radius must also be provided (optional)
    location_near_radius = 56 # int | Distance from location_near in meters, location_near must also be provided (optional)
    limit = 56 # int | Limit the number of results returned (optional)
    order_by = 'order_by_example' # str | Order the results by a field (optional)
    distinct = True # bool | Return only distinct results (optional)

    try:
        api_response = api_instance.query_repository_dataset(x_repository_key, repository_uid, name, start, end=end, select=select, where=where, aggregate_window=aggregate_window, location_near=location_near, location_near_radius=location_near_radius, limit=limit, order_by=order_by, distinct=distinct)
        print("The response of RepositoryApi->query_repository_dataset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->query_repository_dataset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_repository_key** | **str**| The secret key used to access this repository | 
 **repository_uid** | **str**|  | 
 **name** | **str**| The name of the data set | 
 **start** | **str**| Start of the time range, as an ISO-8601 date or relative to now (e.g. -1y). Relative dates follow the Postgres INTERVAL format. | 
 **end** | **str**| End of the time range, as an ISO-8601 date or relative to now. If omitted, current time is used. | [optional] 
 **select** | **str**| Comma separated list of fields to include. Supports aggregate functions (avg, sum, min, max, count, most_recent). | [optional] 
 **where** | **str**| Additional filters using boolean logic mini-language (e.g. and.(device.eq.dev:123,temp.gt.100)) | [optional] 
 **aggregate_window** | **str**| Aggregate results into buckets for a time duration, expressed in Postgres INTERVAL format | [optional] 
 **location_near** | **str**| Latitude and Longitude for location-based filtering, location_near_radius must also be provided | [optional] 
 **location_near_radius** | **int**| Distance from location_near in meters, location_near must also be provided | [optional] 
 **limit** | **int**| Limit the number of results returned | [optional] 
 **order_by** | **str**| Order the results by a field | [optional] 
 **distinct** | **bool**| Return only distinct results | [optional] 

### Return type

**bytearray**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful query |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_repository_sql**
> bytearray query_repository_sql(repository_uid, x_repository_key, body, x_click_house_format=x_click_house_format)



Run a raw Clickhouse-compatible SQL statement against the repository's database. Results are returned in CSV format

### Example

* Api Key Authentication (api_key):

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

# Configure API key authorization: api_key
configuration.api_key['api_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.RepositoryApi(api_client)
    repository_uid = 'rid:2606f411-dea6-44a0-9743-1130f57d77d8' # str | 
    x_repository_key = 'x_repository_key_example' # str | The secret key used to access this repository
    body = 'body_example' # str | Clickhouse-compatible SQL statement
    x_click_house_format = 'x_click_house_format_example' # str | Specify the format of the response data. This functions the same as the ClickHouse `FORMAT` clause. Supported values include `CSV`, `JSON`, `JSONEachRow`, `TabSeparated`, and `NDJSON`. If not specified, defaults to `TabSeparated`. (optional)

    try:
        api_response = api_instance.query_repository_sql(repository_uid, x_repository_key, body, x_click_house_format=x_click_house_format)
        print("The response of RepositoryApi->query_repository_sql:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoryApi->query_repository_sql: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_uid** | **str**|  | 
 **x_repository_key** | **str**| The secret key used to access this repository | 
 **body** | **str**| Clickhouse-compatible SQL statement | 
 **x_click_house_format** | **str**| Specify the format of the response data. This functions the same as the ClickHouse &#x60;FORMAT&#x60; clause. Supported values include &#x60;CSV&#x60;, &#x60;JSON&#x60;, &#x60;JSONEachRow&#x60;, &#x60;TabSeparated&#x60;, and &#x60;NDJSON&#x60;. If not specified, defaults to &#x60;TabSeparated&#x60;. | [optional] 

### Return type

**bytearray**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful query |  -  |
**0** | The response body in case of an API error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

