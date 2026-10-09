# GetApiUsage200Response

## Properties

| Name          | Type                                      | Description                                                                                     | Notes                                                  |
| ------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ---------- |
| **data**      | [**List[UsageApiData]**](UsageApiData.md) |                                                                                                 |
| **truncated** | **bool**                                  | If the data is truncated that means that the parameters selected resulted in a response of over | the requested limit of data points, in order to ensure | [optional] |

## Example

```python
from notehub_py.models.get_api_usage200_response import GetApiUsage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiUsage200Response from a JSON string
get_api_usage200_response_instance = GetApiUsage200Response.from_json(json)
# print the JSON string representation of the object
print(GetApiUsage200Response.to_json())

# convert the object into a dict
get_api_usage200_response_dict = get_api_usage200_response_instance.to_dict()
# create an instance of GetApiUsage200Response from a dict
get_api_usage200_response_from_dict = GetApiUsage200Response.from_dict(
    get_api_usage200_response_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
