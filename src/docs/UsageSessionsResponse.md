# UsageSessionsResponse

## Properties

| Name     | Type                                                | Description | Notes |
| -------- | --------------------------------------------------- | ----------- | ----- |
| **data** | [**List[UsageSessionsData]**](UsageSessionsData.md) |             |

## Example

```python
from notehub_py.models.usage_sessions_response import UsageSessionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UsageSessionsResponse from a JSON string
usage_sessions_response_instance = UsageSessionsResponse.from_json(json)
# print the JSON string representation of the object
print(UsageSessionsResponse.to_json())

# convert the object into a dict
usage_sessions_response_dict = usage_sessions_response_instance.to_dict()
# create an instance of UsageSessionsResponse from a dict
usage_sessions_response_from_dict = UsageSessionsResponse.from_dict(usage_sessions_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
