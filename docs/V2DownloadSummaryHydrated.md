# V2DownloadSummaryHydrated


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**estimated_file_size_mb** | **int** |  | [optional] 
**url** | **str** |  | [optional] 
**cli_download_command_line** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_download_summary_hydrated import V2DownloadSummaryHydrated

# TODO update the JSON string below
json = "{}"
# create an instance of V2DownloadSummaryHydrated from a JSON string
v2_download_summary_hydrated_instance = V2DownloadSummaryHydrated.from_json(json)
# print the JSON string representation of the object
print(V2DownloadSummaryHydrated.to_json())

# convert the object into a dict
v2_download_summary_hydrated_dict = v2_download_summary_hydrated_instance.to_dict()
# create an instance of V2DownloadSummaryHydrated from a dict
v2_download_summary_hydrated_from_dict = V2DownloadSummaryHydrated.from_dict(v2_download_summary_hydrated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


