# CloneProjectRequest

## Properties

| Name                     | Type     | Description                                                                                                                            | Notes      |
| ------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **billing_account_uid**  | **str**  | UID of the organization that owns the new project. List them with &#x60;GetBillingAccounts&#x60;.                                      |
| **disable_clone_fleets** | **bool** | If &#x60;true&#x60;, the new project gets one default fleet instead of copies of this project&#39;s fleets. Default &#x60;false&#x60;. | [optional] |
| **disable_clone_routes** | **bool** | If &#x60;true&#x60;, the new project starts with no routes. Default &#x60;false&#x60;.                                                 | [optional] |
| **label**                | **str**  | Name of the new project.                                                                                                               |

## Example

```python
from notehub_py.models.clone_project_request import CloneProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CloneProjectRequest from a JSON string
clone_project_request_instance = CloneProjectRequest.from_json(json)
# print the JSON string representation of the object
print(CloneProjectRequest.to_json())

# convert the object into a dict
clone_project_request_dict = clone_project_request_instance.to_dict()
# create an instance of CloneProjectRequest from a dict
clone_project_request_from_dict = CloneProjectRequest.from_dict(
    clone_project_request_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
