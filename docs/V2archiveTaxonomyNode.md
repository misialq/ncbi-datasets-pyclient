# V2archiveTaxonomyNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **int** |  | [optional] 
**current_scientific_name** | [**V2reportsNameAndAuthority**](V2reportsNameAndAuthority.md) |  | [optional] 
**basionym** | [**V2reportsNameAndAuthority**](V2reportsNameAndAuthority.md) |  | [optional] 
**curator_common_name** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**classification** | [**V2reportsClassification**](V2reportsClassification.md) |  | [optional] 
**modifiers** | [**List[V2archiveModifier]**](V2archiveModifier.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2archive_taxonomy_node import V2archiveTaxonomyNode

# TODO update the JSON string below
json = "{}"
# create an instance of V2archiveTaxonomyNode from a JSON string
v2archive_taxonomy_node_instance = V2archiveTaxonomyNode.from_json(json)
# print the JSON string representation of the object
print(V2archiveTaxonomyNode.to_json())

# convert the object into a dict
v2archive_taxonomy_node_dict = v2archive_taxonomy_node_instance.to_dict()
# create an instance of V2archiveTaxonomyNode from a dict
v2archive_taxonomy_node_from_dict = V2archiveTaxonomyNode.from_dict(v2archive_taxonomy_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


