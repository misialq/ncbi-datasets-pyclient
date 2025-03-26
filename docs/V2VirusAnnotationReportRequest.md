# V2VirusAnnotationReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | [**V2VirusAnnotationFilter**](V2VirusAnnotationFilter.md) |  | [optional] 
**table_fields** | **List[str]** |  | [optional] 
**table_format** | **str** |  | [optional] 
**page_size** | **int** |  | [optional] 
**page_token** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_virus_annotation_report_request import V2VirusAnnotationReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2VirusAnnotationReportRequest from a JSON string
v2_virus_annotation_report_request_instance = V2VirusAnnotationReportRequest.from_json(json)
# print the JSON string representation of the object
print(V2VirusAnnotationReportRequest.to_json())

# convert the object into a dict
v2_virus_annotation_report_request_dict = v2_virus_annotation_report_request_instance.to_dict()
# create an instance of V2VirusAnnotationReportRequest from a dict
v2_virus_annotation_report_request_from_dict = V2VirusAnnotationReportRequest.from_dict(v2_virus_annotation_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


