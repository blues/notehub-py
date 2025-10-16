# NotehubRouteSummary

## Properties

| Name         | Type         | Description | Notes                                                            |
| ------------ | ------------ | ----------- | ---------------------------------------------------------------- |
| **disabled** | **bool**     |             | [optional] [default to False]                                    |
| **label**    | **str**      |             | [optional] [default to 'success route']                          |
| **modified** | **datetime** |             | [optional] [readonly]                                            |
| **type**     | **str**      |             | [optional] [default to 'http']                                   |
| **uid**      | **str**      |             | [optional] [default to 'route:8d65a087d5d290ce5bdf03aeff2becc0'] |

## Example

```python
from notehub_py.models.notehub_route_summary import NotehubRouteSummary

# TODO update the JSON string below
json = "{}"
# create an instance of NotehubRouteSummary from a JSON string
notehub_route_summary_instance = NotehubRouteSummary.from_json(json)
# print the JSON string representation of the object
print(NotehubRouteSummary.to_json())

# convert the object into a dict
notehub_route_summary_dict = notehub_route_summary_instance.to_dict()
# create an instance of NotehubRouteSummary from a dict
notehub_route_summary_from_dict = NotehubRouteSummary.from_dict(notehub_route_summary_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
