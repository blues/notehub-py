# GetJobs200Response

## Properties

| Name     | Type                    | Description | Notes |
| -------- | ----------------------- | ----------- | ----- |
| **jobs** | [**List[Job]**](Job.md) |             |

## Example

```python
from notehub_py.models.get_jobs200_response import GetJobs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetJobs200Response from a JSON string
get_jobs200_response_instance = GetJobs200Response.from_json(json)
# print the JSON string representation of the object
print(GetJobs200Response.to_json())

# convert the object into a dict
get_jobs200_response_dict = get_jobs200_response_instance.to_dict()
# create an instance of GetJobs200Response from a dict
get_jobs200_response_from_dict = GetJobs200Response.from_dict(get_jobs200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
