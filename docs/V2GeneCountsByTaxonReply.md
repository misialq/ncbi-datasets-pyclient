# V2GeneCountsByTaxonReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report** | [**List[V2GeneCountsByTaxonReplyGeneTypeAndCount]**](V2GeneCountsByTaxonReplyGeneTypeAndCount.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_gene_counts_by_taxon_reply import V2GeneCountsByTaxonReply

# TODO update the JSON string below
json = "{}"
# create an instance of V2GeneCountsByTaxonReply from a JSON string
v2_gene_counts_by_taxon_reply_instance = V2GeneCountsByTaxonReply.from_json(json)
# print the JSON string representation of the object
print(V2GeneCountsByTaxonReply.to_json())

# convert the object into a dict
v2_gene_counts_by_taxon_reply_dict = v2_gene_counts_by_taxon_reply_instance.to_dict()
# create an instance of V2GeneCountsByTaxonReply from a dict
v2_gene_counts_by_taxon_reply_from_dict = V2GeneCountsByTaxonReply.from_dict(v2_gene_counts_by_taxon_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


