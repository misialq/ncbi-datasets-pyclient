# V2reportsVirusGene


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**gene_id** | **int** |  | [optional] 
**nucleotide** | [**V2reportsSeqRangeSetFasta**](V2reportsSeqRangeSetFasta.md) |  | [optional] 
**cds** | [**List[V2reportsVirusPeptide]**](V2reportsVirusPeptide.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_virus_gene import V2reportsVirusGene

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsVirusGene from a JSON string
v2reports_virus_gene_instance = V2reportsVirusGene.from_json(json)
# print the JSON string representation of the object
print(V2reportsVirusGene.to_json())

# convert the object into a dict
v2reports_virus_gene_dict = v2reports_virus_gene_instance.to_dict()
# create an instance of V2reportsVirusGene from a dict
v2reports_virus_gene_from_dict = V2reportsVirusGene.from_dict(v2reports_virus_gene_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


