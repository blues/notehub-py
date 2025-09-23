# Thingworx

Route settings specific to ThingWorx routes. Only used for ThingWorx route types

## Properties

| Name            | Type                                | Description                                                                                    | Notes                      |
| --------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------- |
| **app_key**     | **str**                             | This value is input-only and will be omitted from the response and replaced with a placeholder | [optional]                 |
| **filter**      | [**AwsFilter**](AwsFilter.md)       |                                                                                                | [optional]                 |
| **fleets**      | **List[str]**                       | list of Fleet UIDs to apply route to, if any. If empty, applies to all Fleets                  | [optional]                 |
| **throttle_ms** | **int**                             |                                                                                                | [optional]                 |
| **timeout**     | **int**                             | Timeout in seconds for each request                                                            | [optional] [default to 15] |
| **transform**   | [**AwsTransform**](AwsTransform.md) |                                                                                                | [optional]                 |
| **url**         | **str**                             |                                                                                                | [optional]                 |

## Example

```python
from notehub_py.models.thingworx import Thingworx

# TODO update the JSON string below
json = "{}"
# create an instance of Thingworx from a JSON string
thingworx_instance = Thingworx.from_json(json)
# print the JSON string representation of the object
print(Thingworx.to_json())

# convert the object into a dict
thingworx_dict = thingworx_instance.to_dict()
# create an instance of Thingworx from a dict
thingworx_from_dict = Thingworx.from_dict(thingworx_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
