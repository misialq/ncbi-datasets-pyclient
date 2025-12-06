# Ncbiprotddv2SimilarStructureReportPage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**similar_structures** | [**List[Ncbiprotddv2SimilarStructureReport]**](Ncbiprotddv2SimilarStructureReport.md) |  | [optional] 
**next_page_token** | **str** |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_similar_structure_report_page import Ncbiprotddv2SimilarStructureReportPage

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2SimilarStructureReportPage from a JSON string
ncbiprotddv2_similar_structure_report_page_instance = Ncbiprotddv2SimilarStructureReportPage.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2SimilarStructureReportPage.to_json())

# convert the object into a dict
ncbiprotddv2_similar_structure_report_page_dict = ncbiprotddv2_similar_structure_report_page_instance.to_dict()
# create an instance of Ncbiprotddv2SimilarStructureReportPage from a dict
ncbiprotddv2_similar_structure_report_page_from_dict = Ncbiprotddv2SimilarStructureReportPage.from_dict(ncbiprotddv2_similar_structure_report_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


