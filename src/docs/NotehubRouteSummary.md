# NotehubRouteSummary

## Properties

| Name         | Type         | Description                                        | Notes                                                            |
| ------------ | ------------ | -------------------------------------------------- | ---------------------------------------------------------------- |
| **disabled** | **bool**     | True if the route is turned off and sends nothing. | [optional] [default to False]                                    |
| **label**    | **str**      | Route name.                                        | [optional] [default to 'success route']                          |
| **modified** | **datetime** | When the route was last changed.                   | [optional] [readonly]                                            |
| **type**     | **str**      | Route type; see &#x60;NotehubRoute.type&#x60;.     | [optional] [default to 'http']                                   |
| **uid**      | **str**      | RouteUID.                                          | [optional] [default to 'route:8d65a087d5d290ce5bdf03aeff2becc0'] |

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
notehub_route_summary_from_dict = NotehubRouteSummary.from_dict(
    notehub_route_summary_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
