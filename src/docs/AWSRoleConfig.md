# AWSRoleConfig

Configuration needed to set up an IAM role trust policy for role-based authentication on AWS routes

## Properties

| Name               | Type    | Description                                                           | Notes |
| ------------------ | ------- | --------------------------------------------------------------------- | ----- |
| **aws_account_id** | **str** | The Blues AWS Account ID to trust in your IAM role&#39;s trust policy |
| **external_id**    | **str** | The External ID to use in your IAM role&#39;s trust policy condition  |

## Example

```python
from notehub_py.models.aws_role_config import AWSRoleConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AWSRoleConfig from a JSON string
aws_role_config_instance = AWSRoleConfig.from_json(json)
# print the JSON string representation of the object
print(AWSRoleConfig.to_json())

# convert the object into a dict
aws_role_config_dict = aws_role_config_instance.to_dict()
# create an instance of AWSRoleConfig from a dict
aws_role_config_from_dict = AWSRoleConfig.from_dict(aws_role_config_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
