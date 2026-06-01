# BatchJobRequests

Operations to apply to a device

## Properties

| Name                               | Type               | Description                                                          | Notes      |
| ---------------------------------- | ------------------ | -------------------------------------------------------------------- | ---------- |
| **comment**                        | **str**            |                                                                      | [optional] |
| **connectivity_assurance_disable** | **bool**           | Disable connectivity assurance for the device                        | [optional] |
| **connectivity_assurance_enable**  | **bool**           | Enable connectivity assurance for the device                         | [optional] |
| **disable**                        | **bool**           | Disable the device                                                   | [optional] |
| **enable**                         | **bool**           | Enable the device                                                    | [optional] |
| **fleets_to_default**              | **List[str]**      | Fleet UIDs to assign to the device if it has no fleets               | [optional] |
| **fleets_to_join**                 | **List[str]**      | Fleet UIDs to add the device to                                      | [optional] |
| **fleets_to_leave**                | **List[str]**      | Fleet UIDs to remove the device from                                 | [optional] |
| **provision_product**              | **str**            | Product UID to provision the device with if not already provisioned  | [optional] |
| **sn_to_default**                  | **str**            | Set the device serial number only if not already set                 | [optional] |
| **sn_to_set**                      | **str**            | Set the device serial number (\&quot;-\&quot; to clear)              | [optional] |
| **vars_to_default**                | **Dict[str, str]** | Environment variables to set only if not already set                 | [optional] |
| **vars_to_set**                    | **Dict[str, str]** | Environment variables to set (use \&quot;-\&quot; as value to clear) | [optional] |

## Example

```python
from notehub_py.models.batch_job_requests import BatchJobRequests

# TODO update the JSON string below
json = "{}"
# create an instance of BatchJobRequests from a JSON string
batch_job_requests_instance = BatchJobRequests.from_json(json)
# print the JSON string representation of the object
print(BatchJobRequests.to_json())

# convert the object into a dict
batch_job_requests_dict = batch_job_requests_instance.to_dict()
# create an instance of BatchJobRequests from a dict
batch_job_requests_from_dict = BatchJobRequests.from_dict(batch_job_requests_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
