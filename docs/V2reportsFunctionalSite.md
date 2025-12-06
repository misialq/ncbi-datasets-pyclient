# V2reportsFunctionalSite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**specific** | **bool** |  | [optional] 
**completeness** | **float** |  | [optional] 
**source_accession** | **str** |  | [optional] 
**location** | **List[int]** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_functional_site import V2reportsFunctionalSite

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsFunctionalSite from a JSON string
v2reports_functional_site_instance = V2reportsFunctionalSite.from_json(json)
# print the JSON string representation of the object
print(V2reportsFunctionalSite.to_json())

# convert the object into a dict
v2reports_functional_site_dict = v2reports_functional_site_instance.to_dict()
# create an instance of V2reportsFunctionalSite from a dict
v2reports_functional_site_from_dict = V2reportsFunctionalSite.from_dict(v2reports_functional_site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


