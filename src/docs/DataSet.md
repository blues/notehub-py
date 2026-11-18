# DataSet

## Properties

| Name               | Type                                                  | Description                                                                                                                                                                                                                                                          | Notes                 |
| ------------------ | ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| **fields**         | [**List[DataSetField]**](DataSetField.md)             |                                                                                                                                                                                                                                                                      | [optional]            |
| **is_optimized**   | **bool**                                              | True once the dataset&#39;s underlying table has been deduplicated/optimized. Server-populated; ignored on input.                                                                                                                                                    | [optional] [readonly] |
| **is_ready**       | **bool**                                              | True once the dataset has been fully loaded from the repository&#39;s archive after backfill completed. Server-populated; ignored on input.                                                                                                                          | [optional] [readonly] |
| **lambda_name**    | **str**                                               | Name of the Lambda function deployed for a Python dataset. Derived from the repository and dataset name; set when the function is deployed.                                                                                                                          | [optional] [readonly] |
| **lambda_version** | **str**                                               | Published Lambda version this dataset is pinned to. A reload invokes this version rather than the latest, so republishing a projection never changes how a replay projects.                                                                                          | [optional] [readonly] |
| **lat**            | **str**                                               | JSONata expression resulting in the latitude field                                                                                                                                                                                                                   | [optional]            |
| **location**       | **bool**                                              | Whether the dataset has a location column, taken from each row&#39;s \&quot;lat\&quot; and \&quot;lon\&quot; keys. For Python datasets only; a JSONata dataset declares a location column by setting both lat and lon.                                               | [optional]            |
| **lon**            | **str**                                               | JSONata expression resulting in the Longitude field                                                                                                                                                                                                                  | [optional]            |
| **name**           | **str**                                               | The name of the data set                                                                                                                                                                                                                                             | [optional]            |
| **notefiles**      | **List[str]**                                         | If non-empty, only events from these notefiles populate the dataset. Empty or omitted means all notefiles.                                                                                                                                                           | [optional]            |
| **python**         | **str**                                               | Optional Python projection: &#x60;def rows(record: dict[str, Any]) -&gt; list[dict[str, Any]]&#x60;, called once per &#x60;RepositoryRecord&#x60;. Return rows in a fixed order, or a reload duplicates them. Can&#39;t be combined with JSONata fields. Max 64 KiB. | [optional]            |
| **reload**         | [**DatasetReloadProgress**](DatasetReloadProgress.md) |                                                                                                                                                                                                                                                                      | [optional]            |
| **rows**           | **str**                                               | Optional JSONata expression turning one &#x60;RepositoryRecord&#x60; into row objects whose keys are the columns. When set, fields, &#x60;time&#x60;, &#x60;lat&#x60; and &#x60;lon&#x60; name row keys instead.                                                     | [optional]            |
| **time**           | **str**                                               | JSONata expression for the row&#39;s time. Required without &#x60;rows&#x60;; with &#x60;rows&#x60;, defaults to the row&#39;s &#x60;time&#x60; key.                                                                                                                 | [optional]            |

## Example

```python
from notehub_py.models.data_set import DataSet

# TODO update the JSON string below
json = "{}"
# create an instance of DataSet from a JSON string
data_set_instance = DataSet.from_json(json)
# print the JSON string representation of the object
print(DataSet.to_json())

# convert the object into a dict
data_set_dict = data_set_instance.to_dict()
# create an instance of DataSet from a dict
data_set_from_dict = DataSet.from_dict(data_set_dict)
```

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
