# SkillWrite

## Properties

| Name        | Type          | Description                                                                                                                                | Notes      |
| ----------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **content** | **str**       | Exact UTF-8, at most 1 MiB decoded. Empty is valid; null is not. JSON request limit is 2 MiB plus 64 KiB, including escaping and metadata. |
| **kinds**   | **List[str]** | Lowercase kinds; publish is reserved. Omit to preserve on replacement, or use [] to clear.                                                 | [optional] |

## Example

```python
from notehub_py.models.skill_write import SkillWrite

# TODO update the JSON string below
json = "{}"
# create an instance of SkillWrite from a JSON string
skill_write_instance = SkillWrite.from_json(json)
# print the JSON string representation of the object
print(SkillWrite.to_json())

# convert the object into a dict
skill_write_dict = skill_write_instance.to_dict()
# create an instance of SkillWrite from a dict
skill_write_from_dict = SkillWrite.from_dict(skill_write_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
