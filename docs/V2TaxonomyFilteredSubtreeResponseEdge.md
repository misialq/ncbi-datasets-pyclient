# V2TaxonomyFilteredSubtreeResponseEdge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visible_children** | **List[int]** |  | [optional] 
**children_status** | [**V2TaxonomyFilteredSubtreeResponseEdgeChildStatus**](V2TaxonomyFilteredSubtreeResponseEdgeChildStatus.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_taxonomy_filtered_subtree_response_edge import V2TaxonomyFilteredSubtreeResponseEdge

# TODO update the JSON string below
json = "{}"
# create an instance of V2TaxonomyFilteredSubtreeResponseEdge from a JSON string
v2_taxonomy_filtered_subtree_response_edge_instance = V2TaxonomyFilteredSubtreeResponseEdge.from_json(json)
# print the JSON string representation of the object
print(V2TaxonomyFilteredSubtreeResponseEdge.to_json())

# convert the object into a dict
v2_taxonomy_filtered_subtree_response_edge_dict = v2_taxonomy_filtered_subtree_response_edge_instance.to_dict()
# create an instance of V2TaxonomyFilteredSubtreeResponseEdge from a dict
v2_taxonomy_filtered_subtree_response_edge_from_dict = V2TaxonomyFilteredSubtreeResponseEdge.from_dict(v2_taxonomy_filtered_subtree_response_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


