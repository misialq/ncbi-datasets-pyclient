# V2reportsRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **str** |  | [optional] 
**end** | **str** |  | [optional] 
**orientation** | [**V2reportsOrientation**](V2reportsOrientation.md) |  | [optional] [default to V2reportsOrientation.NONE]
**order** | **int** |  | [optional] 
**ribosomal_slippage** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_range import V2reportsRange

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsRange from a JSON string
v2reports_range_instance = V2reportsRange.from_json(json)
# print the JSON string representation of the object
print(V2reportsRange.to_json())

# convert the object into a dict
v2reports_range_dict = v2reports_range_instance.to_dict()
# create an instance of V2reportsRange from a dict
v2reports_range_from_dict = V2reportsRange.from_dict(v2reports_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


