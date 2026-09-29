# Ncbiprotddv2GetVastQueryDomainsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mmdb_id** | **int** |  | [optional] 
**pdb_id** | **str** |  | [optional] 
**structure_title** | **str** |  | [optional] 
**status** | [**Ncbiprotddv2VastQueryStatus**](Ncbiprotddv2VastQueryStatus.md) |  | [optional] [default to Ncbiprotddv2VastQueryStatus.VAST_QUERY_STATUS_UNSPECIFIED]
**protein_chains** | [**List[Ncbiprotddv2VastProteinChain]**](Ncbiprotddv2VastProteinChain.md) |  | [optional] 
**replacement** | [**Ncbiprotddv2VastReplacement**](Ncbiprotddv2VastReplacement.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_get_vast_query_domains_response import Ncbiprotddv2GetVastQueryDomainsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2GetVastQueryDomainsResponse from a JSON string
ncbiprotddv2_get_vast_query_domains_response_instance = Ncbiprotddv2GetVastQueryDomainsResponse.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2GetVastQueryDomainsResponse.to_json())

# convert the object into a dict
ncbiprotddv2_get_vast_query_domains_response_dict = ncbiprotddv2_get_vast_query_domains_response_instance.to_dict()
# create an instance of Ncbiprotddv2GetVastQueryDomainsResponse from a dict
ncbiprotddv2_get_vast_query_domains_response_from_dict = Ncbiprotddv2GetVastQueryDomainsResponse.from_dict(ncbiprotddv2_get_vast_query_domains_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


