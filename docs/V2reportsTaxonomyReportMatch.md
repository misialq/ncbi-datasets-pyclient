# V2reportsTaxonomyReportMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxonomy** | [**V2reportsTaxonomyNode**](V2reportsTaxonomyNode.md) |  | [optional] 
**query** | **List[str]** |  | [optional] 
**warning** | [**V2reportsWarning**](V2reportsWarning.md) |  | [optional] 
**errors** | [**List[V2reportsError]**](V2reportsError.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_taxonomy_report_match import V2reportsTaxonomyReportMatch

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsTaxonomyReportMatch from a JSON string
v2reports_taxonomy_report_match_instance = V2reportsTaxonomyReportMatch.from_json(json)
# print the JSON string representation of the object
print(V2reportsTaxonomyReportMatch.to_json())

# convert the object into a dict
v2reports_taxonomy_report_match_dict = v2reports_taxonomy_report_match_instance.to_dict()
# create an instance of V2reportsTaxonomyReportMatch from a dict
v2reports_taxonomy_report_match_from_dict = V2reportsTaxonomyReportMatch.from_dict(v2reports_taxonomy_report_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


