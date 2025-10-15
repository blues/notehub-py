# UsageSessionsData

## Properties

| Name            | Type         | Description | Notes      |
| --------------- | ------------ | ----------- | ---------- |
| **device**      | **str**      |             | [optional] |
| **fleet**       | **str**      |             | [optional] |
| **period**      | **datetime** |             |
| **sessions**    | **int**      |             |
| **total_bytes** | **int**      |             |

## Example

```python
from notehub_py.models.usage_sessions_data import UsageSessionsData

# TODO update the JSON string below
json = "{}"
# create an instance of UsageSessionsData from a JSON string
usage_sessions_data_instance = UsageSessionsData.from_json(json)
# print the JSON string representation of the object
print(UsageSessionsData.to_json())

# convert the object into a dict
usage_sessions_data_dict = usage_sessions_data_instance.to_dict()
# create an instance of UsageSessionsData from a dict
usage_sessions_data_from_dict = UsageSessionsData.from_dict(usage_sessions_data_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
