# V2AssemblyDatasetReportsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxons** | **List[str]** |  | [optional] 
**bioprojects** | **List[str]** |  | [optional] 
**biosample_ids** | **List[str]** |  | [optional] 
**assembly_names** | **List[str]** |  | [optional] 
**wgs_accessions** | **List[str]** |  | [optional] 
**accessions** | **List[str]** |  | [optional] 
**filters** | [**V2AssemblyDatasetDescriptorsFilter**](V2AssemblyDatasetDescriptorsFilter.md) |  | [optional] 
**tax_exact_match** | **bool** |  | [optional] 
**chromosomes** | **List[str]** |  | [optional] 
**table_fields** | **List[str]** |  | [optional] 
**returned_content** | [**V2AssemblyDatasetReportsRequestContentType**](V2AssemblyDatasetReportsRequestContentType.md) |  | [optional] [default to V2AssemblyDatasetReportsRequestContentType.COMPLETE]
**page_size** | **int** |  | [optional] 
**page_token** | **str** |  | [optional] 
**sort** | [**List[V2SortField]**](V2SortField.md) |  | [optional] 
**include_tabular_header** | [**V2IncludeTabularHeader**](V2IncludeTabularHeader.md) |  | [optional] [default to V2IncludeTabularHeader.INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
**table_format** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_assembly_dataset_reports_request import V2AssemblyDatasetReportsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssemblyDatasetReportsRequest from a JSON string
v2_assembly_dataset_reports_request_instance = V2AssemblyDatasetReportsRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssemblyDatasetReportsRequest.to_json())

# convert the object into a dict
v2_assembly_dataset_reports_request_dict = v2_assembly_dataset_reports_request_instance.to_dict()
# create an instance of V2AssemblyDatasetReportsRequest from a dict
v2_assembly_dataset_reports_request_from_dict = V2AssemblyDatasetReportsRequest.from_dict(v2_assembly_dataset_reports_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


