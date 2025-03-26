# V2TaxonomyMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[V2reportsMessage]**](V2reportsMessage.md) |  | [optional] 
**taxonomy_nodes** | [**List[V2TaxonomyMatch]**](V2TaxonomyMatch.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_taxonomy_metadata_response import V2TaxonomyMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2TaxonomyMetadataResponse from a JSON string
v2_taxonomy_metadata_response_instance = V2TaxonomyMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(V2TaxonomyMetadataResponse.to_json())

# convert the object into a dict
v2_taxonomy_metadata_response_dict = v2_taxonomy_metadata_response_instance.to_dict()
# create an instance of V2TaxonomyMetadataResponse from a dict
v2_taxonomy_metadata_response_from_dict = V2TaxonomyMetadataResponse.from_dict(v2_taxonomy_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


