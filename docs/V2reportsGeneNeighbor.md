# V2reportsGeneNeighbor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_id** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**gene_type** | [**V2reportsGeneType**](V2reportsGeneType.md) |  | [optional] [default to V2reportsGeneType.UNKNOWN]
**genomic_range** | [**V2reportsRange**](V2reportsRange.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_gene_neighbor import V2reportsGeneNeighbor

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsGeneNeighbor from a JSON string
v2reports_gene_neighbor_instance = V2reportsGeneNeighbor.from_json(json)
# print the JSON string representation of the object
print(V2reportsGeneNeighbor.to_json())

# convert the object into a dict
v2reports_gene_neighbor_dict = v2reports_gene_neighbor_instance.to_dict()
# create an instance of V2reportsGeneNeighbor from a dict
v2reports_gene_neighbor_from_dict = V2reportsGeneNeighbor.from_dict(v2reports_gene_neighbor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


