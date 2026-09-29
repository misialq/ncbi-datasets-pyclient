# Ncbiprotddv2VastQueryDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sdid** | **int** |  | [optional] 
**domain_number** | **int** |  | [optional] 
**intervals** | [**List[Ncbiprotddv2VastResidueInterval]**](Ncbiprotddv2VastResidueInterval.md) |  | [optional] 
**all_sequences_result_count** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_vast_query_domain import Ncbiprotddv2VastQueryDomain

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2VastQueryDomain from a JSON string
ncbiprotddv2_vast_query_domain_instance = Ncbiprotddv2VastQueryDomain.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2VastQueryDomain.to_json())

# convert the object into a dict
ncbiprotddv2_vast_query_domain_dict = ncbiprotddv2_vast_query_domain_instance.to_dict()
# create an instance of Ncbiprotddv2VastQueryDomain from a dict
ncbiprotddv2_vast_query_domain_from_dict = Ncbiprotddv2VastQueryDomain.from_dict(ncbiprotddv2_vast_query_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


