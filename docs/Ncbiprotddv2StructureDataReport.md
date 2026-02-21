# Ncbiprotddv2StructureDataReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pdb_id** | **str** |  | [optional] 
**mmdb_id** | **int** |  | [optional] 
**is_obsolete** | **bool** |  | [optional] 
**publication_pmid** | **List[int]** |  | [optional] 
**deposition_date** | **str** |  | [optional] 
**update_date** | **str** |  | [optional] 
**experiment** | [**Ncbiprotddv2StructureDataReportExperiment**](Ncbiprotddv2StructureDataReportExperiment.md) |  | [optional] 
**chains** | [**List[Ncbiprotddv2StructureDataReportBiounitChain]**](Ncbiprotddv2StructureDataReportBiounitChain.md) |  | [optional] 
**ligand_chains** | [**List[Ncbiprotddv2StructureDataReportLigandChain]**](Ncbiprotddv2StructureDataReportLigandChain.md) |  | [optional] 
**asymmetric_chains** | [**List[Ncbiprotddv2StructureDataReportBiounitChain]**](Ncbiprotddv2StructureDataReportBiounitChain.md) |  | [optional] 
**asymmetric_ligands** | [**List[Ncbiprotddv2StructureDataReportLigandChain]**](Ncbiprotddv2StructureDataReportLigandChain.md) |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_structure_data_report import Ncbiprotddv2StructureDataReport

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2StructureDataReport from a JSON string
ncbiprotddv2_structure_data_report_instance = Ncbiprotddv2StructureDataReport.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2StructureDataReport.to_json())

# convert the object into a dict
ncbiprotddv2_structure_data_report_dict = ncbiprotddv2_structure_data_report_instance.to_dict()
# create an instance of Ncbiprotddv2StructureDataReport from a dict
ncbiprotddv2_structure_data_report_from_dict = Ncbiprotddv2StructureDataReport.from_dict(ncbiprotddv2_structure_data_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


