# S3ArchiveRoute

## Properties

| Name                      | Type                                                    | Description | Notes      |
| ------------------------- | ------------------------------------------------------- | ----------- | ---------- |
| **archive_count_exceeds** | **int**                                                 |             | [optional] |
| **archive_every_mins**    | **int**                                                 |             | [optional] |
| **archive_id**            | **str**                                                 |             | [optional] |
| **bucket_endpoint**       | **str**                                                 |             | [optional] |
| **bucket_name**           | **str**                                                 |             | [optional] |
| **bucket_region**         | **str**                                                 |             | [optional] |
| **file_access**           | **str**                                                 |             | [optional] |
| **file_folder**           | **str**                                                 |             | [optional] |
| **file_format**           | **str**                                                 |             | [optional] |
| **filter**                | [**Filter**](Filter.md)                                 |             | [optional] |
| **fleets**                | **List[str]**                                           |             | [optional] |
| **key_id**                | **str**                                                 |             | [optional] |
| **key_secret**            | **str**                                                 |             | [optional] |
| **throttle_ms**           | **int**                                                 |             | [optional] |
| **timeout**               | **int**                                                 |             | [optional] |
| **transform**             | [**RouteTransformSettings**](RouteTransformSettings.md) |             | [optional] |
| **url**                   | **str**                                                 |             | [optional] |

## Example

```python
from notehub_py.models.s3_archive_route import S3ArchiveRoute

# TODO update the JSON string below
json = "{}"
# create an instance of S3ArchiveRoute from a JSON string
s3_archive_route_instance = S3ArchiveRoute.from_json(json)
# print the JSON string representation of the object
print(S3ArchiveRoute.to_json())

# convert the object into a dict
s3_archive_route_dict = s3_archive_route_instance.to_dict()
# create an instance of S3ArchiveRoute from a dict
s3_archive_route_from_dict = S3ArchiveRoute.from_dict(s3_archive_route_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
