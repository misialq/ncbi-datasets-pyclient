# V2OrganismQueryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organism_query** | **str** |  | [optional] 
**taxon_query** | **str** |  | [optional] 
**tax_rank_filter** | [**V2OrganismQueryRequestTaxRankFilter**](V2OrganismQueryRequestTaxRankFilter.md) |  | [optional] 
**taxon_resource_filter** | [**V2OrganismQueryRequestTaxonResourceFilter**](V2OrganismQueryRequestTaxonResourceFilter.md) |  | [optional] 
**exact_match** | **bool** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_organism_query_request import V2OrganismQueryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2OrganismQueryRequest from a JSON string
v2_organism_query_request_instance = V2OrganismQueryRequest.from_json(json)
# print the JSON string representation of the object
print(V2OrganismQueryRequest.to_json())

# convert the object into a dict
v2_organism_query_request_dict = v2_organism_query_request_instance.to_dict()
# create an instance of V2OrganismQueryRequest from a dict
v2_organism_query_request_from_dict = V2OrganismQueryRequest.from_dict(v2_organism_query_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


