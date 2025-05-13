# SchemaProperty

## Properties

| Name           | Type                                          | Description                                            | Notes      |
| -------------- | --------------------------------------------- | ------------------------------------------------------ | ---------- |
| **name**       | **str**                                       | Name of the field (optional for array/object children) | [optional] |
| **type**       | **str**                                       |                                                        |
| **updated_at** | **datetime**                                  |                                                        |
| **items**      | [**List[SchemaProperty]**](SchemaProperty.md) | Used if type is array                                  | [optional] |
| **properties** | [**List[SchemaProperty]**](SchemaProperty.md) | Used if type is object                                 | [optional] |

## Example

```python
from notehub_py.models.schema_property import SchemaProperty

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaProperty from a JSON string
schema_property_instance = SchemaProperty.from_json(json)
# print the JSON string representation of the object
print(SchemaProperty.to_json())

# convert the object into a dict
schema_property_dict = schema_property_instance.to_dict()
# create an instance of SchemaProperty from a dict
schema_property_from_dict = SchemaProperty.from_dict(schema_property_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
