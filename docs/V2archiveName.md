# V2archiveName


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | **str** |  | [optional] 
**middle** | **str** |  | [optional] 
**last** | **str** |  | [optional] 
**full** | **str** |  | [optional] 
**initials** | **str** |  | [optional] 
**suffix** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**affiliation** | [**V2archiveAffiliation**](V2archiveAffiliation.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2archive_name import V2archiveName

# TODO update the JSON string below
json = "{}"
# create an instance of V2archiveName from a JSON string
v2archive_name_instance = V2archiveName.from_json(json)
# print the JSON string representation of the object
print(V2archiveName.to_json())

# convert the object into a dict
v2archive_name_dict = v2archive_name_instance.to_dict()
# create an instance of V2archiveName from a dict
v2archive_name_from_dict = V2archiveName.from_dict(v2archive_name_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


