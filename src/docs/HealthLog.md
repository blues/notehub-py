# HealthLog

## Properties

| Name      | Type         | Description | Notes |
| --------- | ------------ | ----------- | ----- |
| **alert** | **bool**     |             |
| **text**  | **str**      |             |
| **when**  | **datetime** |             |

## Example

```python
from notehub_py.models.health_log import HealthLog

# TODO update the JSON string below
json = "{}"
# create an instance of HealthLog from a JSON string
health_log_instance = HealthLog.from_json(json)
# print the JSON string representation of the object
print(HealthLog.to_json())

# convert the object into a dict
health_log_dict = health_log_instance.to_dict()
# create an instance of HealthLog from a dict
health_log_from_dict = HealthLog.from_dict(health_log_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
