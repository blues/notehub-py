# GetDataUsage200Response

## Properties

| Name     | Type                                                                              | Description | Notes      |
| -------- | --------------------------------------------------------------------------------- | ----------- | ---------- |
| **data** | [**List[GetDataUsage200ResponseDataInner]**](GetDataUsage200ResponseDataInner.md) |             | [optional] |

## Example

```python
from notehub_py.models.get_data_usage200_response import GetDataUsage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataUsage200Response from a JSON string
get_data_usage200_response_instance = GetDataUsage200Response.from_json(json)
# print the JSON string representation of the object
print(GetDataUsage200Response.to_json())

# convert the object into a dict
get_data_usage200_response_dict = get_data_usage200_response_instance.to_dict()
# create an instance of GetDataUsage200Response from a dict
get_data_usage200_response_from_dict = GetDataUsage200Response.from_dict(get_data_usage200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
