# V2reportsVirusAnnotationReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**isolate_name** | **str** |  | [optional] 
**genes** | [**List[V2reportsVirusGene]**](V2reportsVirusGene.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_virus_annotation_report import V2reportsVirusAnnotationReport

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsVirusAnnotationReport from a JSON string
v2reports_virus_annotation_report_instance = V2reportsVirusAnnotationReport.from_json(json)
# print the JSON string representation of the object
print(V2reportsVirusAnnotationReport.to_json())

# convert the object into a dict
v2reports_virus_annotation_report_dict = v2reports_virus_annotation_report_instance.to_dict()
# create an instance of V2reportsVirusAnnotationReport from a dict
v2reports_virus_annotation_report_from_dict = V2reportsVirusAnnotationReport.from_dict(v2reports_virus_annotation_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


