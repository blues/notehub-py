# ArchiveStats

Statistics about a repository's data archive.

## Properties

| Name                 | Type         | Description                                                                                                                                                            | Notes      |
| -------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **begin**            | **datetime** | Timestamp of the earliest archived record.                                                                                                                             | [optional] |
| **end**              | **datetime** | Timestamp of the latest archived record.                                                                                                                               | [optional] |
| **file_count**       | **int**      | Number of archive files.                                                                                                                                               | [optional] |
| **record_count**     | **int**      | Total number of records across all archive files. Null when the count cannot be determined because one or more archive files predate the record-count filename format. | [optional] |
| **total_size_bytes** | **int**      | Total size of all archive files, in bytes.                                                                                                                             | [optional] |

## Example

```python
from notehub_py.models.archive_stats import ArchiveStats

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveStats from a JSON string
archive_stats_instance = ArchiveStats.from_json(json)
# print the JSON string representation of the object
print(ArchiveStats.to_json())

# convert the object into a dict
archive_stats_dict = archive_stats_instance.to_dict()
# create an instance of ArchiveStats from a dict
archive_stats_from_dict = ArchiveStats.from_dict(archive_stats_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
