# V2reportsSequenceDataReportPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reports** | [**List[V2reportsSequenceDataReport]**](V2reportsSequenceDataReport.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_data_report_page import V2reportsSequenceDataReportPage

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceDataReportPage from a JSON string
v2reports_sequence_data_report_page_instance = V2reportsSequenceDataReportPage.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceDataReportPage.to_json())

# convert the object into a dict
v2reports_sequence_data_report_page_dict = v2reports_sequence_data_report_page_instance.to_dict()
# create an instance of V2reportsSequenceDataReportPage from a dict
v2reports_sequence_data_report_page_from_dict = V2reportsSequenceDataReportPage.from_dict(v2reports_sequence_data_report_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


