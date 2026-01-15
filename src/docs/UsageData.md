# UsageData

## Properties

| Name                        | Type         | Description                                               | Notes      |
| --------------------------- | ------------ | --------------------------------------------------------- | ---------- |
| **billable_bytes_received** | **int**      | Billable bytes received (only for packet-based protocols) | [optional] |
| **billable_bytes_sent**     | **int**      | Billable bytes sent (only for packet-based protocols)     | [optional] |
| **billable_bytes_total**    | **int**      | Total billable bytes (only for packet-based protocols)    | [optional] |
| **bytes_received**          | **int**      |                                                           | [optional] |
| **bytes_sent**              | **int**      |                                                           | [optional] |
| **packets_received**        | **int**      | Packets received (only for packet-based protocols)        | [optional] |
| **packets_sent**            | **int**      | Packets sent (only for packet-based protocols)            | [optional] |
| **period**                  | **datetime** |                                                           |
| **total_bytes**             | **int**      |                                                           |

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
