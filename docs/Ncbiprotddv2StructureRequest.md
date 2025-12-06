# Ncbiprotddv2StructureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pdb_id** | **str** |  | [optional] 
**mmdb_id** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_structure_request import Ncbiprotddv2StructureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2StructureRequest from a JSON string
ncbiprotddv2_structure_request_instance = Ncbiprotddv2StructureRequest.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2StructureRequest.to_json())

# convert the object into a dict
ncbiprotddv2_structure_request_dict = ncbiprotddv2_structure_request_instance.to_dict()
# create an instance of Ncbiprotddv2StructureRequest from a dict
ncbiprotddv2_structure_request_from_dict = Ncbiprotddv2StructureRequest.from_dict(ncbiprotddv2_structure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


