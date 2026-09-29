# Ncbiprotddv2GetVastQueryDomainsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pdb_id** | **str** |  | [optional] 
**mmdb_id** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_get_vast_query_domains_request import Ncbiprotddv2GetVastQueryDomainsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2GetVastQueryDomainsRequest from a JSON string
ncbiprotddv2_get_vast_query_domains_request_instance = Ncbiprotddv2GetVastQueryDomainsRequest.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2GetVastQueryDomainsRequest.to_json())

# convert the object into a dict
ncbiprotddv2_get_vast_query_domains_request_dict = ncbiprotddv2_get_vast_query_domains_request_instance.to_dict()
# create an instance of Ncbiprotddv2GetVastQueryDomainsRequest from a dict
ncbiprotddv2_get_vast_query_domains_request_from_dict = Ncbiprotddv2GetVastQueryDomainsRequest.from_dict(ncbiprotddv2_get_vast_query_domains_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


