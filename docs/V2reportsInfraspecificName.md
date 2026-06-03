# V2reportsInfraspecificName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strain** | **str** |  | [optional] 
**substrain** | **str** |  | [optional] 
**variety** | **str** |  | [optional] 
**serotype** | **str** |  | [optional] 
**serogroup** | **str** |  | [optional] 
**biotype** | **str** |  | [optional] 
**isolate** | **str** |  | [optional] 
**forma** | **str** |  | [optional] 
**forma_specialis** | **str** |  | [optional] 
**ecotype** | **str** |  | [optional] 
**teleomorph** | **str** |  | [optional] 
**breed** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_infraspecific_name import V2reportsInfraspecificName

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsInfraspecificName from a JSON string
v2reports_infraspecific_name_instance = V2reportsInfraspecificName.from_json(json)
# print the JSON string representation of the object
print(V2reportsInfraspecificName.to_json())

# convert the object into a dict
v2reports_infraspecific_name_dict = v2reports_infraspecific_name_instance.to_dict()
# create an instance of V2reportsInfraspecificName from a dict
v2reports_infraspecific_name_from_dict = V2reportsInfraspecificName.from_dict(v2reports_infraspecific_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


