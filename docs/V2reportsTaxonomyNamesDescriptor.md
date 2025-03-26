# V2reportsTaxonomyNamesDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **str** |  | [optional] 
**rank** | [**V2reportsRankType**](V2reportsRankType.md) |  | [optional] 
**current_scientific_name** | [**V2reportsNameAndAuthority**](V2reportsNameAndAuthority.md) |  | [optional] 
**group_name** | **str** |  | [optional] 
**curator_common_name** | **str** |  | [optional] 
**other_common_names** | **List[str]** |  | [optional] 
**general_notes** | **List[str]** |  | [optional] 
**links_from_type** | **str** |  | [optional] 
**citations** | [**List[V2reportsTaxonomyNamesDescriptorCitation]**](V2reportsTaxonomyNamesDescriptorCitation.md) |  | [optional] 
**current_scientific_name_is_formal** | **bool** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_taxonomy_names_descriptor import V2reportsTaxonomyNamesDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsTaxonomyNamesDescriptor from a JSON string
v2reports_taxonomy_names_descriptor_instance = V2reportsTaxonomyNamesDescriptor.from_json(json)
# print the JSON string representation of the object
print(V2reportsTaxonomyNamesDescriptor.to_json())

# convert the object into a dict
v2reports_taxonomy_names_descriptor_dict = v2reports_taxonomy_names_descriptor_instance.to_dict()
# create an instance of V2reportsTaxonomyNamesDescriptor from a dict
v2reports_taxonomy_names_descriptor_from_dict = V2reportsTaxonomyNamesDescriptor.from_dict(v2reports_taxonomy_names_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


