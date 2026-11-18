# DescriptionRecord

Metadata for a stored description record. The content itself is returned by GET on the record.

## Properties

| Name             | Type    | Description                                                                                                                             | Notes      |
| ---------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **content_type** | **str** | The Content-Type served on GET, as sent when the record was stored or detected from its content.                                        |
| **created_at**   | **int** | When the record was first created (Unix seconds).                                                                                       |
| **created_by**   | **str** | The actor who created the record.                                                                                                       | [optional] |
| **length**       | **int** | The content length in bytes.                                                                                                            |
| **md5**          | **str** | The hex-encoded MD5 of the content.                                                                                                     |
| **modified_at**  | **int** | When the record was last updated (Unix seconds).                                                                                        |
| **modified_by**  | **str** | The actor who last updated the record.                                                                                                  | [optional] |
| **name**         | **str** | The record name (letters, digits, &#39;.&#39;, &#39;\_&#39; or &#39;-&#39;).                                                            |
| **owner_uid**    | **str** | ProjectUID of the owning project, e.g. &#x60;app:2606f411-dea6-44a0-9743-1130f57d77d8&#x60;. Empty for a global record.                 | [optional] |
| **scope**        | **str** | Where the record is stored. - &#x60;project&#x60;: in one project - &#x60;global&#x60;: platform-wide, readable by every signed-in user |

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
