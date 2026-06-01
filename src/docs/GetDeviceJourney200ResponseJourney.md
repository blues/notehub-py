# GetDeviceJourney200ResponseJourney

Paginated `_track.qo` events for the journey.

## Properties

| Name         | Type                        | Description | Notes |
| ------------ | --------------------------- | ----------- | ----- |
| **events**   | [**List[Event]**](Event.md) |             |
| **has_more** | **bool**                    |             |

## Example

```python
from notehub_py.models.get_device_journey200_response_journey import (
    GetDeviceJourney200ResponseJourney,
)

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeviceJourney200ResponseJourney from a JSON string
get_device_journey200_response_journey_instance = (
    GetDeviceJourney200ResponseJourney.from_json(json)
)
# print the JSON string representation of the object
print(GetDeviceJourney200ResponseJourney.to_json())

# convert the object into a dict
get_device_journey200_response_journey_dict = (
    get_device_journey200_response_journey_instance.to_dict()
)
# create an instance of GetDeviceJourney200ResponseJourney from a dict
get_device_journey200_response_journey_from_dict = (
    GetDeviceJourney200ResponseJourney.from_dict(
        get_device_journey200_response_journey_dict
    )
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
