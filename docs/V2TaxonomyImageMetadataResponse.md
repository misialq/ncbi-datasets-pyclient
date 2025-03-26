# V2TaxonomyImageMetadataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **str** |  | [optional] 
**src** | **str** |  | [optional] 
**license** | **str** |  | [optional] 
**attribution** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**image_sizes** | [**List[V2ImageSize]**](V2ImageSize.md) |  | [optional] 
**format** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_taxonomy_image_metadata_response import V2TaxonomyImageMetadataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2TaxonomyImageMetadataResponse from a JSON string
v2_taxonomy_image_metadata_response_instance = V2TaxonomyImageMetadataResponse.from_json(json)
# print the JSON string representation of the object
print(V2TaxonomyImageMetadataResponse.to_json())

# convert the object into a dict
v2_taxonomy_image_metadata_response_dict = v2_taxonomy_image_metadata_response_instance.to_dict()
# create an instance of V2TaxonomyImageMetadataResponse from a dict
v2_taxonomy_image_metadata_response_from_dict = V2TaxonomyImageMetadataResponse.from_dict(v2_taxonomy_image_metadata_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


