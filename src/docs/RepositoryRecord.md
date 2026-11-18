# RepositoryRecord

One event in a repository's archive, with the session it arrived in and the device's environment at the time. `GetRepositoryData` returns one per line, and dataset JSONata expressions and Python functions read one at a time, as in `event.body.temp`. `session` is often absent, and `env` is absent in older records.

## Properties

| Name        | Type                                  | Description                                                                                          | Notes      |
| ----------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------- |
| **env**     | **Dict[str, str]**                    | The device&#39;s environment variables when the event arrived, after merging project and fleet ones. | [optional] |
| **event**   | [**Event**](Event.md)                 |                                                                                                      | [optional] |
| **session** | [**DeviceSession**](DeviceSession.md) |                                                                                                      | [optional] |

## Example

```python
from notehub_py.models.repository_record import RepositoryRecord

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoryRecord from a JSON string
repository_record_instance = RepositoryRecord.from_json(json)
# print the JSON string representation of the object
print(RepositoryRecord.to_json())

# convert the object into a dict
repository_record_dict = repository_record_instance.to_dict()
# create an instance of RepositoryRecord from a dict
repository_record_from_dict = RepositoryRecord.from_dict(repository_record_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
