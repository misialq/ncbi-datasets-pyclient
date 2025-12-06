# V2reportsAssemblyDataReportPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reports** | [**List[V2reportsAssemblyDataReport]**](V2reportsAssemblyDataReport.md) |  | [optional] 
**content_type** | [**V2reportsContentType**](V2reportsContentType.md) |  | [optional] [default to V2reportsContentType.COMPLETE]
**total_count** | **int** |  | [optional] 
**next_page_token** | **str** |  | [optional] 
**messages** | [**List[V2reportsMessage]**](V2reportsMessage.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_assembly_data_report_page import V2reportsAssemblyDataReportPage

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsAssemblyDataReportPage from a JSON string
v2reports_assembly_data_report_page_instance = V2reportsAssemblyDataReportPage.from_json(json)
# print the JSON string representation of the object
print(V2reportsAssemblyDataReportPage.to_json())

# convert the object into a dict
v2reports_assembly_data_report_page_dict = v2reports_assembly_data_report_page_instance.to_dict()
# create an instance of V2reportsAssemblyDataReportPage from a dict
v2reports_assembly_data_report_page_from_dict = V2reportsAssemblyDataReportPage.from_dict(v2reports_assembly_data_report_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


