# NotehubRoute

Route resource as stored/returned by the server.

## Properties

| Name                   | Type                                                    | Description               | Notes                         |
| ---------------------- | ------------------------------------------------------- | ------------------------- | ----------------------------- |
| **aws**                | [**AwsRoute**](AwsRoute.md)                             |                           | [optional]                    |
| **azure**              | [**AzureRoute**](AzureRoute.md)                         |                           | [optional]                    |
| **blynk**              | [**BlynkRoute**](BlynkRoute.md)                         |                           | [optional]                    |
| **datacake**           | [**DatacakeRoute**](DatacakeRoute.md)                   |                           | [optional]                    |
| **disabled**           | **bool**                                                |                           | [optional] [default to False] |
| **google**             | [**GoogleRoute**](GoogleRoute.md)                       |                           | [optional]                    |
| **http**               | [**HttpRoute**](HttpRoute.md)                           |                           | [optional]                    |
| **label**              | **str**                                                 |                           | [optional]                    |
| **modified**           | **datetime**                                            |                           | [optional] [readonly]         |
| **mqtt**               | [**MqttRoute**](MqttRoute.md)                           |                           | [optional]                    |
| **proxy**              | [**ProxyRoute**](ProxyRoute.md)                         |                           | [optional]                    |
| **qubitro**            | [**QubitroRoute**](QubitroRoute.md)                     |                           | [optional]                    |
| **radnote**            | [**RadRoute**](RadRoute.md)                             |                           | [optional]                    |
| **s3archive**          | [**S3ArchiveRoute**](S3ArchiveRoute.md)                 |                           | [optional]                    |
| **slack**              | [**SlackRoute**](SlackRoute.md)                         |                           | [optional]                    |
| **snowflake**          | [**SnowflakeRoute**](SnowflakeRoute.md)                 |                           | [optional]                    |
| **snowpipe_streaming** | [**SnowpipeStreamingRoute**](SnowpipeStreamingRoute.md) |                           | [optional]                    |
| **thingworx**          | [**ThingworxRoute**](ThingworxRoute.md)                 |                           | [optional]                    |
| **twilio**             | [**TwilioRoute**](TwilioRoute.md)                       |                           | [optional]                    |
| **type**               | **str**                                                 | Mirrors hublib.RouteType. | [optional]                    |
| **uid**                | **str**                                                 |                           | [optional] [readonly]         |

## Example

```python
from notehub_py.models.notehub_route import NotehubRoute

# TODO update the JSON string below
json = "{}"
# create an instance of NotehubRoute from a JSON string
notehub_route_instance = NotehubRoute.from_json(json)
# print the JSON string representation of the object
print(NotehubRoute.to_json())

# convert the object into a dict
notehub_route_dict = notehub_route_instance.to_dict()
# create an instance of NotehubRoute from a dict
notehub_route_from_dict = NotehubRoute.from_dict(notehub_route_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
