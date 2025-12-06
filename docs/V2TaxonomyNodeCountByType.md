# V2TaxonomyNodeCountByType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**V2reportsCountType**](V2reportsCountType.md) |  | [optional] [default to V2reportsCountType.COUNT_TYPE_UNSPECIFIED]
**count** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_taxonomy_node_count_by_type import V2TaxonomyNodeCountByType

# TODO update the JSON string below
json = "{}"
# create an instance of V2TaxonomyNodeCountByType from a JSON string
v2_taxonomy_node_count_by_type_instance = V2TaxonomyNodeCountByType.from_json(json)
# print the JSON string representation of the object
print(V2TaxonomyNodeCountByType.to_json())

# convert the object into a dict
v2_taxonomy_node_count_by_type_dict = v2_taxonomy_node_count_by_type_instance.to_dict()
# create an instance of V2TaxonomyNodeCountByType from a dict
v2_taxonomy_node_count_by_type_from_dict = V2TaxonomyNodeCountByType.from_dict(v2_taxonomy_node_count_by_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


