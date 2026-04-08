# notehub_py.JobsApi

All URIs are relative to *https://api.notefile.net*

| Method                                          | HTTP request                                                             | Description |
| ----------------------------------------------- | ------------------------------------------------------------------------ | ----------- |
| [**cancel_job_run**](JobsApi.md#cancel_job_run) | **POST** /v1/projects/{projectOrProductUID}/jobs/runs/{reportUID}/cancel |
| [**create_job**](JobsApi.md#create_job)         | **POST** /v1/projects/{projectOrProductUID}/jobs                         |
| [**delete_job**](JobsApi.md#delete_job)         | **DELETE** /v1/projects/{projectOrProductUID}/jobs/{jobUID}              |
| [**get_job**](JobsApi.md#get_job)               | **GET** /v1/projects/{projectOrProductUID}/jobs/{jobUID}                 |
| [**get_job_run**](JobsApi.md#get_job_run)       | **GET** /v1/projects/{projectOrProductUID}/jobs/runs/{reportUID}         |
| [**get_job_runs**](JobsApi.md#get_job_runs)     | **GET** /v1/projects/{projectOrProductUID}/jobs/{jobUID}/runs            |
| [**get_jobs**](JobsApi.md#get_jobs)             | **GET** /v1/projects/{projectOrProductUID}/jobs                          |
| [**run_job**](JobsApi.md#run_job)               | **POST** /v1/projects/{projectOrProductUID}/jobs/{jobUID}/run            |

## cancel_job_run

> CancelJobRun200Response cancel_job_run(project_or_product_uid, report_uid)

Cancel a running job execution

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.cancel_job_run200_response import CancelJobRun200Response
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
    api_instance = notehub_py.JobsApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    report_uid = 'my-reconciliation-job-1707654321000' # str | Unique identifier for a job run report

    try:
        api_response = api_instance.cancel_job_run(project_or_product_uid, report_uid)
        print("The response of JobsApi->cancel_job_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->cancel_job_run: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                            | Notes |
| -------------------------- | ------- | -------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                        |
| **report_uid**             | **str** | Unique identifier for a job run report |

### Return type

[**CancelJobRun200Response**](CancelJobRun200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## create_job

> CreateJob201Response create_job(project_or_product_uid, name, body)

Create a new batch job with an optional name

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.create_job201_response import CreateJob201Response
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
    api_instance = notehub_py.JobsApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    name = 'name_example' # str | Name for the job
    body = None # object | The job definition as raw JSON

    try:
        api_response = api_instance.create_job(project_or_product_uid, name, body)
        print("The response of JobsApi->create_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->create_job: %s\n" % e)
```

### Parameters

| Name                       | Type       | Description                    | Notes |
| -------------------------- | ---------- | ------------------------------ | ----- |
| **project_or_product_uid** | **str**    |                                |
| **name**                   | **str**    | Name for the job               |
| **body**                   | **object** | The job definition as raw JSON |

### Return type

[**CreateJob201Response**](CreateJob201Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

## delete_job

> DeleteJob200Response delete_job(project_or_product_uid, job_uid)

Delete a batch job

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.delete_job200_response import DeleteJob200Response
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
    api_instance = notehub_py.JobsApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    job_uid = 'my-reconciliation-job' # str | Unique identifier for a batch job

    try:
        api_response = api_instance.delete_job(project_or_product_uid, job_uid)
        print("The response of JobsApi->delete_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->delete_job: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                       | Notes |
| -------------------------- | ------- | --------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                   |
| **job_uid**                | **str** | Unique identifier for a batch job |

### Return type

[**DeleteJob200Response**](DeleteJob200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_job

> Job get_job(project_or_product_uid, job_uid)

Get a specific batch job definition

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.job import Job
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
    api_instance = notehub_py.JobsApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    job_uid = 'my-reconciliation-job' # str | Unique identifier for a batch job

    try:
        api_response = api_instance.get_job(project_or_product_uid, job_uid)
        print("The response of JobsApi->get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                       | Notes |
| -------------------------- | ------- | --------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                   |
| **job_uid**                | **str** | Unique identifier for a batch job |

### Return type

[**Job**](Job.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_job_run

> JobRun get_job_run(project_or_product_uid, report_uid)

Get the result of a job execution

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.job_run import JobRun
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
    api_instance = notehub_py.JobsApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    report_uid = 'my-reconciliation-job-1707654321000' # str | Unique identifier for a job run report

    try:
        api_response = api_instance.get_job_run(project_or_product_uid, report_uid)
        print("The response of JobsApi->get_job_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_run: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                            | Notes |
| -------------------------- | ------- | -------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                        |
| **report_uid**             | **str** | Unique identifier for a job run report |

### Return type

[**JobRun**](JobRun.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_job_runs

> GetJobRuns200Response get_job_runs(project_or_product_uid, job_uid, status=status, dry_run=dry_run)

List all runs for a specific job

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_job_runs200_response import GetJobRuns200Response
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
    api_instance = notehub_py.JobsApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    job_uid = 'my-reconciliation-job' # str | Unique identifier for a batch job
    status = 'status_example' # str | Filter runs by status (optional)
    dry_run = True # bool | Filter runs by dry run flag (optional)

    try:
        api_response = api_instance.get_job_runs(project_or_product_uid, job_uid, status=status, dry_run=dry_run)
        print("The response of JobsApi->get_job_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_runs: %s\n" % e)
```

### Parameters

| Name                       | Type     | Description                       | Notes      |
| -------------------------- | -------- | --------------------------------- | ---------- |
| **project_or_product_uid** | **str**  |                                   |
| **job_uid**                | **str**  | Unique identifier for a batch job |
| **status**                 | **str**  | Filter runs by status             | [optional] |
| **dry_run**                | **bool** | Filter runs by dry run flag       | [optional] |

### Return type

[**GetJobRuns200Response**](GetJobRuns200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_jobs

> GetJobs200Response get_jobs(project_or_product_uid)

List all batch jobs for a project

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.get_jobs200_response import GetJobs200Response
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
    api_instance = notehub_py.JobsApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |

    try:
        api_response = api_instance.get_jobs(project_or_product_uid)
        print("The response of JobsApi->get_jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_jobs: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description | Notes |
| -------------------------- | ------- | ----------- | ----- |
| **project_or_product_uid** | **str** |             |

### Return type

[**GetJobs200Response**](GetJobs200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## run_job

> RunJob200Response run_job(project_or_product_uid, job_uid, dry_run=dry_run)

Execute a batch job

### Example

- Bearer Authentication (personalAccessToken):

```python
import notehub_py
from notehub_py.models.run_job200_response import RunJob200Response
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
    api_instance = notehub_py.JobsApi(api_client)
    project_or_product_uid = 'app:2606f411-dea6-44a0-9743-1130f57d77d8' # str |
    job_uid = 'my-reconciliation-job' # str | Unique identifier for a batch job
    dry_run = False # bool | Run job in dry-run mode without making actual changes (optional) (default to False)

    try:
        api_response = api_instance.run_job(project_or_product_uid, job_uid, dry_run=dry_run)
        print("The response of JobsApi->run_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->run_job: %s\n" % e)
```

### Parameters

| Name                       | Type     | Description                                           | Notes                         |
| -------------------------- | -------- | ----------------------------------------------------- | ----------------------------- |
| **project_or_product_uid** | **str**  |                                                       |
| **job_uid**                | **str**  | Unique identifier for a batch job                     |
| **dry_run**                | **bool** | Run job in dry-run mode without making actual changes | [optional] [default to False] |

### Return type

[**RunJob200Response**](RunJob200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json
