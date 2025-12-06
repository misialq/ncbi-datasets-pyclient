# V2GenePubmedIdsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pubmed_ids** | **List[int]** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_gene_pubmed_ids_response import V2GenePubmedIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of V2GenePubmedIdsResponse from a JSON string
v2_gene_pubmed_ids_response_instance = V2GenePubmedIdsResponse.from_json(json)
# print the JSON string representation of the object
print(V2GenePubmedIdsResponse.to_json())

# convert the object into a dict
v2_gene_pubmed_ids_response_dict = v2_gene_pubmed_ids_response_instance.to_dict()
# create an instance of V2GenePubmedIdsResponse from a dict
v2_gene_pubmed_ids_response_from_dict = V2GenePubmedIdsResponse.from_dict(v2_gene_pubmed_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


