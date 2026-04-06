# CancelJobRun200Response

## Properties

| Name           | Type     | Description                         | Notes |
| -------------- | -------- | ----------------------------------- | ----- |
| **successful** | **bool** | True if cancellation was successful |

## Example

```python
from notehub_py.models.cancel_job_run200_response import CancelJobRun200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CancelJobRun200Response from a JSON string
cancel_job_run200_response_instance = CancelJobRun200Response.from_json(json)
# print the JSON string representation of the object
print(CancelJobRun200Response.to_json())

# convert the object into a dict
cancel_job_run200_response_dict = cancel_job_run200_response_instance.to_dict()
# create an instance of CancelJobRun200Response from a dict
cancel_job_run200_response_from_dict = CancelJobRun200Response.from_dict(cancel_job_run200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
