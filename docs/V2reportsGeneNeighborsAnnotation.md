# V2reportsGeneNeighborsAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembly_accession** | **str** |  | [optional] 
**assembly_name** | **str** |  | [optional] 
**annotation_name** | **str** |  | [optional] 
**annotation_release_date** | **str** |  | [optional] 
**genomic_locations** | [**List[V2reportsGeneNeighborGenomicLocation]**](V2reportsGeneNeighborGenomicLocation.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_gene_neighbors_annotation import V2reportsGeneNeighborsAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsGeneNeighborsAnnotation from a JSON string
v2reports_gene_neighbors_annotation_instance = V2reportsGeneNeighborsAnnotation.from_json(json)
# print the JSON string representation of the object
print(V2reportsGeneNeighborsAnnotation.to_json())

# convert the object into a dict
v2reports_gene_neighbors_annotation_dict = v2reports_gene_neighbors_annotation_instance.to_dict()
# create an instance of V2reportsGeneNeighborsAnnotation from a dict
v2reports_gene_neighbors_annotation_from_dict = V2reportsGeneNeighborsAnnotation.from_dict(v2reports_gene_neighbors_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


