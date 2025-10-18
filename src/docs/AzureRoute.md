# AzureRoute

## Properties

| Name                     | Type                                                    | Description | Notes      |
| ------------------------ | ------------------------------------------------------- | ----------- | ---------- |
| **filter**               | [**Filter**](Filter.md)                                 |             | [optional] |
| **fleets**               | **List[str]**                                           |             | [optional] |
| **functions_key_secret** | **str**                                                 |             | [optional] |
| **sas_policy_key**       | **str**                                                 |             | [optional] |
| **sas_policy_name**      | **str**                                                 |             | [optional] |
| **throttle_ms**          | **int**                                                 |             | [optional] |
| **timeout**              | **int**                                                 |             | [optional] |
| **transform**            | [**RouteTransformSettings**](RouteTransformSettings.md) |             | [optional] |
| **url**                  | **str**                                                 |             | [optional] |

## Example

```python
from notehub_py.models.azure_route import AzureRoute

# TODO update the JSON string below
json = "{}"
# create an instance of AzureRoute from a JSON string
azure_route_instance = AzureRoute.from_json(json)
# print the JSON string representation of the object
print(AzureRoute.to_json())

# convert the object into a dict
azure_route_dict = azure_route_instance.to_dict()
# create an instance of AzureRoute from a dict
azure_route_from_dict = AzureRoute.from_dict(azure_route_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
