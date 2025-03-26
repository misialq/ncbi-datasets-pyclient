# V2TaxonomyNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **int** |  | [optional] 
**organism_name** | **str** |  | [optional] 
**common_name** | **str** |  | [optional] 
**genbank_common_name** | **str** |  | [optional] 
**acronyms** | **List[str]** |  | [optional] 
**genbank_acronym** | **str** |  | [optional] 
**blast_name** | **str** |  | [optional] 
**lineage** | **List[int]** |  | [optional] 
**children** | **List[int]** |  | [optional] 
**descendent_with_described_species_names_count** | **int** |  | [optional] 
**rank** | [**V2reportsRankType**](V2reportsRankType.md) |  | [optional] 
**has_described_species_name** | **bool** |  | [optional] 
**counts** | [**List[V2TaxonomyNodeCountByType]**](V2TaxonomyNodeCountByType.md) |  | [optional] 
**min_ord** | **int** |  | [optional] 
**max_ord** | **int** |  | [optional] 
**extinct** | **bool** |  | [optional] 
**genomic_moltype** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_taxonomy_node import V2TaxonomyNode

# TODO update the JSON string below
json = "{}"
# create an instance of V2TaxonomyNode from a JSON string
v2_taxonomy_node_instance = V2TaxonomyNode.from_json(json)
# print the JSON string representation of the object
print(V2TaxonomyNode.to_json())

# convert the object into a dict
v2_taxonomy_node_dict = v2_taxonomy_node_instance.to_dict()
# create an instance of V2TaxonomyNode from a dict
v2_taxonomy_node_from_dict = V2TaxonomyNode.from_dict(v2_taxonomy_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


