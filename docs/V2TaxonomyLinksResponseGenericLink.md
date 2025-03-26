# V2TaxonomyLinksResponseGenericLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**link_name** | **str** |  | [optional] 
**link_url** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_taxonomy_links_response_generic_link import V2TaxonomyLinksResponseGenericLink

# TODO update the JSON string below
json = "{}"
# create an instance of V2TaxonomyLinksResponseGenericLink from a JSON string
v2_taxonomy_links_response_generic_link_instance = V2TaxonomyLinksResponseGenericLink.from_json(json)
# print the JSON string representation of the object
print(V2TaxonomyLinksResponseGenericLink.to_json())

# convert the object into a dict
v2_taxonomy_links_response_generic_link_dict = v2_taxonomy_links_response_generic_link_instance.to_dict()
# create an instance of V2TaxonomyLinksResponseGenericLink from a dict
v2_taxonomy_links_response_generic_link_from_dict = V2TaxonomyLinksResponseGenericLink.from_dict(v2_taxonomy_links_response_generic_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


