# DataSet

## Properties

| Name       | Type                                      | Description                                             | Notes      |
| ---------- | ----------------------------------------- | ------------------------------------------------------- | ---------- |
| **name**   | **str**                                   | The name of the data set                                | [optional] |
| **time**   | **str**                                   | JSONata expression resulting in the relevant time field | [optional] |
| **lat**    | **str**                                   | JSONata expression resulting in the latitude field      | [optional] |
| **lon**    | **str**                                   | JSONata expression resulting in the Longitude field     | [optional] |
| **fields** | [**List[DataSetField]**](DataSetField.md) |                                                         | [optional] |

## Example

```python
from notehub_py.models.data_set import DataSet

# TODO update the JSON string below
json = "{}"
# create an instance of DataSet from a JSON string
data_set_instance = DataSet.from_json(json)
# print the JSON string representation of the object
print(DataSet.to_json())

# convert the object into a dict
data_set_dict = data_set_instance.to_dict()
# create an instance of DataSet from a dict
data_set_from_dict = DataSet.from_dict(data_set_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
