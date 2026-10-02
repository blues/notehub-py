# DataSetField

## Properties

| Name         | Type    | Description                                                                                                                                                                                                                                                                                                            | Notes      |
| ------------ | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **datatype** | **int** | The datatype of the field                                                                                                                                                                                                                                                                                              | [optional] |
| **jsonata**  | **str** | The JSONata expression that populates this field from the event. Required for a dataset with no rows expression. Must be omitted when the dataset has one: the column is then taken from the row object key matching this field&#39;s name, and supplying an expression here is rejected rather than silently ignored. | [optional] |
| **name**     | **str** | The name of the field                                                                                                                                                                                                                                                                                                  | [optional] |

## Example

```python
from notehub_py.models.data_set_field import DataSetField

# TODO update the JSON string below
json = "{}"
# create an instance of DataSetField from a JSON string
data_set_field_instance = DataSetField.from_json(json)
# print the JSON string representation of the object
print(DataSetField.to_json())

# convert the object into a dict
data_set_field_dict = data_set_field_instance.to_dict()
# create an instance of DataSetField from a dict
data_set_field_from_dict = DataSetField.from_dict(data_set_field_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
