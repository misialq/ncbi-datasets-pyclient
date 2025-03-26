# V2SequenceReportPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reports** | [**List[V2reportsSequenceInfo]**](V2reportsSequenceInfo.md) |  | [optional] 
**total_count** | **int** |  | [optional] 
**next_page_token** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_sequence_report_page import V2SequenceReportPage

# TODO update the JSON string below
json = "{}"
# create an instance of V2SequenceReportPage from a JSON string
v2_sequence_report_page_instance = V2SequenceReportPage.from_json(json)
# print the JSON string representation of the object
print(V2SequenceReportPage.to_json())

# convert the object into a dict
v2_sequence_report_page_dict = v2_sequence_report_page_instance.to_dict()
# create an instance of V2SequenceReportPage from a dict
v2_sequence_report_page_from_dict = V2SequenceReportPage.from_dict(v2_sequence_report_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


