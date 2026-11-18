# CreateProjectRequest

## Properties

| Name                    | Type    | Description                                                                                                     | Notes |
| ----------------------- | ------- | --------------------------------------------------------------------------------------------------------------- | ----- |
| **billing_account_uid** | **str** | UID of the organization that owns and is billed for the project. List them with &#x60;GetBillingAccounts&#x60;. |
| **label**               | **str** | Project name shown in Notehub.                                                                                  |

## Example

```python
from notehub_py.models.create_project_request import CreateProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProjectRequest from a JSON string
create_project_request_instance = CreateProjectRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProjectRequest.to_json())

# convert the object into a dict
create_project_request_dict = create_project_request_instance.to_dict()
# create an instance of CreateProjectRequest from a dict
create_project_request_from_dict = CreateProjectRequest.from_dict(
    create_project_request_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
