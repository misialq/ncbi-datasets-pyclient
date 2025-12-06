# V2reportsProteinDataReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**length** | **int** |  | [optional] 
**gene_id** | **int** |  | [optional] 
**identical_protein_group** | **int** |  | [optional] 
**conserved_domains** | [**List[V2reportsProteinConservedDomain]**](V2reportsProteinConservedDomain.md) |  | [optional] 
**functional_sites** | [**List[V2reportsFunctionalSite]**](V2reportsFunctionalSite.md) |  | [optional] 
**protein_families** | [**List[V2reportsProteinFamily]**](V2reportsProteinFamily.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_protein_data_report import V2reportsProteinDataReport

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsProteinDataReport from a JSON string
v2reports_protein_data_report_instance = V2reportsProteinDataReport.from_json(json)
# print the JSON string representation of the object
print(V2reportsProteinDataReport.to_json())

# convert the object into a dict
v2reports_protein_data_report_dict = v2reports_protein_data_report_instance.to_dict()
# create an instance of V2reportsProteinDataReport from a dict
v2reports_protein_data_report_from_dict = V2reportsProteinDataReport.from_dict(v2reports_protein_data_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


