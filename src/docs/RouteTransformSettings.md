# RouteTransformSettings

Settings for transforming route payloads before delivery. Supports format selection and JSONata-based transformations.

## Properties

| Name           | Type    | Description                                                                                           | Notes      |
| -------------- | ------- | ----------------------------------------------------------------------------------------------------- | ---------- |
| **format**     | **str** | Output format for transformed data (e.g., \&quot;json\&quot;, \&quot;xml\&quot;, \&quot;text\&quot;). | [optional] |
| **jsonata**    | **str** | JSONata expression used to transform the data payload (outgoing).                                     | [optional] |
| **jsonata_in** | **str** | JSONata expression used to transform the data payload (incoming).                                     | [optional] |

## Example

```python
from notehub_py.models.route_transform_settings import RouteTransformSettings

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTransformSettings from a JSON string
route_transform_settings_instance = RouteTransformSettings.from_json(json)
# print the JSON string representation of the object
print(RouteTransformSettings.to_json())

# convert the object into a dict
route_transform_settings_dict = route_transform_settings_instance.to_dict()
# create an instance of RouteTransformSettings from a dict
route_transform_settings_from_dict = RouteTransformSettings.from_dict(route_transform_settings_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
