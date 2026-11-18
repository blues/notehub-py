# SkillSet

Complete skill collection from one snapshot. Content is included only when requested.

## Properties

| Name             | Type                                      | Description                                                  | Notes |
| ---------------- | ----------------------------------------- | ------------------------------------------------------------ | ----- |
| **complete**     | **bool**                                  | Always true for a successful response; no silent truncation. |
| **project_uid**  | **str**                                   |                                                              |
| **set_revision** | **str**                                   |                                                              |
| **skills**       | [**List[SkillSummary]**](SkillSummary.md) |                                                              |
| **total**        | **int**                                   |                                                              |

## Example

```python
from notehub_py.models.skill_set import SkillSet

# TODO update the JSON string below
json = "{}"
# create an instance of SkillSet from a JSON string
skill_set_instance = SkillSet.from_json(json)
# print the JSON string representation of the object
print(SkillSet.to_json())

# convert the object into a dict
skill_set_dict = skill_set_instance.to_dict()
# create an instance of SkillSet from a dict
skill_set_from_dict = SkillSet.from_dict(skill_set_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
