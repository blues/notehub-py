# GetJobRuns200Response

## Properties

| Name     | Type                          | Description | Notes |
| -------- | ----------------------------- | ----------- | ----- |
| **runs** | [**List[JobRun]**](JobRun.md) |             |

## Example

```python
from notehub_py.models.get_job_runs200_response import GetJobRuns200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetJobRuns200Response from a JSON string
get_job_runs200_response_instance = GetJobRuns200Response.from_json(json)
# print the JSON string representation of the object
print(GetJobRuns200Response.to_json())

# convert the object into a dict
get_job_runs200_response_dict = get_job_runs200_response_instance.to_dict()
# create an instance of GetJobRuns200Response from a dict
get_job_runs200_response_from_dict = GetJobRuns200Response.from_dict(get_job_runs200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
