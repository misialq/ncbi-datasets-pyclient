# V2reportsAtypicalInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_atypical** | **bool** |  | [optional] 
**warnings** | **List[str]** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_atypical_info import V2reportsAtypicalInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsAtypicalInfo from a JSON string
v2reports_atypical_info_instance = V2reportsAtypicalInfo.from_json(json)
# print the JSON string representation of the object
print(V2reportsAtypicalInfo.to_json())

# convert the object into a dict
v2reports_atypical_info_dict = v2reports_atypical_info_instance.to_dict()
# create an instance of V2reportsAtypicalInfo from a dict
v2reports_atypical_info_from_dict = V2reportsAtypicalInfo.from_dict(v2reports_atypical_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


