# V2reportsNameAndAuthority


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**authority** | **str** |  | [optional] 
**type_strains** | [**List[V2reportsTaxonomyTypeMaterial]**](V2reportsTaxonomyTypeMaterial.md) |  | [optional] 
**curator_synonym** | **str** |  | [optional] 
**homotypic_synonyms** | [**List[V2reportsNameAndAuthority]**](V2reportsNameAndAuthority.md) |  | [optional] 
**heterotypic_synonyms** | [**List[V2reportsNameAndAuthority]**](V2reportsNameAndAuthority.md) |  | [optional] 
**other_synonyms** | [**List[V2reportsNameAndAuthority]**](V2reportsNameAndAuthority.md) |  | [optional] 
**informal_names** | **List[str]** |  | [optional] 
**basionym** | [**V2reportsNameAndAuthority**](V2reportsNameAndAuthority.md) |  | [optional] 
**publications** | [**List[V2reportsNameAndAuthorityPublication]**](V2reportsNameAndAuthorityPublication.md) |  | [optional] 
**notes** | [**List[V2reportsNameAndAuthorityNote]**](V2reportsNameAndAuthorityNote.md) |  | [optional] 
**formal** | **bool** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_name_and_authority import V2reportsNameAndAuthority

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsNameAndAuthority from a JSON string
v2reports_name_and_authority_instance = V2reportsNameAndAuthority.from_json(json)
# print the JSON string representation of the object
print(V2reportsNameAndAuthority.to_json())

# convert the object into a dict
v2reports_name_and_authority_dict = v2reports_name_and_authority_instance.to_dict()
# create an instance of V2reportsNameAndAuthority from a dict
v2reports_name_and_authority_from_dict = V2reportsNameAndAuthority.from_dict(v2reports_name_and_authority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


