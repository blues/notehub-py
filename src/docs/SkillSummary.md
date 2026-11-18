# SkillSummary

Skill metadata, with content only when includeContent=true.

## Properties

| Name           | Type                            | Description                                                                               | Notes      |
| -------------- | ------------------------------- | ----------------------------------------------------------------------------------------- | ---------- |
| **content**    | **str**                         | Exact Markdown when includeContent&#x3D;true; present even when empty. Otherwise omitted. | [optional] |
| **created_at** | **datetime**                    |                                                                                           |
| **kinds**      | **List[str]**                   | Effective stored kinds, independent of document front matter.                             |
| **links**      | [**SkillLinks**](SkillLinks.md) |                                                                                           |
| **name**       | **str**                         |                                                                                           |
| **revision**   | **str**                         | Opaque concurrency token; ETag is this value wrapped in double quotes.                    |
| **size_bytes** | **int**                         | UTF-8 content byte count.                                                                 |
| **updated_at** | **datetime**                    |                                                                                           |

## Example

```python
from notehub_py.models.skill_summary import SkillSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SkillSummary from a JSON string
skill_summary_instance = SkillSummary.from_json(json)
# print the JSON string representation of the object
print(SkillSummary.to_json())

# convert the object into a dict
skill_summary_dict = skill_summary_instance.to_dict()
# create an instance of SkillSummary from a dict
skill_summary_from_dict = SkillSummary.from_dict(skill_summary_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
