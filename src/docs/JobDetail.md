# JobDetail

Batch job with full definition

## Properties

| Name                   | Type                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                        | Notes      |
| ---------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **created**            | **int**                               | Unix timestamp when job was created                                                                                                                                                                                                                                                                                                                                                                                |
| **created_by**         | **str**                               | User who created the job                                                                                                                                                                                                                                                                                                                                                                                           |
| **job_uid**            | **str**                               | Unique identifier for the job                                                                                                                                                                                                                                                                                                                                                                                      |
| **last_run_completed** | **int**                               | Unix timestamp when the most recent run completed (0 if still in progress)                                                                                                                                                                                                                                                                                                                                         | [optional] |
| **last_run_status**    | **str**                               | Status of the most recent job run. Terminal values are: \&quot;submitted\&quot;, \&quot;completed successfully\&quot;, \&quot;dry run completed successfully\&quot;, \&quot;completed with errors\&quot;, \&quot;cancelled\&quot;. While a job is running, intermediate per-device progress updates may appear (e.g. \&quot;dev:000000000000000 completed\&quot;, \&quot;dev:000000000000000 updated: ...\&quot;). | [optional] |
| **last_run_submitted** | **int**                               | Unix timestamp when the most recent run was submitted                                                                                                                                                                                                                                                                                                                                                              | [optional] |
| **name**               | **str**                               | Human-readable job name                                                                                                                                                                                                                                                                                                                                                                                            |
| **definition**         | [**JobDefinition**](JobDefinition.md) |                                                                                                                                                                                                                                                                                                                                                                                                                    | [optional] |

## Example

```python
from notehub_py.models.job_detail import JobDetail

# TODO update the JSON string below
json = "{}"
# create an instance of JobDetail from a JSON string
job_detail_instance = JobDetail.from_json(json)
# print the JSON string representation of the object
print(JobDetail.to_json())

# convert the object into a dict
job_detail_dict = job_detail_instance.to_dict()
# create an instance of JobDetail from a dict
job_detail_from_dict = JobDetail.from_dict(job_detail_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
