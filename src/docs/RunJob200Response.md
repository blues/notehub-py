# RunJob200Response

## Properties

| Name           | Type    | Description                        | Notes |
| -------------- | ------- | ---------------------------------- | ----- |
| **report_uid** | **str** | Unique identifier for this job run |

## Example

```python
from notehub_py.models.run_job200_response import RunJob200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RunJob200Response from a JSON string
run_job200_response_instance = RunJob200Response.from_json(json)
# print the JSON string representation of the object
print(RunJob200Response.to_json())

# convert the object into a dict
run_job200_response_dict = run_job200_response_instance.to_dict()
# create an instance of RunJob200Response from a dict
run_job200_response_from_dict = RunJob200Response.from_dict(run_job200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
