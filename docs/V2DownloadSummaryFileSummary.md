# V2DownloadSummaryFileSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_count** | **int** |  | [optional] 
**size_mb** | **float** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_download_summary_file_summary import V2DownloadSummaryFileSummary

# TODO update the JSON string below
json = "{}"
# create an instance of V2DownloadSummaryFileSummary from a JSON string
v2_download_summary_file_summary_instance = V2DownloadSummaryFileSummary.from_json(json)
# print the JSON string representation of the object
print(V2DownloadSummaryFileSummary.to_json())

# convert the object into a dict
v2_download_summary_file_summary_dict = v2_download_summary_file_summary_instance.to_dict()
# create an instance of V2DownloadSummaryFileSummary from a dict
v2_download_summary_file_summary_from_dict = V2DownloadSummaryFileSummary.from_dict(v2_download_summary_file_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


