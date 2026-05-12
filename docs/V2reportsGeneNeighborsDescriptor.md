# V2reportsGeneNeighborsDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **str** |  | [optional] 
**gene_id** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**gene_type** | [**V2reportsGeneType**](V2reportsGeneType.md) |  | [optional] [default to V2reportsGeneType.UNKNOWN]
**annotations** | [**List[V2reportsGeneNeighborsAnnotation]**](V2reportsGeneNeighborsAnnotation.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_gene_neighbors_descriptor import V2reportsGeneNeighborsDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsGeneNeighborsDescriptor from a JSON string
v2reports_gene_neighbors_descriptor_instance = V2reportsGeneNeighborsDescriptor.from_json(json)
# print the JSON string representation of the object
print(V2reportsGeneNeighborsDescriptor.to_json())

# convert the object into a dict
v2reports_gene_neighbors_descriptor_dict = v2reports_gene_neighbors_descriptor_instance.to_dict()
# create an instance of V2reportsGeneNeighborsDescriptor from a dict
v2reports_gene_neighbors_descriptor_from_dict = V2reportsGeneNeighborsDescriptor.from_dict(v2reports_gene_neighbors_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


