# V2reportsMapLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map_type** | [**V2reportsMapLocationMapType**](V2reportsMapLocationMapType.md) |  | [optional] [default to V2reportsMapLocationMapType.UNKNOWN]
**map_value** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_map_location import V2reportsMapLocation

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsMapLocation from a JSON string
v2reports_map_location_instance = V2reportsMapLocation.from_json(json)
# print the JSON string representation of the object
print(V2reportsMapLocation.to_json())

# convert the object into a dict
v2reports_map_location_dict = v2reports_map_location_instance.to_dict()
# create an instance of V2reportsMapLocation from a dict
v2reports_map_location_from_dict = V2reportsMapLocation.from_dict(v2reports_map_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


