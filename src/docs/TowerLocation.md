# TowerLocation

## Properties

| Name       | Type      | Description                                       | Notes      |
| ---------- | --------- | ------------------------------------------------- | ---------- |
| **source** | **str**   | The source of this location                       | [optional] |
| **time**   | **int**   | Unix timestamp when this location was ascertained | [optional] |
| **n**      | **str**   | Name of the location                              | [optional] |
| **c**      | **str**   | Country code                                      | [optional] |
| **lat**    | **float** | Latitude                                          | [optional] |
| **lon**    | **float** | Longitude                                         | [optional] |
| **zone**   | **str**   | Timezone name                                     | [optional] |
| **mcc**    | **int**   | Mobile Country Code                               | [optional] |
| **mnc**    | **int**   | Mobile Network Code                               | [optional] |
| **lac**    | **int**   | Location Area Code                                | [optional] |
| **cid**    | **int**   | Cell ID                                           | [optional] |
| **l**      | **str**   | Open Location Code                                | [optional] |
| **z**      | **int**   | Timezone ID                                       | [optional] |
| **towers** | **int**   | Number of triangulation points                    | [optional] |

## Example

```python
from notehub_py.models.tower_location import TowerLocation

# TODO update the JSON string below
json = "{}"
# create an instance of TowerLocation from a JSON string
tower_location_instance = TowerLocation.from_json(json)
# print the JSON string representation of the object
print(TowerLocation.to_json())

# convert the object into a dict
tower_location_dict = tower_location_instance.to_dict()
# create an instance of TowerLocation from a dict
tower_location_from_dict = TowerLocation.from_dict(tower_location_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
