# V2TaxonomyLinksResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **str** |  | [optional] 
**encyclopedia_of_life** | **str** |  | [optional] 
**global_biodiversity_information_facility** | **str** |  | [optional] 
**inaturalist** | **str** |  | [optional] 
**viralzone** | **str** |  | [optional] 
**wikipedia** | **str** |  | [optional] 
**generic_links** | [**List[V2TaxonomyLinksResponseGenericLink]**](V2TaxonomyLinksResponseGenericLink.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_taxonomy_links_response import V2TaxonomyLinksResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2TaxonomyLinksResponse from a JSON string
v2_taxonomy_links_response_instance = V2TaxonomyLinksResponse.from_json(json)
# print the JSON string representation of the object
print(V2TaxonomyLinksResponse.to_json())

# convert the object into a dict
v2_taxonomy_links_response_dict = v2_taxonomy_links_response_instance.to_dict()
# create an instance of V2TaxonomyLinksResponse from a dict
v2_taxonomy_links_response_from_dict = V2TaxonomyLinksResponse.from_dict(v2_taxonomy_links_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


