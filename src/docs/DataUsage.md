# DataUsage

## Properties

| Name             | Type      | Description                          | Notes |
| ---------------- | --------- | ------------------------------------ | ----- |
| **kb_remaining** | **float** | Kilobytes remaining in the plan      |
| **kb_total**     | **float** | Total Kilobytes included in the plan |
| **kb_used**      | **float** | Kilobytes used to date               |

## Example

```python
from notehub_py.models.data_usage import DataUsage

# TODO update the JSON string below
json = "{}"
# create an instance of DataUsage from a JSON string
data_usage_instance = DataUsage.from_json(json)
# print the JSON string representation of the object
print(DataUsage.to_json())

# convert the object into a dict
data_usage_dict = data_usage_instance.to_dict()
# create an instance of DataUsage from a dict
data_usage_from_dict = DataUsage.from_dict(data_usage_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
