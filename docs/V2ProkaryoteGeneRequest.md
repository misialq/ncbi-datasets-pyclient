# V2ProkaryoteGeneRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessions** | **List[str]** |  | [optional] 
**include_annotation_type** | [**List[V2Fasta]**](V2Fasta.md) |  | [optional] 
**gene_flank_config** | [**V2ProkaryoteGeneRequestGeneFlankConfig**](V2ProkaryoteGeneRequestGeneFlankConfig.md) |  | [optional] 
**taxon** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_prokaryote_gene_request import V2ProkaryoteGeneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2ProkaryoteGeneRequest from a JSON string
v2_prokaryote_gene_request_instance = V2ProkaryoteGeneRequest.from_json(json)
# print the JSON string representation of the object
print(V2ProkaryoteGeneRequest.to_json())

# convert the object into a dict
v2_prokaryote_gene_request_dict = v2_prokaryote_gene_request_instance.to_dict()
# create an instance of V2ProkaryoteGeneRequest from a dict
v2_prokaryote_gene_request_from_dict = V2ProkaryoteGeneRequest.from_dict(v2_prokaryote_gene_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


