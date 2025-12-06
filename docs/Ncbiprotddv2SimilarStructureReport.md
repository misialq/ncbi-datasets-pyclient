# Ncbiprotddv2SimilarStructureReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sdid** | **int** |  | [optional] 
**structure_title** | **str** |  | [optional] 
**protein_chain_name** | **str** |  | [optional] 
**chain_id** | **str** |  | [optional] 
**domain_number** | **int** |  | [optional] 
**mmdb_id** | **int** |  | [optional] 
**pdb_id** | **str** |  | [optional] 
**vast_score** | [**Ncbiprotddv2VastScore**](Ncbiprotddv2VastScore.md) |  | [optional] 
**align_id** | **int** |  | [optional] 
**superkingdom_id** | **int** |  | [optional] 
**tax_id** | **int** |  | [optional] 
**footprints** | [**List[Ncbiprotddv2ChainFootprint]**](Ncbiprotddv2ChainFootprint.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_similar_structure_report import Ncbiprotddv2SimilarStructureReport

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2SimilarStructureReport from a JSON string
ncbiprotddv2_similar_structure_report_instance = Ncbiprotddv2SimilarStructureReport.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2SimilarStructureReport.to_json())

# convert the object into a dict
ncbiprotddv2_similar_structure_report_dict = ncbiprotddv2_similar_structure_report_instance.to_dict()
# create an instance of Ncbiprotddv2SimilarStructureReport from a dict
ncbiprotddv2_similar_structure_report_from_dict = Ncbiprotddv2SimilarStructureReport.from_dict(ncbiprotddv2_similar_structure_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


