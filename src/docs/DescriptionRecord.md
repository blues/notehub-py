# DescriptionRecord

Metadata for a stored description record. The content itself is returned by GET on the record.

## Properties

| Name             | Type    | Description                                                                                                     | Notes      |
| ---------------- | ------- | --------------------------------------------------------------------------------------------------------------- | ---------- |
| **content_type** | **str** | The stored content type, either \&quot;application/json\&quot; or \&quot;text/plain; charset&#x3D;utf-8\&quot;. |
| **created_at**   | **int** | When the record was first created (Unix seconds).                                                               |
| **created_by**   | **str** | The actor who created the record.                                                                               | [optional] |
| **length**       | **int** | The content length in bytes.                                                                                    |
| **md5**          | **str** | The hex-encoded MD5 of the content.                                                                             |
| **modified_at**  | **int** | When the record was last updated (Unix seconds).                                                                |
| **modified_by**  | **str** | The actor who last updated the record.                                                                          | [optional] |
| **name**         | **str** | The record name (letters, digits, &#39;.&#39;, &#39;\_&#39; or &#39;-&#39;).                                    |
| **owner_uid**    | **str** | The owning project (app) UID for project-scoped records; empty for global.                                      | [optional] |
| **scope**        | **str** | The ownership scope of the record (\&quot;global\&quot; or \&quot;project\&quot;).                              |

## Example

```python
from notehub_py.models.description_record import DescriptionRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DescriptionRecord from a JSON string
description_record_instance = DescriptionRecord.from_json(json)
# print the JSON string representation of the object
print(DescriptionRecord.to_json())

# convert the object into a dict
description_record_dict = description_record_instance.to_dict()
# create an instance of DescriptionRecord from a dict
description_record_from_dict = DescriptionRecord.from_dict(description_record_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
