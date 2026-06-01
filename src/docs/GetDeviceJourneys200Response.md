# GetDeviceJourneys200Response

## Properties

| Name         | Type                                                                                                | Description | Notes |
| ------------ | --------------------------------------------------------------------------------------------------- | ----------- | ----- |
| **has_more** | **bool**                                                                                            |             |
| **journeys** | [**List[GetDeviceJourneys200ResponseJourneysInner]**](GetDeviceJourneys200ResponseJourneysInner.md) |             |

## Example

```python
from notehub_py.models.get_device_journeys200_response import (
    GetDeviceJourneys200Response,
)

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeviceJourneys200Response from a JSON string
get_device_journeys200_response_instance = GetDeviceJourneys200Response.from_json(json)
# print the JSON string representation of the object
print(GetDeviceJourneys200Response.to_json())

# convert the object into a dict
get_device_journeys200_response_dict = (
    get_device_journeys200_response_instance.to_dict()
)
# create an instance of GetDeviceJourneys200Response from a dict
get_device_journeys200_response_from_dict = GetDeviceJourneys200Response.from_dict(
    get_device_journeys200_response_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
