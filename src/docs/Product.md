# Product

## Properties

| Name                           | Type          | Description                                                                                                                   | Notes      |
| ------------------------------ | ------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **auto_provision_fleets**      | **List[str]** | FleetUIDs that devices are added to when first provisioned with this ProductUID.                                              | [optional] |
| **disable_devices_by_default** | **bool**      | If &#x60;true&#x60;, devices provisioned with this ProductUID start out disabled.                                             |
| **label**                      | **str**       | Product name shown in Notehub.                                                                                                |
| **uid**                        | **str**       | ProductUID, e.g. &#x60;com.blues.bridge:sensors&#x60;. &#x60;GetProducts&#x60; returns it with a &#x60;product:&#x60; prefix. |

## Example

```python
from notehub_py.models.product import Product

# TODO update the JSON string below
json = "{}"
# create an instance of Product from a JSON string
product_instance = Product.from_json(json)
# print the JSON string representation of the object
print(Product.to_json())

# convert the object into a dict
product_dict = product_instance.to_dict()
# create an instance of Product from a dict
product_from_dict = Product.from_dict(product_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
