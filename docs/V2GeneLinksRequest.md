# V2GeneLinksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_ids** | **List[int]** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_gene_links_request import V2GeneLinksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2GeneLinksRequest from a JSON string
v2_gene_links_request_instance = V2GeneLinksRequest.from_json(json)
# print the JSON string representation of the object
print(V2GeneLinksRequest.to_json())

# convert the object into a dict
v2_gene_links_request_dict = v2_gene_links_request_instance.to_dict()
# create an instance of V2GeneLinksRequest from a dict
v2_gene_links_request_from_dict = V2GeneLinksRequest.from_dict(v2_gene_links_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


