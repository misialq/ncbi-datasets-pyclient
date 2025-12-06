# V2TaxonomyMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxons** | **List[str]** |  | [optional] 
**returned_content** | [**V2TaxonomyMetadataRequestContentType**](V2TaxonomyMetadataRequestContentType.md) |  | [optional] [default to V2TaxonomyMetadataRequestContentType.COMPLETE]
**page_size** | **int** |  | [optional] 
**include_tabular_header** | [**V2IncludeTabularHeader**](V2IncludeTabularHeader.md) |  | [optional] [default to V2IncludeTabularHeader.INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
**page_token** | **str** |  | [optional] 
**table_format** | [**V2TaxonomyMetadataRequestTableFormat**](V2TaxonomyMetadataRequestTableFormat.md) |  | [optional] [default to V2TaxonomyMetadataRequestTableFormat.SUMMARY]
**children** | **bool** |  | [optional] 
**ranks** | [**List[V2reportsRankType]**](V2reportsRankType.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_taxonomy_metadata_request import V2TaxonomyMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2TaxonomyMetadataRequest from a JSON string
v2_taxonomy_metadata_request_instance = V2TaxonomyMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(V2TaxonomyMetadataRequest.to_json())

# convert the object into a dict
v2_taxonomy_metadata_request_dict = v2_taxonomy_metadata_request_instance.to_dict()
# create an instance of V2TaxonomyMetadataRequest from a dict
v2_taxonomy_metadata_request_from_dict = V2TaxonomyMetadataRequest.from_dict(v2_taxonomy_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


