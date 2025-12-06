# V2GeneLinksReplyGeneLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_id** | **int** |  | [optional] 
**gene_link_type** | [**V2GeneLinksReplyGeneLinkType**](V2GeneLinksReplyGeneLinkType.md) |  | [optional] [default to V2GeneLinksReplyGeneLinkType.DEFAULT]
**resource_link** | **str** |  | [optional] 
**resource_id** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_gene_links_reply_gene_link import V2GeneLinksReplyGeneLink

# TODO update the JSON string below
json = "{}"
# create an instance of V2GeneLinksReplyGeneLink from a JSON string
v2_gene_links_reply_gene_link_instance = V2GeneLinksReplyGeneLink.from_json(json)
# print the JSON string representation of the object
print(V2GeneLinksReplyGeneLink.to_json())

# convert the object into a dict
v2_gene_links_reply_gene_link_dict = v2_gene_links_reply_gene_link_instance.to_dict()
# create an instance of V2GeneLinksReplyGeneLink from a dict
v2_gene_links_reply_gene_link_from_dict = V2GeneLinksReplyGeneLink.from_dict(v2_gene_links_reply_gene_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


