# V2TaxonomyFilteredSubtreeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_nodes** | **List[int]** |  | [optional] 
**edges** | [**V2TaxonomyFilteredSubtreeResponseEdgesEntry**](V2TaxonomyFilteredSubtreeResponseEdgesEntry.md) |  | [optional] 
**warnings** | [**List[V2reportsWarning]**](V2reportsWarning.md) |  | [optional] 
**errors** | [**List[V2reportsError]**](V2reportsError.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_taxonomy_filtered_subtree_response import V2TaxonomyFilteredSubtreeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2TaxonomyFilteredSubtreeResponse from a JSON string
v2_taxonomy_filtered_subtree_response_instance = V2TaxonomyFilteredSubtreeResponse.from_json(json)
# print the JSON string representation of the object
print(V2TaxonomyFilteredSubtreeResponse.to_json())

# convert the object into a dict
v2_taxonomy_filtered_subtree_response_dict = v2_taxonomy_filtered_subtree_response_instance.to_dict()
# create an instance of V2TaxonomyFilteredSubtreeResponse from a dict
v2_taxonomy_filtered_subtree_response_from_dict = V2TaxonomyFilteredSubtreeResponse.from_dict(v2_taxonomy_filtered_subtree_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


