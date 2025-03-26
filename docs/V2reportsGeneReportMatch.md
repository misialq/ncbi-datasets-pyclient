# V2reportsGeneReportMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene** | [**V2reportsGeneDescriptor**](V2reportsGeneDescriptor.md) |  | [optional] 
**product** | [**V2reportsProductDescriptor**](V2reportsProductDescriptor.md) |  | [optional] 
**query** | **List[str]** |  | [optional] 
**warnings** | [**List[V2reportsWarning]**](V2reportsWarning.md) |  | [optional] 
**warning** | [**V2reportsWarning**](V2reportsWarning.md) |  | [optional] 
**errors** | [**List[V2reportsError]**](V2reportsError.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_gene_report_match import V2reportsGeneReportMatch

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsGeneReportMatch from a JSON string
v2reports_gene_report_match_instance = V2reportsGeneReportMatch.from_json(json)
# print the JSON string representation of the object
print(V2reportsGeneReportMatch.to_json())

# convert the object into a dict
v2reports_gene_report_match_dict = v2reports_gene_report_match_instance.to_dict()
# create an instance of V2reportsGeneReportMatch from a dict
v2reports_gene_report_match_from_dict = V2reportsGeneReportMatch.from_dict(v2reports_gene_report_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


