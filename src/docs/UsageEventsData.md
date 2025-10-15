# UsageEventsData

## Properties

| Name                | Type         | Description | Notes      |
| ------------------- | ------------ | ----------- | ---------- |
| **device**          | **str**      |             | [optional] |
| **fleet**           | **str**      |             | [optional] |
| **period**          | **datetime** |             |
| **platform_events** | **int**      |             |
| **total_events**    | **int**      |             |

## Example

```python
from notehub_py.models.usage_events_data import UsageEventsData

# TODO update the JSON string below
json = "{}"
# create an instance of UsageEventsData from a JSON string
usage_events_data_instance = UsageEventsData.from_json(json)
# print the JSON string representation of the object
print(UsageEventsData.to_json())

# convert the object into a dict
usage_events_data_dict = usage_events_data_instance.to_dict()
# create an instance of UsageEventsData from a dict
usage_events_data_from_dict = UsageEventsData.from_dict(usage_events_data_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
