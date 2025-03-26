# V2reportsGeneDataReportPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reports** | [**List[V2reportsGeneReportMatch]**](V2reportsGeneReportMatch.md) |  | [optional] 
**messages** | [**List[V2reportsMessage]**](V2reportsMessage.md) |  | [optional] 
**total_count** | **int** |  | [optional] 
**next_page_token** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_gene_data_report_page import V2reportsGeneDataReportPage

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsGeneDataReportPage from a JSON string
v2reports_gene_data_report_page_instance = V2reportsGeneDataReportPage.from_json(json)
# print the JSON string representation of the object
print(V2reportsGeneDataReportPage.to_json())

# convert the object into a dict
v2reports_gene_data_report_page_dict = v2reports_gene_data_report_page_instance.to_dict()
# create an instance of V2reportsGeneDataReportPage from a dict
v2reports_gene_data_report_page_from_dict = V2reportsGeneDataReportPage.from_dict(v2reports_gene_data_report_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


