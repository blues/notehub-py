# SatelliteDataUsage

## Properties

| Name                    | Type    | Description                      | Notes |
| ----------------------- | ------- | -------------------------------- | ----- |
| **bytes_remaining**     | **int** | Bytes remaining in the plan      |
| **bytes_total**         | **int** | Total bytes included in the plan |
| **bytes_used**          | **int** | Bytes used to date               |
| **bytes_used_billable** | **int** | Billable bytes used to date      |

## Example

```python
from notehub_py.models.satellite_data_usage import SatelliteDataUsage

# TODO update the JSON string below
json = "{}"
# create an instance of SatelliteDataUsage from a JSON string
satellite_data_usage_instance = SatelliteDataUsage.from_json(json)
# print the JSON string representation of the object
print(SatelliteDataUsage.to_json())

# convert the object into a dict
satellite_data_usage_dict = satellite_data_usage_instance.to_dict()
# create an instance of SatelliteDataUsage from a dict
satellite_data_usage_from_dict = SatelliteDataUsage.from_dict(satellite_data_usage_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
