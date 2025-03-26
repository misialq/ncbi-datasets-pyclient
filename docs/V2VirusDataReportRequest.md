# V2VirusDataReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**V2VirusDatasetFilter**](V2VirusDatasetFilter.md) |  | [optional] 
**returned_content** | [**V2VirusDataReportRequestContentType**](V2VirusDataReportRequestContentType.md) |  | [optional] 
**table_fields** | **List[str]** |  | [optional] 
**table_format** | **str** |  | [optional] 
**page_size** | **int** |  | [optional] 
**page_token** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_virus_data_report_request import V2VirusDataReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2VirusDataReportRequest from a JSON string
v2_virus_data_report_request_instance = V2VirusDataReportRequest.from_json(json)
# print the JSON string representation of the object
print(V2VirusDataReportRequest.to_json())

# convert the object into a dict
v2_virus_data_report_request_dict = v2_virus_data_report_request_instance.to_dict()
# create an instance of V2VirusDataReportRequest from a dict
v2_virus_data_report_request_from_dict = V2VirusDataReportRequest.from_dict(v2_virus_data_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


