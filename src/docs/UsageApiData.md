# UsageApiData

## Properties

| Name         | Type         | Description                                                                                                                                                                 | Notes      |
| ------------ | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **endpoint** | **str**      | The templated path of the endpoint the requests were made against, with path parameters left unsubstituted. Empty if the endpoint could not be resolved for these requests. | [optional] |
| **method**   | **str**      | The HTTP method of the requests counted in this data point. Empty if the endpoint could not be resolved for these requests.                                                 | [optional] |
| **period**   | **datetime** |                                                                                                                                                                             |
| **requests** | **int**      | Number of billable API requests in this period.                                                                                                                             |

## Example

```python
from notehub_py.models.usage_api_data import UsageApiData

# TODO update the JSON string below
json = "{}"
# create an instance of UsageApiData from a JSON string
usage_api_data_instance = UsageApiData.from_json(json)
# print the JSON string representation of the object
print(UsageApiData.to_json())

# convert the object into a dict
usage_api_data_dict = usage_api_data_instance.to_dict()
# create an instance of UsageApiData from a dict
usage_api_data_from_dict = UsageApiData.from_dict(usage_api_data_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
