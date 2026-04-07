# DeleteJob200Response

## Properties

| Name        | Type     | Description                     | Notes |
| ----------- | -------- | ------------------------------- | ----- |
| **success** | **bool** | True if deletion was successful |

## Example

```python
from notehub_py.models.delete_job200_response import DeleteJob200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteJob200Response from a JSON string
delete_job200_response_instance = DeleteJob200Response.from_json(json)
# print the JSON string representation of the object
print(DeleteJob200Response.to_json())

# convert the object into a dict
delete_job200_response_dict = delete_job200_response_instance.to_dict()
# create an instance of DeleteJob200Response from a dict
delete_job200_response_from_dict = DeleteJob200Response.from_dict(delete_job200_response_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
