# AwsTransform

## Properties

| Name        | Type    | Description                                                                                                                                                                                                                                     | Notes      |
| ----------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **format**  | **str** | Data transformation to apply. Options of \&quot;\&quot; for none, \&quot;bridge\&quot; for Azure IoT, \&quot;jsonata\&quot; for JSONata expression, or \&quot;flatten\&quot;, \&quot;simple\&quot;, \&quot;body\&quot; or \&quot;payload\&quot; | [optional] |
| **jsonata** | **str** | JSONata transformation, if JSONata                                                                                                                                                                                                              | [optional] |

## Example

```python
from notehub_py.models.aws_transform import AwsTransform

# TODO update the JSON string below
json = "{}"
# create an instance of AwsTransform from a JSON string
aws_transform_instance = AwsTransform.from_json(json)
# print the JSON string representation of the object
print(AwsTransform.to_json())

# convert the object into a dict
aws_transform_dict = aws_transform_instance.to_dict()
# create an instance of AwsTransform from a dict
aws_transform_from_dict = AwsTransform.from_dict(aws_transform_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
