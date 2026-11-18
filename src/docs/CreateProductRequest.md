# CreateProductRequest

## Properties

| Name                           | Type          | Description                                                                                                                                                  | Notes      |
| ------------------------------ | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| **auto_provision_fleets**      | **List[str]** | FleetUIDs that devices are added to when first provisioned with this ProductUID.                                                                             | [optional] |
| **disable_devices_by_default** | **bool**      | If &#x60;true&#x60;, devices provisioned with this ProductUID start out disabled.                                                                            | [optional] |
| **label**                      | **str**       | Product name shown in Notehub.                                                                                                                               |
| **product_uid**                | **str**       | Suffix of the new ProductUID. Must start with a lowercase letter and contain only lowercase letters, digits, &#x60;.&#x60;, &#x60;\_&#x60; or &#x60;-&#x60;. |

## Example

```python
from notehub_py.models.create_product_request import CreateProductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProductRequest from a JSON string
create_product_request_instance = CreateProductRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProductRequest.to_json())

# convert the object into a dict
create_product_request_dict = create_product_request_instance.to_dict()
# create an instance of CreateProductRequest from a dict
create_product_request_from_dict = CreateProductRequest.from_dict(
    create_product_request_dict
)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
