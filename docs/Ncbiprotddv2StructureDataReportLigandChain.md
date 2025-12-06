# Ncbiprotddv2StructureDataReportLigandChain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** |  | [optional] 
**kind** | [**Ncbiprotddv2StructureDataReportKind**](Ncbiprotddv2StructureDataReportKind.md) |  | [optional] [default to Ncbiprotddv2StructureDataReportKind.DNA]
**molecule_group** | **int** |  | [optional] 
**sid** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_structure_data_report_ligand_chain import Ncbiprotddv2StructureDataReportLigandChain

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2StructureDataReportLigandChain from a JSON string
ncbiprotddv2_structure_data_report_ligand_chain_instance = Ncbiprotddv2StructureDataReportLigandChain.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2StructureDataReportLigandChain.to_json())

# convert the object into a dict
ncbiprotddv2_structure_data_report_ligand_chain_dict = ncbiprotddv2_structure_data_report_ligand_chain_instance.to_dict()
# create an instance of Ncbiprotddv2StructureDataReportLigandChain from a dict
ncbiprotddv2_structure_data_report_ligand_chain_from_dict = Ncbiprotddv2StructureDataReportLigandChain.from_dict(ncbiprotddv2_structure_data_report_ligand_chain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


