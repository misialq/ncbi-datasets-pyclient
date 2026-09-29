# Ncbiprotddv2VastProteinChain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asu_molecule_id** | **int** |  | [optional] 
**chain_id** | **str** |  | [optional] 
**protein_chain_name** | **str** |  | [optional] 
**query_domains** | [**List[Ncbiprotddv2VastQueryDomain]**](Ncbiprotddv2VastQueryDomain.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_vast_protein_chain import Ncbiprotddv2VastProteinChain

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2VastProteinChain from a JSON string
ncbiprotddv2_vast_protein_chain_instance = Ncbiprotddv2VastProteinChain.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2VastProteinChain.to_json())

# convert the object into a dict
ncbiprotddv2_vast_protein_chain_dict = ncbiprotddv2_vast_protein_chain_instance.to_dict()
# create an instance of Ncbiprotddv2VastProteinChain from a dict
ncbiprotddv2_vast_protein_chain_from_dict = Ncbiprotddv2VastProteinChain.from_dict(ncbiprotddv2_vast_protein_chain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


