# V2reportsAssemblyDataReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**current_accession** | **str** |  | [optional] 
**paired_accession** | **str** |  | [optional] 
**source_database** | [**V2reportsSourceDatabase**](V2reportsSourceDatabase.md) |  | [optional] [default to V2reportsSourceDatabase.SOURCE_DATABASE_UNSPECIFIED]
**organism** | [**V2reportsOrganism**](V2reportsOrganism.md) |  | [optional] 
**assembly_info** | [**V2reportsAssemblyInfo**](V2reportsAssemblyInfo.md) |  | [optional] 
**assembly_stats** | [**V2reportsAssemblyStats**](V2reportsAssemblyStats.md) |  | [optional] 
**organelle_info** | [**List[V2reportsOrganelleInfo]**](V2reportsOrganelleInfo.md) |  | [optional] 
**additional_submitters** | [**List[V2reportsAdditionalSubmitter]**](V2reportsAdditionalSubmitter.md) |  | [optional] 
**annotation_info** | [**V2reportsAnnotationInfo**](V2reportsAnnotationInfo.md) |  | [optional] 
**wgs_info** | [**V2reportsWGSInfo**](V2reportsWGSInfo.md) |  | [optional] 
**type_material** | [**V2reportsTypeMaterial**](V2reportsTypeMaterial.md) |  | [optional] 
**checkm_info** | [**V2reportsCheckM**](V2reportsCheckM.md) |  | [optional] 
**average_nucleotide_identity** | [**V2reportsAverageNucleotideIdentity**](V2reportsAverageNucleotideIdentity.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_assembly_data_report import V2reportsAssemblyDataReport

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsAssemblyDataReport from a JSON string
v2reports_assembly_data_report_instance = V2reportsAssemblyDataReport.from_json(json)
# print the JSON string representation of the object
print(V2reportsAssemblyDataReport.to_json())

# convert the object into a dict
v2reports_assembly_data_report_dict = v2reports_assembly_data_report_instance.to_dict()
# create an instance of V2reportsAssemblyDataReport from a dict
v2reports_assembly_data_report_from_dict = V2reportsAssemblyDataReport.from_dict(v2reports_assembly_data_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


