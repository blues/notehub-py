# AwsFilter

Route filtering settings

## Properties

| Name                 | Type          | Description                                               | Notes      |
| -------------------- | ------------- | --------------------------------------------------------- | ---------- |
| **files**            | **List[str]** |                                                           | [optional] |
| **system_notefiles** | **bool**      | Whether system notefiles should be affected by this route | [optional] |
| **type**             | **str**       | What notefiles this route applies to.                     | [optional] |

## Example

```python
from notehub_py.models.aws_filter import AwsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AwsFilter from a JSON string
aws_filter_instance = AwsFilter.from_json(json)
# print the JSON string representation of the object
print(AwsFilter.to_json())

# convert the object into a dict
aws_filter_dict = aws_filter_instance.to_dict()
# create an instance of AwsFilter from a dict
aws_filter_from_dict = AwsFilter.from_dict(aws_filter_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
