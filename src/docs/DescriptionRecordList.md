# DescriptionRecordList

## Properties

| Name             | Type                                                | Description | Notes |
| ---------------- | --------------------------------------------------- | ----------- | ----- |
| **descriptions** | [**List[DescriptionRecord]**](DescriptionRecord.md) |             |

## Example

```python
from notehub_py.models.description_record_list import DescriptionRecordList

# TODO update the JSON string below
json = "{}"
# create an instance of DescriptionRecordList from a JSON string
description_record_list_instance = DescriptionRecordList.from_json(json)
# print the JSON string representation of the object
print(DescriptionRecordList.to_json())

# convert the object into a dict
description_record_list_dict = description_record_list_instance.to_dict()
# create an instance of DescriptionRecordList from a dict
description_record_list_from_dict = DescriptionRecordList.from_dict(
    description_record_list_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
