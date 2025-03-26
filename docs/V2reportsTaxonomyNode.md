# V2reportsTaxonomyNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **int** |  | [optional] 
**rank** | [**V2reportsRankType**](V2reportsRankType.md) |  | [optional] 
**current_scientific_name** | [**V2reportsNameAndAuthority**](V2reportsNameAndAuthority.md) |  | [optional] 
**basionym** | [**V2reportsNameAndAuthority**](V2reportsNameAndAuthority.md) |  | [optional] 
**curator_common_name** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 
**has_type_material** | **bool** |  | [optional] 
**classification** | [**V2reportsClassification**](V2reportsClassification.md) |  | [optional] 
**parents** | **List[int]** |  | [optional] 
**children** | **List[int]** |  | [optional] 
**counts** | [**List[V2reportsTaxonomyNodeCountByType]**](V2reportsTaxonomyNodeCountByType.md) |  | [optional] 
**genomic_moltype** | **str** |  | [optional] 
**current_scientific_name_is_formal** | **bool** |  | [optional] 
**secondary_tax_ids** | **List[int]** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_taxonomy_node import V2reportsTaxonomyNode

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsTaxonomyNode from a JSON string
v2reports_taxonomy_node_instance = V2reportsTaxonomyNode.from_json(json)
# print the JSON string representation of the object
print(V2reportsTaxonomyNode.to_json())

# convert the object into a dict
v2reports_taxonomy_node_dict = v2reports_taxonomy_node_instance.to_dict()
# create an instance of V2reportsTaxonomyNode from a dict
v2reports_taxonomy_node_from_dict = V2reportsTaxonomyNode.from_dict(v2reports_taxonomy_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


