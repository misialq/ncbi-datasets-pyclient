# V2reportsSequenceFeatureTreeNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_id** | **int** |  | [optional] 
**parent_feature_id** | **int** |  | [optional] 
**has_children** | **bool** |  | [optional] 
**accession** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_feature_tree_node import V2reportsSequenceFeatureTreeNode

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceFeatureTreeNode from a JSON string
v2reports_sequence_feature_tree_node_instance = V2reportsSequenceFeatureTreeNode.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceFeatureTreeNode.to_json())

# convert the object into a dict
v2reports_sequence_feature_tree_node_dict = v2reports_sequence_feature_tree_node_instance.to_dict()
# create an instance of V2reportsSequenceFeatureTreeNode from a dict
v2reports_sequence_feature_tree_node_from_dict = V2reportsSequenceFeatureTreeNode.from_dict(v2reports_sequence_feature_tree_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


