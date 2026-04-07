# Job

## Properties

| Name           | Type                  | Description                               | Notes      |
| -------------- | --------------------- | ----------------------------------------- | ---------- |
| **created**    | **int**               | Unix timestamp when job was created       |
| **created_by** | **str**               | User who created the job                  |
| **definition** | **Dict[str, object]** | Full job definition (only in detail view) | [optional] |
| **job_uid**    | **str**               | Unique identifier for the job             |
| **name**       | **str**               | Human-readable job name                   |

## Example

```python
from notehub_py.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print(Job.to_json())

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_from_dict = Job.from_dict(job_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
