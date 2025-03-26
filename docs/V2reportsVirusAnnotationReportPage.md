# V2reportsVirusAnnotationReportPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reports** | [**List[V2reportsVirusAnnotationReport]**](V2reportsVirusAnnotationReport.md) |  | [optional] 
**total_count** | **int** |  | [optional] 
**next_page_token** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_virus_annotation_report_page import V2reportsVirusAnnotationReportPage

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsVirusAnnotationReportPage from a JSON string
v2reports_virus_annotation_report_page_instance = V2reportsVirusAnnotationReportPage.from_json(json)
# print the JSON string representation of the object
print(V2reportsVirusAnnotationReportPage.to_json())

# convert the object into a dict
v2reports_virus_annotation_report_page_dict = v2reports_virus_annotation_report_page_instance.to_dict()
# create an instance of V2reportsVirusAnnotationReportPage from a dict
v2reports_virus_annotation_report_page_from_dict = V2reportsVirusAnnotationReportPage.from_dict(v2reports_virus_annotation_report_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


