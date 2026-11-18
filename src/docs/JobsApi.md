# notehub_py.JobsApi

All URIs are relative to *https://api.notefile.net*

| Method                                          | HTTP request                                                             | Description           |
| ----------------------------------------------- | ------------------------------------------------------------------------ | --------------------- |
| [**cancel_job_run**](JobsApi.md#cancel_job_run) | **POST** /v1/projects/{projectOrProductUID}/jobs/runs/{reportUID}/cancel | Cancel a job run      |
| [**create_job**](JobsApi.md#create_job)         | **POST** /v1/projects/{projectOrProductUID}/jobs                         | Create a batch job    |
| [**delete_job**](JobsApi.md#delete_job)         | **DELETE** /v1/projects/{projectOrProductUID}/jobs/{jobUID}              | Delete a batch job    |
| [**delete_job_run**](JobsApi.md#delete_job_run) | **DELETE** /v1/projects/{projectOrProductUID}/jobs/runs/{reportUID}      | Delete a job run      |
| [**get_job**](JobsApi.md#get_job)               | **GET** /v1/projects/{projectOrProductUID}/jobs/{jobUID}                 | Get a batch job       |
| [**get_job_run**](JobsApi.md#get_job_run)       | **GET** /v1/projects/{projectOrProductUID}/jobs/runs/{reportUID}         | Get a job run         |
| [**get_job_runs**](JobsApi.md#get_job_runs)     | **GET** /v1/projects/{projectOrProductUID}/jobs/{jobUID}/runs            | List a job&#39;s runs |
| [**get_jobs**](JobsApi.md#get_jobs)             | **GET** /v1/projects/{projectOrProductUID}/jobs                          | List batch jobs       |
| [**run_job**](JobsApi.md#run_job)               | **POST** /v1/projects/{projectOrProductUID}/jobs/{jobUID}/run            | Run a batch job       |

## cancel_job_run

> CancelJobRun200Response cancel_job_run(project_or_product_uid, report_uid)

Cancel a job run

Ask a running job to stop. `successful` is false if the run couldn't be cancelled. Requires the Owner or Developer role. Returns 404 if the run doesn't exist.

### Example

```python
import notehub_py
from notehub_py.models.cancel_job_run200_response import CancelJobRun200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.JobsApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    report_uid = "my-reconciliation-job-1707654321000"  # str | Job run UID, as returned by `RunJob`.

    try:
        # Cancel a job run
        api_response = api_instance.cancel_job_run(project_or_product_uid, report_uid)
        print("The response of JobsApi->cancel_job_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->cancel_job_run: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                     | Notes |
| -------------------------- | ------- | ----------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                 |
| **report_uid**             | **str** | Job run UID, as returned by &#x60;RunJob&#x60;. |

### Return type

[**CancelJobRun200Response**](CancelJobRun200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## create_job

> CreateJob201Response create_job(project_or_product_uid, name, job_definition)

Create a batch job

Create a batch job from a definition that selects devices and the changes to make to them. It doesn't run until `RunJob`. Each call creates a new job with its own UID; names needn't be unique. Requires the Owner or Developer role. Returns 400 without a `name`; an invalid definition returns 500.

### Example

```python
import notehub_py
from notehub_py.models.create_job201_response import CreateJob201Response
from notehub_py.models.job_definition import JobDefinition
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.JobsApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    name = (
        "name_example"  # str | Job name, shown in lists. It doesn't have to be unique.
    )
    job_definition = (
        notehub_py.JobDefinition()
    )  # JobDefinition | The batch job definition

    try:
        # Create a batch job
        api_response = api_instance.create_job(
            project_or_product_uid, name, job_definition
        )
        print("The response of JobsApi->create_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->create_job: %s\n" % e)
```

### Parameters

| Name                       | Type                                  | Description                                                 | Notes |
| -------------------------- | ------------------------------------- | ----------------------------------------------------------- | ----- |
| **project_or_product_uid** | **str**                               |                                                             |
| **name**                   | **str**                               | Job name, shown in lists. It doesn&#39;t have to be unique. |
| **job_definition**         | [**JobDefinition**](JobDefinition.md) | The batch job definition                                    |

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

Delete a batch job. Requires the Owner or Developer role. Returns 404 if the job doesn't exist.

### Example

```python
import notehub_py
from notehub_py.models.delete_job200_response import DeleteJob200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.JobsApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    job_uid = (
        "my-reconciliation-job"  # str | Batch job UID, as returned by `CreateJob`.
    )

    try:
        # Delete a batch job
        api_response = api_instance.delete_job(project_or_product_uid, job_uid)
        print("The response of JobsApi->delete_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->delete_job: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                          | Notes |
| -------------------------- | ------- | ---------------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                      |
| **job_uid**                | **str** | Batch job UID, as returned by &#x60;CreateJob&#x60;. |

### Return type

[**DeleteJob200Response**](DeleteJob200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## delete_job_run

> delete_job_run(project_or_product_uid, report_uid)

Delete a job run

Delete a job run and its results. Deleting a run that doesn't exist also succeeds. Requires the Owner or Developer role.

### Example

```python
import notehub_py
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.JobsApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    report_uid = "my-reconciliation-job-1707654321000"  # str | Job run UID, as returned by `RunJob`.

    try:
        # Delete a job run
        api_instance.delete_job_run(project_or_product_uid, report_uid)
    except Exception as e:
        print("Exception when calling JobsApi->delete_job_run: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                     | Notes |
| -------------------------- | ------- | ----------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                 |
| **report_uid**             | **str** | Job run UID, as returned by &#x60;RunJob&#x60;. |

### Return type

void (empty response body)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_job

> JobDetail get_job(project_or_product_uid, job_uid)

Get a batch job

Get one batch job's definition and its latest run's status. Returns 404 if the job doesn't exist.

### Example

```python
import notehub_py
from notehub_py.models.job_detail import JobDetail
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.JobsApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    job_uid = (
        "my-reconciliation-job"  # str | Batch job UID, as returned by `CreateJob`.
    )

    try:
        # Get a batch job
        api_response = api_instance.get_job(project_or_product_uid, job_uid)
        print("The response of JobsApi->get_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                          | Notes |
| -------------------------- | ------- | ---------------------------------------------------- | ----- |
| **project_or_product_uid** | **str** |                                                      |
| **job_uid**                | **str** | Batch job UID, as returned by &#x60;CreateJob&#x60;. |

### Return type

[**JobDetail**](JobDetail.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_job_run

> JobRun get_job_run(project_or_product_uid, report_uid, view=view)

Get a job run

Get a job run's status and, with `view=detail`, its full results. Returns 404 if the run doesn't exist.

### Example

```python
import notehub_py
from notehub_py.models.job_run import JobRun
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.JobsApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    report_uid = "my-reconciliation-job-1707654321000"  # str | Job run UID, as returned by `RunJob`.
    view = "summary"  # str | Controls the level of detail returned: 'summary' returns metadata only, 'detail' returns the full result payload (optional) (default to 'summary')

    try:
        # Get a job run
        api_response = api_instance.get_job_run(
            project_or_product_uid, report_uid, view=view
        )
        print("The response of JobsApi->get_job_run:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_run: %s\n" % e)
```

### Parameters

| Name                       | Type    | Description                                                                                                                      | Notes                                     |
| -------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **project_or_product_uid** | **str** |                                                                                                                                  |
| **report_uid**             | **str** | Job run UID, as returned by &#x60;RunJob&#x60;.                                                                                  |
| **view**                   | **str** | Controls the level of detail returned: &#39;summary&#39; returns metadata only, &#39;detail&#39; returns the full result payload | [optional] [default to &#39;summary&#39;] |

### Return type

[**JobRun**](JobRun.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_job_runs

> GetJobRuns200Response get_job_runs(project_or_product_uid, job_uid, status=status, dry_run=dry_run)

List a job's runs

List a batch job's runs, optionally filtered by status or dry-run flag. Returns 404 if the job doesn't exist.

### Example

```python
import notehub_py
from notehub_py.models.get_job_runs200_response import GetJobRuns200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.JobsApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    job_uid = (
        "my-reconciliation-job"  # str | Batch job UID, as returned by `CreateJob`.
    )
    status = "status_example"  # str | Return only runs with this status. (optional)
    dry_run = True  # bool | If set, return only dry runs (`true`) or only real runs (`false`). (optional)

    try:
        # List a job's runs
        api_response = api_instance.get_job_runs(
            project_or_product_uid, job_uid, status=status, dry_run=dry_run
        )
        print("The response of JobsApi->get_job_runs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get_job_runs: %s\n" % e)
```

### Parameters

| Name                       | Type     | Description                                                                            | Notes      |
| -------------------------- | -------- | -------------------------------------------------------------------------------------- | ---------- |
| **project_or_product_uid** | **str**  |                                                                                        |
| **job_uid**                | **str**  | Batch job UID, as returned by &#x60;CreateJob&#x60;.                                   |
| **status**                 | **str**  | Return only runs with this status.                                                     | [optional] |
| **dry_run**                | **bool** | If set, return only dry runs (&#x60;true&#x60;) or only real runs (&#x60;false&#x60;). | [optional] |

### Return type

[**GetJobRuns200Response**](GetJobRuns200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

## get_jobs

> GetJobs200Response get_jobs(project_or_product_uid)

List batch jobs

List a project's batch jobs with their latest run's status. A batch job applies changes, such as environment variables, to a selected set of devices.

### Example

```python
import notehub_py
from notehub_py.models.get_jobs200_response import GetJobs200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.JobsApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |

    try:
        # List batch jobs
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

Run a batch job

Start a run of a batch job and return its run UID. The run continues in the background, and `GetJobRun` shows its progress. With `dry_run=true`, it reports what would change without changing anything. Requires the Owner or Developer role. Returns 404 if the job doesn't exist.

### Example

```python
import notehub_py
from notehub_py.models.run_job200_response import RunJob200Response
from notehub_py.rest import ApiException
from pprint import pprint

configuration = notehub_py.Configuration(access_token="PERSONAL_ACCESS_TOKEN")

# Enter a context with an instance of the API client
with notehub_py.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notehub_py.JobsApi(api_client)
    project_or_product_uid = "app:2606f411-dea6-44a0-9743-1130f57d77d8"  # str |
    job_uid = (
        "my-reconciliation-job"  # str | Batch job UID, as returned by `CreateJob`.
    )
    dry_run = False  # bool | If true, report what the job would change without changing anything. (optional) (default to False)

    try:
        # Run a batch job
        api_response = api_instance.run_job(
            project_or_product_uid, job_uid, dry_run=dry_run
        )
        print("The response of JobsApi->run_job:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->run_job: %s\n" % e)
```

### Parameters

| Name                       | Type     | Description                                                          | Notes                         |
| -------------------------- | -------- | -------------------------------------------------------------------- | ----------------------------- |
| **project_or_product_uid** | **str**  |                                                                      |
| **job_uid**                | **str**  | Batch job UID, as returned by &#x60;CreateJob&#x60;.                 |
| **dry_run**                | **bool** | If true, report what the job would change without changing anything. | [optional] [default to False] |

### Return type

[**RunJob200Response**](RunJob200Response.md)

### Authorization

[personalAccessToken](../README.md#personalAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json
