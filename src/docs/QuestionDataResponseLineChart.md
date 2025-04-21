# QuestionDataResponseLineChart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Graph type must be &#39;lineChart&#39; for a line chart. | 
**title** | **str** | Title of the chart. | 
**var_property** | **str** | The property displayed as the Y-axis for the line chart. | 
**display_value** | **str** | Label of the Y-axis for the line chart. | 
**split_by** | **str** | Optional. Split the data by this property to create multiple lines on the chart. | [optional] 
**start_date** | **datetime** | Optional start date for filtering/charting data. | [optional] 
**end_date** | **datetime** | Optional end date for filtering/charting data. | [optional] 

## Example

```python
from notehub_py.models.question_data_response_line_chart import QuestionDataResponseLineChart

# TODO update the JSON string below
json = "{}"
# create an instance of QuestionDataResponseLineChart from a JSON string
question_data_response_line_chart_instance = QuestionDataResponseLineChart.from_json(json)
# print the JSON string representation of the object
print(QuestionDataResponseLineChart.to_json())

# convert the object into a dict
question_data_response_line_chart_dict = question_data_response_line_chart_instance.to_dict()
# create an instance of QuestionDataResponseLineChart from a dict
question_data_response_line_chart_from_dict = QuestionDataResponseLineChart.from_dict(question_data_response_line_chart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


