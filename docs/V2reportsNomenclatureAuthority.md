# V2reportsNomenclatureAuthority


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authority** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_nomenclature_authority import V2reportsNomenclatureAuthority

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsNomenclatureAuthority from a JSON string
v2reports_nomenclature_authority_instance = V2reportsNomenclatureAuthority.from_json(json)
# print the JSON string representation of the object
print(V2reportsNomenclatureAuthority.to_json())

# convert the object into a dict
v2reports_nomenclature_authority_dict = v2reports_nomenclature_authority_instance.to_dict()
# create an instance of V2reportsNomenclatureAuthority from a dict
v2reports_nomenclature_authority_from_dict = V2reportsNomenclatureAuthority.from_dict(v2reports_nomenclature_authority_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


