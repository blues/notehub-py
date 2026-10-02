# DatasetReloadProgress

Live progress of an in-flight reload of this dataset; absent when not reloading.

## Properties

| Name                      | Type         | Description                                                                                                                                        | Notes      |
| ------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **archive_records_read**  | **int**      | Archived records read so far.                                                                                                                      | [optional] |
| **archive_records_total** | **int**      | Approximate total archived records to read. Null when it cannot be determined because some archive files predate the record-count filename format. | [optional] |
| **started**               | **datetime** | When this reload started.                                                                                                                          | [optional] |
| **tail_records_read**     | **int**      | Unarchived (Kafka tail) records read so far.                                                                                                       | [optional] |

## Example

```python
from notehub_py.models.dataset_reload_progress import DatasetReloadProgress

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetReloadProgress from a JSON string
dataset_reload_progress_instance = DatasetReloadProgress.from_json(json)
# print the JSON string representation of the object
print(DatasetReloadProgress.to_json())

# convert the object into a dict
dataset_reload_progress_dict = dataset_reload_progress_instance.to_dict()
# create an instance of DatasetReloadProgress from a dict
dataset_reload_progress_from_dict = DatasetReloadProgress.from_dict(
    dataset_reload_progress_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
