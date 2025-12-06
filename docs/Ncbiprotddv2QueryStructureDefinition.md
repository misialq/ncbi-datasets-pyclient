# Ncbiprotddv2QueryStructureDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sdid** | **int** |  | [optional] 
**mmdb_id** | **int** |  | [optional] 
**pdb_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**chain_id** | **str** |  | [optional] 
**domain_number** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_query_structure_definition import Ncbiprotddv2QueryStructureDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2QueryStructureDefinition from a JSON string
ncbiprotddv2_query_structure_definition_instance = Ncbiprotddv2QueryStructureDefinition.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2QueryStructureDefinition.to_json())

# convert the object into a dict
ncbiprotddv2_query_structure_definition_dict = ncbiprotddv2_query_structure_definition_instance.to_dict()
# create an instance of Ncbiprotddv2QueryStructureDefinition from a dict
ncbiprotddv2_query_structure_definition_from_dict = Ncbiprotddv2QueryStructureDefinition.from_dict(ncbiprotddv2_query_structure_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


