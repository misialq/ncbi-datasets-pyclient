# V2reportsGeneral


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pmid** | **int** |  | [optional] 
**title** | **str** |  | [optional] 
**var_date** | **str** |  | [optional] 
**authors** | [**List[V2reportsAuthor]**](V2reportsAuthor.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_general import V2reportsGeneral

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsGeneral from a JSON string
v2reports_general_instance = V2reportsGeneral.from_json(json)
# print the JSON string representation of the object
print(V2reportsGeneral.to_json())

# convert the object into a dict
v2reports_general_dict = v2reports_general_instance.to_dict()
# create an instance of V2reportsGeneral from a dict
v2reports_general_from_dict = V2reportsGeneral.from_dict(v2reports_general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


