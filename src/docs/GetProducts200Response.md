# GetProducts200Response

## Properties

| Name         | Type                            | Description | Notes      |
| ------------ | ------------------------------- | ----------- | ---------- |
| **products** | [**List[Product]**](Product.md) |             | [optional] |

## Example

```python
from notehub_py.models.get_products200_response import GetProducts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProducts200Response from a JSON string
get_products200_response_instance = GetProducts200Response.from_json(json)
# print the JSON string representation of the object
print(GetProducts200Response.to_json())

# convert the object into a dict
get_products200_response_dict = get_products200_response_instance.to_dict()
# create an instance of GetProducts200Response from a dict
get_products200_response_from_dict = GetProducts200Response.from_dict(get_products200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
