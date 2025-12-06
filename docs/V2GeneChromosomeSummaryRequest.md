# V2GeneChromosomeSummaryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxon** | **str** |  | [optional] 
**annotation_name** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_gene_chromosome_summary_request import V2GeneChromosomeSummaryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2GeneChromosomeSummaryRequest from a JSON string
v2_gene_chromosome_summary_request_instance = V2GeneChromosomeSummaryRequest.from_json(json)
# print the JSON string representation of the object
print(V2GeneChromosomeSummaryRequest.to_json())

# convert the object into a dict
v2_gene_chromosome_summary_request_dict = v2_gene_chromosome_summary_request_instance.to_dict()
# create an instance of V2GeneChromosomeSummaryRequest from a dict
v2_gene_chromosome_summary_request_from_dict = V2GeneChromosomeSummaryRequest.from_dict(v2_gene_chromosome_summary_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


