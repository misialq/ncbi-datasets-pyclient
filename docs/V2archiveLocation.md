# V2archiveLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** |  | [optional] 
**sub** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**street** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2archive_location import V2archiveLocation

# TODO update the JSON string below
json = "{}"
# create an instance of V2archiveLocation from a JSON string
v2archive_location_instance = V2archiveLocation.from_json(json)
# print the JSON string representation of the object
print(V2archiveLocation.to_json())

# convert the object into a dict
v2archive_location_dict = v2archive_location_instance.to_dict()
# create an instance of V2archiveLocation from a dict
v2archive_location_from_dict = V2archiveLocation.from_dict(v2archive_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


