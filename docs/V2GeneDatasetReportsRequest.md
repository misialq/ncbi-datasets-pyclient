# V2GeneDatasetReportsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**returned_content** | [**V2GeneDatasetReportsRequestContentType**](V2GeneDatasetReportsRequestContentType.md) |  | [optional] [default to V2GeneDatasetReportsRequestContentType.COMPLETE]
**gene_ids** | **List[int]** |  | [optional] 
**accessions** | **List[str]** |  | [optional] 
**symbols_for_taxon** | [**V2GeneDatasetReportsRequestSymbolsForTaxon**](V2GeneDatasetReportsRequestSymbolsForTaxon.md) |  | [optional] 
**taxon** | **str** |  | [optional] 
**locus_tags** | **List[str]** |  | [optional] 
**table_fields** | **List[str]** |  | [optional] 
**table_format** | **str** |  | [optional] 
**include_tabular_header** | [**V2IncludeTabularHeader**](V2IncludeTabularHeader.md) |  | [optional] [default to V2IncludeTabularHeader.INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
**page_size** | **int** |  | [optional] 
**page_token** | **str** |  | [optional] 
**query** | **str** |  | [optional] 
**types** | [**List[V2GeneType]**](V2GeneType.md) |  | [optional] 
**accession_filter** | **List[str]** |  | [optional] 
**tax_search_subtree** | **bool** |  | [optional] 
**sort** | [**List[V2SortField]**](V2SortField.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_gene_dataset_reports_request import V2GeneDatasetReportsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2GeneDatasetReportsRequest from a JSON string
v2_gene_dataset_reports_request_instance = V2GeneDatasetReportsRequest.from_json(json)
# print the JSON string representation of the object
print(V2GeneDatasetReportsRequest.to_json())

# convert the object into a dict
v2_gene_dataset_reports_request_dict = v2_gene_dataset_reports_request_instance.to_dict()
# create an instance of V2GeneDatasetReportsRequest from a dict
v2_gene_dataset_reports_request_from_dict = V2GeneDatasetReportsRequest.from_dict(v2_gene_dataset_reports_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


