# V2TaxonomyImageMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxon** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_taxonomy_image_metadata_request import V2TaxonomyImageMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2TaxonomyImageMetadataRequest from a JSON string
v2_taxonomy_image_metadata_request_instance = V2TaxonomyImageMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(V2TaxonomyImageMetadataRequest.to_json())

# convert the object into a dict
v2_taxonomy_image_metadata_request_dict = v2_taxonomy_image_metadata_request_instance.to_dict()
# create an instance of V2TaxonomyImageMetadataRequest from a dict
v2_taxonomy_image_metadata_request_from_dict = V2TaxonomyImageMetadataRequest.from_dict(v2_taxonomy_image_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


