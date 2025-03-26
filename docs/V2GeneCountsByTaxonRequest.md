# V2GeneCountsByTaxonRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**taxon** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_gene_counts_by_taxon_request import V2GeneCountsByTaxonRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2GeneCountsByTaxonRequest from a JSON string
v2_gene_counts_by_taxon_request_instance = V2GeneCountsByTaxonRequest.from_json(json)
# print the JSON string representation of the object
print(V2GeneCountsByTaxonRequest.to_json())

# convert the object into a dict
v2_gene_counts_by_taxon_request_dict = v2_gene_counts_by_taxon_request_instance.to_dict()
# create an instance of V2GeneCountsByTaxonRequest from a dict
v2_gene_counts_by_taxon_request_from_dict = V2GeneCountsByTaxonRequest.from_dict(v2_gene_counts_by_taxon_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


