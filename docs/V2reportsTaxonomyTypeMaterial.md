# V2reportsTaxonomyTypeMaterial


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_strain_name** | **str** |  | [optional] 
**type_strain_id** | **str** |  | [optional] 
**bio_collection_id** | **str** |  | [optional] 
**bio_collection_name** | **str** |  | [optional] 
**collection_type** | [**List[V2reportsCollectionType]**](V2reportsCollectionType.md) |  | [optional] 
**type_class** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_taxonomy_type_material import V2reportsTaxonomyTypeMaterial

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsTaxonomyTypeMaterial from a JSON string
v2reports_taxonomy_type_material_instance = V2reportsTaxonomyTypeMaterial.from_json(json)
# print the JSON string representation of the object
print(V2reportsTaxonomyTypeMaterial.to_json())

# convert the object into a dict
v2reports_taxonomy_type_material_dict = v2reports_taxonomy_type_material_instance.to_dict()
# create an instance of V2reportsTaxonomyTypeMaterial from a dict
v2reports_taxonomy_type_material_from_dict = V2reportsTaxonomyTypeMaterial.from_dict(v2reports_taxonomy_type_material_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


