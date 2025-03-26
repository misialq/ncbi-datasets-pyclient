# V2reportsANIMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembly** | **str** |  | [optional] 
**organism_name** | **str** |  | [optional] 
**category** | [**V2reportsANITypeCategory**](V2reportsANITypeCategory.md) |  | [optional] 
**ani** | **float** |  | [optional] 
**assembly_coverage** | **float** |  | [optional] 
**type_assembly_coverage** | **float** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_ani_match import V2reportsANIMatch

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsANIMatch from a JSON string
v2reports_ani_match_instance = V2reportsANIMatch.from_json(json)
# print the JSON string representation of the object
print(V2reportsANIMatch.to_json())

# convert the object into a dict
v2reports_ani_match_dict = v2reports_ani_match_instance.to_dict()
# create an instance of V2reportsANIMatch from a dict
v2reports_ani_match_from_dict = V2reportsANIMatch.from_dict(v2reports_ani_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


