# V2reportsOrganelleGeneCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**protein_coding** | **int** |  | [optional] 
**rrna** | **int** |  | [optional] 
**trna** | **int** |  | [optional] 
**lncrna** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_organelle_gene_counts import V2reportsOrganelleGeneCounts

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsOrganelleGeneCounts from a JSON string
v2reports_organelle_gene_counts_instance = V2reportsOrganelleGeneCounts.from_json(json)
# print the JSON string representation of the object
print(V2reportsOrganelleGeneCounts.to_json())

# convert the object into a dict
v2reports_organelle_gene_counts_dict = v2reports_organelle_gene_counts_instance.to_dict()
# create an instance of V2reportsOrganelleGeneCounts from a dict
v2reports_organelle_gene_counts_from_dict = V2reportsOrganelleGeneCounts.from_dict(v2reports_organelle_gene_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


