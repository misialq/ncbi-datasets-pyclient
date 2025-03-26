# V2OrganelleMetadataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxons** | **List[str]** |  | [optional] 
**accessions** | **List[str]** |  | [optional] 
**organelle_types** | [**List[V2reportsOrganelleType]**](V2reportsOrganelleType.md) |  | [optional] 
**first_release_date** | **datetime** |  | [optional] 
**last_release_date** | **datetime** |  | [optional] 
**tax_exact_match** | **bool** |  | [optional] 
**sort** | [**List[V2OrganelleSort]**](V2OrganelleSort.md) |  | [optional] 
**returned_content** | [**V2OrganelleMetadataRequestContentType**](V2OrganelleMetadataRequestContentType.md) |  | [optional] 
**page_size** | **int** |  | [optional] 
**page_token** | **str** |  | [optional] 
**table_format** | [**V2OrganelleMetadataRequestOrganelleTableFormat**](V2OrganelleMetadataRequestOrganelleTableFormat.md) |  | [optional] 
**include_tabular_header** | [**V2IncludeTabularHeader**](V2IncludeTabularHeader.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_organelle_metadata_request import V2OrganelleMetadataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2OrganelleMetadataRequest from a JSON string
v2_organelle_metadata_request_instance = V2OrganelleMetadataRequest.from_json(json)
# print the JSON string representation of the object
print(V2OrganelleMetadataRequest.to_json())

# convert the object into a dict
v2_organelle_metadata_request_dict = v2_organelle_metadata_request_instance.to_dict()
# create an instance of V2OrganelleMetadataRequest from a dict
v2_organelle_metadata_request_from_dict = V2OrganelleMetadataRequest.from_dict(v2_organelle_metadata_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


