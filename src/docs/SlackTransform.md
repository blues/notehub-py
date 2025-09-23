# SlackTransform

## Properties

| Name        | Type    | Description                                                                            | Notes                             |
| ----------- | ------- | -------------------------------------------------------------------------------------- | --------------------------------- |
| **format**  | **str** | Data transformation to apply. Only \&quot;jsonata\&quot; is valid for Snowflake routes | [optional] [default to 'jsonata'] |
| **jsonata** | **str** | JSONata transformation                                                                 | [optional]                        |

## Example

```python
from notehub_py.models.slack_transform import SlackTransform

# TODO update the JSON string below
json = "{}"
# create an instance of SlackTransform from a JSON string
slack_transform_instance = SlackTransform.from_json(json)
# print the JSON string representation of the object
print(SlackTransform.to_json())

# convert the object into a dict
slack_transform_dict = slack_transform_instance.to_dict()
# create an instance of SlackTransform from a dict
slack_transform_from_dict = SlackTransform.from_dict(slack_transform_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
