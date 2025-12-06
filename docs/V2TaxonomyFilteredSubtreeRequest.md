# V2TaxonomyFilteredSubtreeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxons** | **List[str]** |  | [optional] 
**specified_limit** | **bool** |  | [optional] 
**rank_limits** | [**List[V2reportsRankType]**](V2reportsRankType.md) |  | [optional] 
**include_incertae_sedis** | **bool** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_taxonomy_filtered_subtree_request import V2TaxonomyFilteredSubtreeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2TaxonomyFilteredSubtreeRequest from a JSON string
v2_taxonomy_filtered_subtree_request_instance = V2TaxonomyFilteredSubtreeRequest.from_json(json)
# print the JSON string representation of the object
print(V2TaxonomyFilteredSubtreeRequest.to_json())

# convert the object into a dict
v2_taxonomy_filtered_subtree_request_dict = v2_taxonomy_filtered_subtree_request_instance.to_dict()
# create an instance of V2TaxonomyFilteredSubtreeRequest from a dict
v2_taxonomy_filtered_subtree_request_from_dict = V2TaxonomyFilteredSubtreeRequest.from_dict(v2_taxonomy_filtered_subtree_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


