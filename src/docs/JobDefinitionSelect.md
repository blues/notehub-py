# JobDefinitionSelect

Device selection criteria

## Properties

| Name                  | Type          | Description                                                            | Notes      |
| --------------------- | ------------- | ---------------------------------------------------------------------- | ---------- |
| **all_devices**       | **bool**      | Select all devices in the project                                      | [optional] |
| **comment**           | **str**       |                                                                        | [optional] |
| **devices**           | **List[str]** | Specific device UIDs to include                                        | [optional] |
| **devices_by_sn**     | **List[str]** | Serial number patterns to match (supports glob wildcards \*, ?, [...]) | [optional] |
| **devices_in_fleets** | **List[str]** | Fleet UIDs whose devices should be included                            | [optional] |

## Example

```python
from notehub_py.models.job_definition_select import JobDefinitionSelect

# TODO update the JSON string below
json = "{}"
# create an instance of JobDefinitionSelect from a JSON string
job_definition_select_instance = JobDefinitionSelect.from_json(json)
# print the JSON string representation of the object
print(JobDefinitionSelect.to_json())

# convert the object into a dict
job_definition_select_dict = job_definition_select_instance.to_dict()
# create an instance of JobDefinitionSelect from a dict
job_definition_select_from_dict = JobDefinitionSelect.from_dict(
    job_definition_select_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
