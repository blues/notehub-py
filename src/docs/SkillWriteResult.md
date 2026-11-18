# SkillWriteResult

## Properties

| Name        | Type                  | Description | Notes |
| ----------- | --------------------- | ----------- | ----- |
| **outcome** | **str**               |             |
| **skill**   | [**Skill**](Skill.md) |             |

## Example

```python
from notehub_py.models.skill_write_result import SkillWriteResult

# TODO update the JSON string below
json = "{}"
# create an instance of SkillWriteResult from a JSON string
skill_write_result_instance = SkillWriteResult.from_json(json)
# print the JSON string representation of the object
print(SkillWriteResult.to_json())

# convert the object into a dict
skill_write_result_dict = skill_write_result_instance.to_dict()
# create an instance of SkillWriteResult from a dict
skill_write_result_from_dict = SkillWriteResult.from_dict(skill_write_result_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
