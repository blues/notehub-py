# SkillLinks

## Properties

| Name         | Type    | Description                        | Notes |
| ------------ | ------- | ---------------------------------- | ----- |
| **catalog**  | **str** | Relative metadata catalog URL.     |
| **var_self** | **str** | Relative URL for this named skill. |

## Example

```python
from notehub_py.models.skill_links import SkillLinks

# TODO update the JSON string below
json = "{}"
# create an instance of SkillLinks from a JSON string
skill_links_instance = SkillLinks.from_json(json)
# print the JSON string representation of the object
print(SkillLinks.to_json())

# convert the object into a dict
skill_links_dict = skill_links_instance.to_dict()
# create an instance of SkillLinks from a dict
skill_links_from_dict = SkillLinks.from_dict(skill_links_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
