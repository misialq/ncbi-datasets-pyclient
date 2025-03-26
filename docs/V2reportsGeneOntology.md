# V2reportsGeneOntology


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assigned_by** | **str** |  | [optional] 
**molecular_functions** | [**List[V2reportsProcessMetadata]**](V2reportsProcessMetadata.md) |  | [optional] 
**biological_processes** | [**List[V2reportsProcessMetadata]**](V2reportsProcessMetadata.md) |  | [optional] 
**cellular_components** | [**List[V2reportsProcessMetadata]**](V2reportsProcessMetadata.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_gene_ontology import V2reportsGeneOntology

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsGeneOntology from a JSON string
v2reports_gene_ontology_instance = V2reportsGeneOntology.from_json(json)
# print the JSON string representation of the object
print(V2reportsGeneOntology.to_json())

# convert the object into a dict
v2reports_gene_ontology_dict = v2reports_gene_ontology_instance.to_dict()
# create an instance of V2reportsGeneOntology from a dict
v2reports_gene_ontology_from_dict = V2reportsGeneOntology.from_dict(v2reports_gene_ontology_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


