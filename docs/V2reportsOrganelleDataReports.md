# V2reportsOrganelleDataReports


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[V2reportsMessage]**](V2reportsMessage.md) |  | [optional] 
**reports** | [**List[V2reportsOrganelle]**](V2reportsOrganelle.md) |  | [optional] 
**total_count** | **int** |  | [optional] 
**next_page_token** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_organelle_data_reports import V2reportsOrganelleDataReports

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsOrganelleDataReports from a JSON string
v2reports_organelle_data_reports_instance = V2reportsOrganelleDataReports.from_json(json)
# print the JSON string representation of the object
print(V2reportsOrganelleDataReports.to_json())

# convert the object into a dict
v2reports_organelle_data_reports_dict = v2reports_organelle_data_reports_instance.to_dict()
# create an instance of V2reportsOrganelleDataReports from a dict
v2reports_organelle_data_reports_from_dict = V2reportsOrganelleDataReports.from_dict(v2reports_organelle_data_reports_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


