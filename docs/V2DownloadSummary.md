# V2DownloadSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**record_count** | **int** |  | [optional] 
**assembly_count** | **int** |  | [optional] 
**resource_updated_on** | **datetime** |  | [optional] 
**hydrated** | [**V2DownloadSummaryHydrated**](V2DownloadSummaryHydrated.md) |  | [optional] 
**dehydrated** | [**V2DownloadSummaryDehydrated**](V2DownloadSummaryDehydrated.md) |  | [optional] 
**errors** | [**List[V2reportsError]**](V2reportsError.md) |  | [optional] 
**messages** | [**List[V2reportsMessage]**](V2reportsMessage.md) |  | [optional] 
**available_files** | [**V2DownloadSummaryAvailableFiles**](V2DownloadSummaryAvailableFiles.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_download_summary import V2DownloadSummary

# TODO update the JSON string below
json = "{}"
# create an instance of V2DownloadSummary from a JSON string
v2_download_summary_instance = V2DownloadSummary.from_json(json)
# print the JSON string representation of the object
print(V2DownloadSummary.to_json())

# convert the object into a dict
v2_download_summary_dict = v2_download_summary_instance.to_dict()
# create an instance of V2DownloadSummary from a dict
v2_download_summary_from_dict = V2DownloadSummary.from_dict(v2_download_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


