# V2GeneChromosomeSummaryReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_chromosome_summaries** | [**List[V2GeneChromosomeSummaryReplyGeneChromosomeSummary]**](V2GeneChromosomeSummaryReplyGeneChromosomeSummary.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_gene_chromosome_summary_reply import V2GeneChromosomeSummaryReply

# TODO update the JSON string below
json = "{}"
# create an instance of V2GeneChromosomeSummaryReply from a JSON string
v2_gene_chromosome_summary_reply_instance = V2GeneChromosomeSummaryReply.from_json(json)
# print the JSON string representation of the object
print(V2GeneChromosomeSummaryReply.to_json())

# convert the object into a dict
v2_gene_chromosome_summary_reply_dict = v2_gene_chromosome_summary_reply_instance.to_dict()
# create an instance of V2GeneChromosomeSummaryReply from a dict
v2_gene_chromosome_summary_reply_from_dict = V2GeneChromosomeSummaryReply.from_dict(v2_gene_chromosome_summary_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


