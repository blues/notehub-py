# EnvTreeJsonNode

## Properties

| Name                    | Type                                            | Description | Notes      |
| ----------------------- | ----------------------------------------------- | ----------- | ---------- |
| **var_count**           | [**Int**](Int.md)                               |             |
| **inherited_var_count** | [**Int**](Int.md)                               |             |
| **type**                | **str**                                         |             |
| **variables**           | [**List[EnvVar]**](EnvVar.md)                   |             |
| **children**            | [**List[EnvTreeJsonNode]**](EnvTreeJsonNode.md) |             |
| **device_uid**          | **str**                                         |             | [optional] |
| **fleet_label**         | **str**                                         |             | [optional] |
| **fleet_uid**           | **str**                                         |             | [optional] |
| **app_uid**             | **str**                                         |             | [optional] |
| **app_label**           | **str**                                         |             | [optional] |
| **url**                 | **str**                                         |             | [optional] |

## Example

```python
from notehub_py.models.env_tree_json_node import EnvTreeJsonNode

# TODO update the JSON string below
json = "{}"
# create an instance of EnvTreeJsonNode from a JSON string
env_tree_json_node_instance = EnvTreeJsonNode.from_json(json)
# print the JSON string representation of the object
print(EnvTreeJsonNode.to_json())

# convert the object into a dict
env_tree_json_node_dict = env_tree_json_node_instance.to_dict()
# create an instance of EnvTreeJsonNode from a dict
env_tree_json_node_from_dict = EnvTreeJsonNode.from_dict(env_tree_json_node_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
