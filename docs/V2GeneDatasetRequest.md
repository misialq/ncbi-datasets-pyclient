# V2GeneDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_ids** | **List[int]** |  | [optional] 
**include_annotation_type** | [**List[V2Fasta]**](V2Fasta.md) |  | [optional] 
**returned_content** | [**V2GeneDatasetRequestContentType**](V2GeneDatasetRequestContentType.md) |  | [optional] [default to V2GeneDatasetRequestContentType.COMPLETE]
**fasta_filter** | **List[str]** |  | [optional] 
**accession_filter** | **List[str]** |  | [optional] 
**aux_report** | [**List[V2GeneDatasetRequestGeneDatasetReportType]**](V2GeneDatasetRequestGeneDatasetReportType.md) |  | [optional] 
**tabular_reports** | [**List[V2GeneDatasetRequestGeneDatasetReportType]**](V2GeneDatasetRequestGeneDatasetReportType.md) |  | [optional] 
**table_fields** | **List[str]** |  | [optional] 
**table_report_type** | [**V2GeneDatasetRequestGeneDatasetReportType**](V2GeneDatasetRequestGeneDatasetReportType.md) |  | [optional] [default to V2GeneDatasetRequestGeneDatasetReportType.DATASET_REPORT]

## Example

```python
from ncbi.datasets.openapi.models.v2_gene_dataset_request import V2GeneDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2GeneDatasetRequest from a JSON string
v2_gene_dataset_request_instance = V2GeneDatasetRequest.from_json(json)
# print the JSON string representation of the object
print(V2GeneDatasetRequest.to_json())

# convert the object into a dict
v2_gene_dataset_request_dict = v2_gene_dataset_request_instance.to_dict()
# create an instance of V2GeneDatasetRequest from a dict
v2_gene_dataset_request_from_dict = V2GeneDatasetRequest.from_dict(v2_gene_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


