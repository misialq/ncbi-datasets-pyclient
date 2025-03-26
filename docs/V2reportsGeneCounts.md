# V2reportsGeneCounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**protein_coding** | **int** |  | [optional] 
**non_coding** | **int** |  | [optional] 
**pseudogene** | **int** |  | [optional] 
**other** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_gene_counts import V2reportsGeneCounts

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsGeneCounts from a JSON string
v2reports_gene_counts_instance = V2reportsGeneCounts.from_json(json)
# print the JSON string representation of the object
print(V2reportsGeneCounts.to_json())

# convert the object into a dict
v2reports_gene_counts_dict = v2reports_gene_counts_instance.to_dict()
# create an instance of V2reportsGeneCounts from a dict
v2reports_gene_counts_from_dict = V2reportsGeneCounts.from_dict(v2reports_gene_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


