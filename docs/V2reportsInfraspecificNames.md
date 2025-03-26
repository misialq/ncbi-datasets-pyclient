# V2reportsInfraspecificNames


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breed** | **str** |  | [optional] 
**cultivar** | **str** |  | [optional] 
**ecotype** | **str** |  | [optional] 
**isolate** | **str** |  | [optional] 
**sex** | **str** |  | [optional] 
**strain** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_infraspecific_names import V2reportsInfraspecificNames

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsInfraspecificNames from a JSON string
v2reports_infraspecific_names_instance = V2reportsInfraspecificNames.from_json(json)
# print the JSON string representation of the object
print(V2reportsInfraspecificNames.to_json())

# convert the object into a dict
v2reports_infraspecific_names_dict = v2reports_infraspecific_names_instance.to_dict()
# create an instance of V2reportsInfraspecificNames from a dict
v2reports_infraspecific_names_from_dict = V2reportsInfraspecificNames.from_dict(v2reports_infraspecific_names_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


