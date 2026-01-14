# GetDataUsage200ResponseDataInner

## Properties

| Name             | Type                                | Description                                                                                 | Notes      |
| ---------------- | ----------------------------------- | ------------------------------------------------------------------------------------------- | ---------- |
| **data**         | [**List[UsageData]**](UsageData.md) |                                                                                             |
| **device**       | **str**                             | The device UID this usage data belongs to (only present when aggregate is &#39;device&#39;) | [optional] |
| **device_count** | **int**                             | the number of devices represented by this data point                                        | [optional] |
| **fleet**        | **str**                             | The fleet UID this usage data belongs to (only present when aggregate is &#39;fleet&#39;)   | [optional] |
| **iccid**        | **str**                             | The ICCID of the cellular SIM card (only present when type is &#39;cellular&#39;)           | [optional] |
| **psid**         | **str**                             | The PSID (Packet Service ID) of the satellite (or other packet-based device)                | [optional] |
| **type**         | **str**                             | The type of connectivity                                                                    |

## Example

```python
from notehub_py.models.get_data_usage200_response_data_inner import GetDataUsage200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetDataUsage200ResponseDataInner from a JSON string
get_data_usage200_response_data_inner_instance = GetDataUsage200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetDataUsage200ResponseDataInner.to_json())

# convert the object into a dict
get_data_usage200_response_data_inner_dict = get_data_usage200_response_data_inner_instance.to_dict()
# create an instance of GetDataUsage200ResponseDataInner from a dict
get_data_usage200_response_data_inner_from_dict = GetDataUsage200ResponseDataInner.from_dict(get_data_usage200_response_data_inner_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
