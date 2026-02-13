# GetSessionsUsage200Response

## Properties

| Name          | Type                                                | Description                                                                                     | Notes                                                  |
| ------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **sessions**  | [**List[UsageSessionsData]**](UsageSessionsData.md) |                                                                                                 |
| **truncated** | **bool**                                            | If the data is truncated that means that the parameters selected resulted in a response of over | the requested limit of data points, in order to ensure |

## Example

```python
from notehub_py.models.get_sessions_usage200_response import GetSessionsUsage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSessionsUsage200Response from a JSON string
get_sessions_usage200_response_instance = GetSessionsUsage200Response.from_json(json)
# print the JSON string representation of the object
print(GetSessionsUsage200Response.to_json())

# convert the object into a dict
get_sessions_usage200_response_dict = get_sessions_usage200_response_instance.to_dict()
# create an instance of GetSessionsUsage200Response from a dict
get_sessions_usage200_response_from_dict = GetSessionsUsage200Response.from_dict(get_sessions_usage200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
