# Ncbiprotddv2ChainFootprint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query_from** | **int** |  | [optional] 
**query_to** | **int** |  | [optional] 
**dependent_from** | **int** |  | [optional] 
**dependent_to** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_chain_footprint import Ncbiprotddv2ChainFootprint

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2ChainFootprint from a JSON string
ncbiprotddv2_chain_footprint_instance = Ncbiprotddv2ChainFootprint.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2ChainFootprint.to_json())

# convert the object into a dict
ncbiprotddv2_chain_footprint_dict = ncbiprotddv2_chain_footprint_instance.to_dict()
# create an instance of Ncbiprotddv2ChainFootprint from a dict
ncbiprotddv2_chain_footprint_from_dict = Ncbiprotddv2ChainFootprint.from_dict(ncbiprotddv2_chain_footprint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


