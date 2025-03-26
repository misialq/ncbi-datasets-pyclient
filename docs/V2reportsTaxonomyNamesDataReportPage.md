# V2reportsTaxonomyNamesDataReportPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reports** | [**List[V2reportsTaxonomyNamesReportMatch]**](V2reportsTaxonomyNamesReportMatch.md) |  | [optional] 
**messages** | [**List[V2reportsMessage]**](V2reportsMessage.md) |  | [optional] 
**total_count** | **int** |  | [optional] 
**next_page_token** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_taxonomy_names_data_report_page import V2reportsTaxonomyNamesDataReportPage

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsTaxonomyNamesDataReportPage from a JSON string
v2reports_taxonomy_names_data_report_page_instance = V2reportsTaxonomyNamesDataReportPage.from_json(json)
# print the JSON string representation of the object
print(V2reportsTaxonomyNamesDataReportPage.to_json())

# convert the object into a dict
v2reports_taxonomy_names_data_report_page_dict = v2reports_taxonomy_names_data_report_page_instance.to_dict()
# create an instance of V2reportsTaxonomyNamesDataReportPage from a dict
v2reports_taxonomy_names_data_report_page_from_dict = V2reportsTaxonomyNamesDataReportPage.from_dict(v2reports_taxonomy_names_data_report_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


