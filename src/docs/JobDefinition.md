# JobDefinition

Batch job definition

## Properties

| Name                 | Type                                                            | Description                                            | Notes      |
| -------------------- | --------------------------------------------------------------- | ------------------------------------------------------ | ---------- |
| **comment**          | **str**                                                         | Human-readable description of the job                  | [optional] |
| **default_requests** | [**BatchJobRequests**](BatchJobRequests.md)                     |                                                        | [optional] |
| **device_requests**  | [**Dict[str, BatchJobRequests]**](BatchJobRequests.md)          | Device-specific request overrides, keyed by device UID | [optional] |
| **report_options**   | [**JobDefinitionReportOptions**](JobDefinitionReportOptions.md) |                                                        | [optional] |
| **select**           | [**JobDefinitionSelect**](JobDefinitionSelect.md)               |                                                        | [optional] |

## Example

```python
from notehub_py.models.job_definition import JobDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of JobDefinition from a JSON string
job_definition_instance = JobDefinition.from_json(json)
# print the JSON string representation of the object
print(JobDefinition.to_json())

# convert the object into a dict
job_definition_dict = job_definition_instance.to_dict()
# create an instance of JobDefinition from a dict
job_definition_from_dict = JobDefinition.from_dict(job_definition_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
