# QuestionDataResponseMap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Graph type must be &#39;map&#39; for a map visualization. | 
**title** | **str** | Title of the map. | 

## Example

```python
from notehub_py.models.question_data_response_map import QuestionDataResponseMap

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionDataResponseMap from a JSON string
question_data_response_map_instance = QuestionDataResponseMap.from_json(json)
# print the JSON string representation of the object
print(QuestionDataResponseMap.to_json())

# convert the object into a dict
question_data_response_map_dict = question_data_response_map_instance.to_dict()
# create an instance of QuestionDataResponseMap from a dict
question_data_response_map_from_dict = QuestionDataResponseMap.from_dict(question_data_response_map_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


