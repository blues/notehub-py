# JobRun

## Properties

| Name             | Type                  | Description                                                       | Notes      |
| ---------------- | --------------------- | ----------------------------------------------------------------- | ---------- |
| **cancel**       | **bool**              | Whether cancellation was requested                                | [optional] |
| **completed**    | **int**               | Unix timestamp when completed                                     | [optional] |
| **dry_run**      | **bool**              | Whether this was a dry run                                        |
| **job_name**     | **str**               | Name of the job                                                   |
| **job_uid**      | **str**               | Unique identifier for the job                                     |
| **report_uid**   | **str**               | Unique identifier for this run                                    |
| **results**      | **Dict[str, object]** | Full results (only in detail view)                                | [optional] |
| **started**      | **int**               | Unix timestamp when started                                       | [optional] |
| **status**       | **str**               | Current status (submitted, running, completed, cancelled, failed) |
| **submitted**    | **int**               | Unix timestamp when submitted                                     |
| **submitted_by** | **str**               | User who submitted the run                                        |
| **updated**      | **int**               | Unix timestamp of last update                                     |

## Example

```python
from notehub_py.models.job_run import JobRun

# TODO update the JSON string below
json = "{}"
# create an instance of JobRun from a JSON string
job_run_instance = JobRun.from_json(json)
# print the JSON string representation of the object
print(JobRun.to_json())

# convert the object into a dict
job_run_dict = job_run_instance.to_dict()
# create an instance of JobRun from a dict
job_run_from_dict = JobRun.from_dict(job_run_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
