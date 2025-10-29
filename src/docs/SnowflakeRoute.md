# SnowflakeRoute

## Properties

| Name                  | Type                                                    | Description | Notes      |
| --------------------- | ------------------------------------------------------- | ----------- | ---------- |
| **account_name**      | **str**                                                 |             | [optional] |
| **filter**            | [**Filter**](Filter.md)                                 |             | [optional] |
| **fleets**            | **List[str]**                                           |             | [optional] |
| **organization_name** | **str**                                                 |             | [optional] |
| **pem**               | **str**                                                 |             | [optional] |
| **private_key_name**  | **str**                                                 |             | [optional] |
| **timeout**           | **int**                                                 |             | [optional] |
| **transform**         | [**RouteTransformSettings**](RouteTransformSettings.md) |             | [optional] |
| **user_name**         | **str**                                                 |             | [optional] |

## Example

```python
from notehub_py.models.snowflake_route import SnowflakeRoute

# TODO update the JSON string below
json = "{}"
# create an instance of SnowflakeRoute from a JSON string
snowflake_route_instance = SnowflakeRoute.from_json(json)
# print the JSON string representation of the object
print(SnowflakeRoute.to_json())

# convert the object into a dict
snowflake_route_dict = snowflake_route_instance.to_dict()
# create an instance of SnowflakeRoute from a dict
snowflake_route_from_dict = SnowflakeRoute.from_dict(snowflake_route_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
