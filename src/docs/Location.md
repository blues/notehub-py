# Location

## Properties

| Name          | Type      | Description                                                           | Notes |
| ------------- | --------- | --------------------------------------------------------------------- | ----- |
| **country**   | **str**   | Two-letter country code, e.g. &#x60;US&#x60;.                         |
| **latitude**  | **float** | Latitude in degrees.                                                  |
| **longitude** | **float** | Longitude in degrees.                                                 |
| **name**      | **str**   | Place name, e.g. &#x60;Waverly MI&#x60;.                              |
| **timezone**  | **str**   | IANA time zone, e.g. &#x60;America/Detroit&#x60;.                     |
| **when**      | **str**   | When the location was recorded, in RFC 3339 format. Empty if unknown. |

## Example

```python
from notehub_py.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print(Location.to_json())

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_from_dict = Location.from_dict(location_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
