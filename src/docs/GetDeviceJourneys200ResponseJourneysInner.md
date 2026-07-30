# GetDeviceJourneys200ResponseJourneysInner

## Properties

| Name             | Type         | Description                                                                                                                                                            | Notes |
| ---------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| **end_date**     | **datetime** | Latest event time within the journey.                                                                                                                                  |
| **journey_id**   | **int**      | Identifier of the journey, taken from the numeric &#x60;journey&#x60; field in the event body. This value is itself a Unix timestamp marking the start of the journey. |
| **start_date**   | **datetime** | Earliest event time within the journey.                                                                                                                                |
| **total_events** | **int**      | The number of events in the journey.                                                                                                                                   |

## Example

```python
from notehub_py.models.get_device_journeys200_response_journeys_inner import (
    GetDeviceJourneys200ResponseJourneysInner,
)

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeviceJourneys200ResponseJourneysInner from a JSON string
get_device_journeys200_response_journeys_inner_instance = (
    GetDeviceJourneys200ResponseJourneysInner.from_json(json)
)
# print the JSON string representation of the object
print(GetDeviceJourneys200ResponseJourneysInner.to_json())

# convert the object into a dict
get_device_journeys200_response_journeys_inner_dict = (
    get_device_journeys200_response_journeys_inner_instance.to_dict()
)
# create an instance of GetDeviceJourneys200ResponseJourneysInner from a dict
get_device_journeys200_response_journeys_inner_from_dict = (
    GetDeviceJourneys200ResponseJourneysInner.from_dict(
        get_device_journeys200_response_journeys_inner_dict
    )
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
