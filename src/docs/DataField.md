# DataField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the field | [optional] 

## Example

```python
from notehub_py.models.data_field import DataField

# TODO update the JSON string below
json = "{}"
# create an instance of DataField from a JSON string
data_field_instance = DataField.from_json(json)
# print the JSON string representation of the object
print(DataField.to_json())

# convert the object into a dict
data_field_dict = data_field_instance.to_dict()
# create an instance of DataField from a dict
data_field_from_dict = DataField.from_dict(data_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


