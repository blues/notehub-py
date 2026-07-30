# DataSet

## Properties

| Name             | Type                                      | Description                                                                                                                                 | Notes                 |
| ---------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **fields**       | [**List[DataSetField]**](DataSetField.md) |                                                                                                                                             | [optional]            |
| **is_optimized** | **bool**                                  | True once the dataset&#39;s underlying table has been deduplicated/optimized. Server-populated; ignored on input.                           | [optional] [readonly] |
| **is_ready**     | **bool**                                  | True once the dataset has been fully loaded from the repository&#39;s archive after backfill completed. Server-populated; ignored on input. | [optional] [readonly] |
| **lat**          | **str**                                   | JSONata expression resulting in the latitude field                                                                                          | [optional]            |
| **lon**          | **str**                                   | JSONata expression resulting in the Longitude field                                                                                         | [optional]            |
| **name**         | **str**                                   | The name of the data set                                                                                                                    | [optional]            |
| **notefiles**    | **List[str]**                             | If non-empty, only events from these notefiles populate the dataset. Empty or omitted means all notefiles.                                  | [optional]            |
| **time**         | **str**                                   | JSONata expression resulting in the relevant time field                                                                                     | [optional]            |

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
