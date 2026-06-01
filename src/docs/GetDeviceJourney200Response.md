# GetDeviceJourney200Response

## Properties

| Name           | Type                                                                            | Description                             | Notes |
| -------------- | ------------------------------------------------------------------------------- | --------------------------------------- | ----- |
| **end_date**   | **datetime**                                                                    | Latest event time within the journey.   |
| **journey**    | [**GetDeviceJourney200ResponseJourney**](GetDeviceJourney200ResponseJourney.md) |                                         |
| **journey_id** | **int**                                                                         | Identifier of the journey.              |
| **start_date** | **datetime**                                                                    | Earliest event time within the journey. |

## Example

```python
from notehub_py.models.get_device_journey200_response import GetDeviceJourney200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeviceJourney200Response from a JSON string
get_device_journey200_response_instance = GetDeviceJourney200Response.from_json(json)
# print the JSON string representation of the object
print(GetDeviceJourney200Response.to_json())

# convert the object into a dict
get_device_journey200_response_dict = get_device_journey200_response_instance.to_dict()
# create an instance of GetDeviceJourney200Response from a dict
get_device_journey200_response_from_dict = GetDeviceJourney200Response.from_dict(
    get_device_journey200_response_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
