# GetDevicePlans200Response

## Properties

| Name               | Type                                      | Description | Notes      |
| ------------------ | ----------------------------------------- | ----------- | ---------- |
| **cellular_plans** | [**List[CellularPlan]**](CellularPlan.md) |             | [optional] |

## Example

```python
from notehub_py.models.get_device_plans200_response import GetDevicePlans200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDevicePlans200Response from a JSON string
get_device_plans200_response_instance = GetDevicePlans200Response.from_json(json)
# print the JSON string representation of the object
print(GetDevicePlans200Response.to_json())

# convert the object into a dict
get_device_plans200_response_dict = get_device_plans200_response_instance.to_dict()
# create an instance of GetDevicePlans200Response from a dict
get_device_plans200_response_from_dict = GetDevicePlans200Response.from_dict(get_device_plans200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
