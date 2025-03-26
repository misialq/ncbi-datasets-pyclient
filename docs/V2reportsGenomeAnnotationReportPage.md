# V2reportsGenomeAnnotationReportPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reports** | [**List[V2reportsGenomeAnnotationReportMatch]**](V2reportsGenomeAnnotationReportMatch.md) |  | [optional] 
**messages** | [**List[V2reportsMessage]**](V2reportsMessage.md) |  | [optional] 
**total_count** | **int** |  | [optional] 
**next_page_token** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_genome_annotation_report_page import V2reportsGenomeAnnotationReportPage

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsGenomeAnnotationReportPage from a JSON string
v2reports_genome_annotation_report_page_instance = V2reportsGenomeAnnotationReportPage.from_json(json)
# print the JSON string representation of the object
print(V2reportsGenomeAnnotationReportPage.to_json())

# convert the object into a dict
v2reports_genome_annotation_report_page_dict = v2reports_genome_annotation_report_page_instance.to_dict()
# create an instance of V2reportsGenomeAnnotationReportPage from a dict
v2reports_genome_annotation_report_page_from_dict = V2reportsGenomeAnnotationReportPage.from_dict(v2reports_genome_annotation_report_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


