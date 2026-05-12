# V2reportsGeneNeighborGenomicLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genomic_location** | [**V2reportsGenomicLocation**](V2reportsGenomicLocation.md) |  | [optional] 
**gene_neighbors** | [**List[V2reportsGeneNeighbor]**](V2reportsGeneNeighbor.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_gene_neighbor_genomic_location import V2reportsGeneNeighborGenomicLocation

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsGeneNeighborGenomicLocation from a JSON string
v2reports_gene_neighbor_genomic_location_instance = V2reportsGeneNeighborGenomicLocation.from_json(json)
# print the JSON string representation of the object
print(V2reportsGeneNeighborGenomicLocation.to_json())

# convert the object into a dict
v2reports_gene_neighbor_genomic_location_dict = v2reports_gene_neighbor_genomic_location_instance.to_dict()
# create an instance of V2reportsGeneNeighborGenomicLocation from a dict
v2reports_gene_neighbor_genomic_location_from_dict = V2reportsGeneNeighborGenomicLocation.from_dict(v2reports_gene_neighbor_genomic_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


