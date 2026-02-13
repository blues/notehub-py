# UsageData

## Properties

| Name                        | Type         | Description                                               | Notes      |
| --------------------------- | ------------ | --------------------------------------------------------- | ---------- |
| **billable_bytes_total**    | **int**      | Total billable bytes (only for packet-based protocols)    | [optional] |
| **downlink_bytes**          | **int**      |                                                           | [optional] |
| **downlink_bytes_billable** | **int**      | Billable downlink bytes (only for packet-based protocols) | [optional] |
| **downlink_packets**        | **int**      | Downlink packets (only for packet-based protocols)        | [optional] |
| **period**                  | **datetime** |                                                           |
| **total_bytes**             | **int**      |                                                           |
| **uplink_bytes**            | **int**      |                                                           | [optional] |
| **uplink_bytes_billable**   | **int**      | Billable uplink bytes (only for packet-based protocols)   | [optional] |
| **uplink_packets**          | **int**      | Uplink packets (only for packet-based protocols)          | [optional] |

## Example

```python
from notehub_py.models.usage_data import UsageData

# TODO update the JSON string below
json = "{}"
# create an instance of UsageData from a JSON string
usage_data_instance = UsageData.from_json(json)
# print the JSON string representation of the object
print(UsageData.to_json())

# convert the object into a dict
usage_data_dict = usage_data_instance.to_dict()
# create an instance of UsageData from a dict
usage_data_from_dict = UsageData.from_dict(usage_data_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
