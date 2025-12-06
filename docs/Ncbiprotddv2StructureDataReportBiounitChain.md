# Ncbiprotddv2StructureDataReportBiounitChain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chain_id** | **str** |  | [optional] 
**tax_id** | **int** |  | [optional] 
**kind** | [**Ncbiprotddv2StructureDataReportKind**](Ncbiprotddv2StructureDataReportKind.md) |  | [optional] [default to Ncbiprotddv2StructureDataReportKind.DNA]
**molecule_group** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_structure_data_report_biounit_chain import Ncbiprotddv2StructureDataReportBiounitChain

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2StructureDataReportBiounitChain from a JSON string
ncbiprotddv2_structure_data_report_biounit_chain_instance = Ncbiprotddv2StructureDataReportBiounitChain.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2StructureDataReportBiounitChain.to_json())

# convert the object into a dict
ncbiprotddv2_structure_data_report_biounit_chain_dict = ncbiprotddv2_structure_data_report_biounit_chain_instance.to_dict()
# create an instance of Ncbiprotddv2StructureDataReportBiounitChain from a dict
ncbiprotddv2_structure_data_report_biounit_chain_from_dict = Ncbiprotddv2StructureDataReportBiounitChain.from_dict(ncbiprotddv2_structure_data_report_biounit_chain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


