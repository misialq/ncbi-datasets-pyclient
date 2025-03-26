# V2DownloadSummaryAvailableFiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_genomic_fasta** | [**V2DownloadSummaryFileSummary**](V2DownloadSummaryFileSummary.md) |  | [optional] 
**genome_gff** | [**V2DownloadSummaryFileSummary**](V2DownloadSummaryFileSummary.md) |  | [optional] 
**genome_gbff** | [**V2DownloadSummaryFileSummary**](V2DownloadSummaryFileSummary.md) |  | [optional] 
**rna_fasta** | [**V2DownloadSummaryFileSummary**](V2DownloadSummaryFileSummary.md) |  | [optional] 
**prot_fasta** | [**V2DownloadSummaryFileSummary**](V2DownloadSummaryFileSummary.md) |  | [optional] 
**genome_gtf** | [**V2DownloadSummaryFileSummary**](V2DownloadSummaryFileSummary.md) |  | [optional] 
**cds_fasta** | [**V2DownloadSummaryFileSummary**](V2DownloadSummaryFileSummary.md) |  | [optional] 
**sequence_report** | [**V2DownloadSummaryFileSummary**](V2DownloadSummaryFileSummary.md) |  | [optional] 
**annotation_report** | [**V2DownloadSummaryFileSummary**](V2DownloadSummaryFileSummary.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_download_summary_available_files import V2DownloadSummaryAvailableFiles

# TODO update the JSON string below
json = "{}"
# create an instance of V2DownloadSummaryAvailableFiles from a JSON string
v2_download_summary_available_files_instance = V2DownloadSummaryAvailableFiles.from_json(json)
# print the JSON string representation of the object
print(V2DownloadSummaryAvailableFiles.to_json())

# convert the object into a dict
v2_download_summary_available_files_dict = v2_download_summary_available_files_instance.to_dict()
# create an instance of V2DownloadSummaryAvailableFiles from a dict
v2_download_summary_available_files_from_dict = V2DownloadSummaryAvailableFiles.from_dict(v2_download_summary_available_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


