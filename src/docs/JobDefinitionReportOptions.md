# JobDefinitionReportOptions

Controls what data is included in the job report

## Properties

| Name                | Type     | Description                                         | Notes      |
| ------------------- | -------- | --------------------------------------------------- | ---------- |
| **app_fleets**      | **bool** | Include project fleets in the report                | [optional] |
| **app_info**        | **bool** | Include project info in the report                  | [optional] |
| **app_vars**        | **bool** | Include project environment variables in the report | [optional] |
| **comment**         | **str**  |                                                     | [optional] |
| **device_activity** | **bool** | Include device activity data in the report          | [optional] |
| **device_health**   | **bool** | Include device health data in the report            | [optional] |
| **device_info**     | **bool** | Include device info in the report                   | [optional] |
| **device_vars**     | **bool** | Include device environment variables in the report  | [optional] |

## Example

```python
from notehub_py.models.job_definition_report_options import JobDefinitionReportOptions

# TODO update the JSON string below
json = "{}"
# create an instance of JobDefinitionReportOptions from a JSON string
job_definition_report_options_instance = JobDefinitionReportOptions.from_json(json)
# print the JSON string representation of the object
print(JobDefinitionReportOptions.to_json())

# convert the object into a dict
job_definition_report_options_dict = job_definition_report_options_instance.to_dict()
# create an instance of JobDefinitionReportOptions from a dict
job_definition_report_options_from_dict = JobDefinitionReportOptions.from_dict(
    job_definition_report_options_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
