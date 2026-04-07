# CreateJob201Response

## Properties

| Name        | Type    | Description                               | Notes |
| ----------- | ------- | ----------------------------------------- | ----- |
| **job_uid** | **str** | The unique identifier for the created job |

## Example

```python
from notehub_py.models.create_job201_response import CreateJob201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateJob201Response from a JSON string
create_job201_response_instance = CreateJob201Response.from_json(json)
# print the JSON string representation of the object
print(CreateJob201Response.to_json())

# convert the object into a dict
create_job201_response_dict = create_job201_response_instance.to_dict()
# create an instance of CreateJob201Response from a dict
create_job201_response_from_dict = CreateJob201Response.from_dict(create_job201_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
