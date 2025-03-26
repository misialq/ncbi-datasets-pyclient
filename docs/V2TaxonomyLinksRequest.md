# V2TaxonomyLinksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxon** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_taxonomy_links_request import V2TaxonomyLinksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2TaxonomyLinksRequest from a JSON string
v2_taxonomy_links_request_instance = V2TaxonomyLinksRequest.from_json(json)
# print the JSON string representation of the object
print(V2TaxonomyLinksRequest.to_json())

# convert the object into a dict
v2_taxonomy_links_request_dict = v2_taxonomy_links_request_instance.to_dict()
# create an instance of V2TaxonomyLinksRequest from a dict
v2_taxonomy_links_request_from_dict = V2TaxonomyLinksRequest.from_dict(v2_taxonomy_links_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


