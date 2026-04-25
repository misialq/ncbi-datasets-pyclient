# V2reportsSequenceGeneContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_symbol** | **str** |  | [optional] 
**gene_id** | **str** |  | [optional] 
**genomic_location** | [**V2reportsSequenceGenomicLocation**](V2reportsSequenceGenomicLocation.md) |  | [optional] 
**exons** | [**V2reportsSequenceExonList**](V2reportsSequenceExonList.md) |  | [optional] 
**select_category** | **str** |  | [optional] 
**refseq_select_category** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_gene_context import V2reportsSequenceGeneContext

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceGeneContext from a JSON string
v2reports_sequence_gene_context_instance = V2reportsSequenceGeneContext.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceGeneContext.to_json())

# convert the object into a dict
v2reports_sequence_gene_context_dict = v2reports_sequence_gene_context_instance.to_dict()
# create an instance of V2reportsSequenceGeneContext from a dict
v2reports_sequence_gene_context_from_dict = V2reportsSequenceGeneContext.from_dict(v2reports_sequence_gene_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


