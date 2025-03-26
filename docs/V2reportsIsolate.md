# V2reportsIsolate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**collection_date** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_isolate import V2reportsIsolate

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsIsolate from a JSON string
v2reports_isolate_instance = V2reportsIsolate.from_json(json)
# print the JSON string representation of the object
print(V2reportsIsolate.to_json())

# convert the object into a dict
v2reports_isolate_dict = v2reports_isolate_instance.to_dict()
# create an instance of V2reportsIsolate from a dict
v2reports_isolate_from_dict = V2reportsIsolate.from_dict(v2reports_isolate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


