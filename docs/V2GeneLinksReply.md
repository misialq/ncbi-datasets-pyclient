# V2GeneLinksReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_links** | [**List[V2GeneLinksReplyGeneLink]**](V2GeneLinksReplyGeneLink.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_gene_links_reply import V2GeneLinksReply

# TODO update the JSON string below
json = "{}"
# create an instance of V2GeneLinksReply from a JSON string
v2_gene_links_reply_instance = V2GeneLinksReply.from_json(json)
# print the JSON string representation of the object
print(V2GeneLinksReply.to_json())

# convert the object into a dict
v2_gene_links_reply_dict = v2_gene_links_reply_instance.to_dict()
# create an instance of V2GeneLinksReply from a dict
v2_gene_links_reply_from_dict = V2GeneLinksReply.from_dict(v2_gene_links_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


