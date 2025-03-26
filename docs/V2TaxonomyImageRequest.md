# V2TaxonomyImageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxon** | **str** |  | [optional] 
**image_size** | [**V2ImageSize**](V2ImageSize.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_taxonomy_image_request import V2TaxonomyImageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2TaxonomyImageRequest from a JSON string
v2_taxonomy_image_request_instance = V2TaxonomyImageRequest.from_json(json)
# print the JSON string representation of the object
print(V2TaxonomyImageRequest.to_json())

# convert the object into a dict
v2_taxonomy_image_request_dict = v2_taxonomy_image_request_instance.to_dict()
# create an instance of V2TaxonomyImageRequest from a dict
v2_taxonomy_image_request_from_dict = V2TaxonomyImageRequest.from_dict(v2_taxonomy_image_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


