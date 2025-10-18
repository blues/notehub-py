# Filter

Filter applied to route data. Controls which notefiles are sent through the route.

## Properties

| Name                 | Type          | Description                                                                     | Notes      |
| -------------------- | ------------- | ------------------------------------------------------------------------------- | ---------- |
| **files**            | **List[str]** | List of notefile names or patterns to filter on.                                | [optional] |
| **system_notefiles** | **bool**      | Whether system notefiles should be included.                                    | [optional] |
| **type**             | **str**       | Type of filter to apply (corresponds to &#x60;hublib.NotefileFilterType&#x60;). | [optional] |

## Example

```python
from notehub_py.models.filter import Filter

# TODO update the JSON string below
json = "{}"
# create an instance of Filter from a JSON string
filter_instance = Filter.from_json(json)
# print the JSON string representation of the object
print(Filter.to_json())

# convert the object into a dict
filter_dict = filter_instance.to_dict()
# create an instance of Filter from a dict
filter_from_dict = Filter.from_dict(filter_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
