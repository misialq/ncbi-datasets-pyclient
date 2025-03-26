# V2TaxonomyRelatedIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **int** |  | [optional] 
**include_lineage** | **bool** |  | [optional] 
**include_subtree** | **bool** |  | [optional] 
**ranks** | [**List[V2reportsRankType]**](V2reportsRankType.md) |  | [optional] 
**page_size** | **int** |  | [optional] 
**page_token** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_taxonomy_related_id_request import V2TaxonomyRelatedIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2TaxonomyRelatedIdRequest from a JSON string
v2_taxonomy_related_id_request_instance = V2TaxonomyRelatedIdRequest.from_json(json)
# print the JSON string representation of the object
print(V2TaxonomyRelatedIdRequest.to_json())

# convert the object into a dict
v2_taxonomy_related_id_request_dict = v2_taxonomy_related_id_request_instance.to_dict()
# create an instance of V2TaxonomyRelatedIdRequest from a dict
v2_taxonomy_related_id_request_from_dict = V2TaxonomyRelatedIdRequest.from_dict(v2_taxonomy_related_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


