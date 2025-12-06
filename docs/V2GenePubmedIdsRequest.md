# V2GenePubmedIdsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_ids** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_gene_pubmed_ids_request import V2GenePubmedIdsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2GenePubmedIdsRequest from a JSON string
v2_gene_pubmed_ids_request_instance = V2GenePubmedIdsRequest.from_json(json)
# print the JSON string representation of the object
print(V2GenePubmedIdsRequest.to_json())

# convert the object into a dict
v2_gene_pubmed_ids_request_dict = v2_gene_pubmed_ids_request_instance.to_dict()
# create an instance of V2GenePubmedIdsRequest from a dict
v2_gene_pubmed_ids_request_from_dict = V2GenePubmedIdsRequest.from_dict(v2_gene_pubmed_ids_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


