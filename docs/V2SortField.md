# V2SortField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**direction** | [**V2SortDirection**](V2SortDirection.md) |  | [optional] [default to V2SortDirection.SORT_DIRECTION_UNSPECIFIED]

## Example

```python
from ncbi.datasets.openapi.models.v2_sort_field import V2SortField

# TODO update the JSON string below
json = "{}"
# create an instance of V2SortField from a JSON string
v2_sort_field_instance = V2SortField.from_json(json)
# print the JSON string representation of the object
print(V2SortField.to_json())

# convert the object into a dict
v2_sort_field_dict = v2_sort_field_instance.to_dict()
# create an instance of V2SortField from a dict
v2_sort_field_from_dict = V2SortField.from_dict(v2_sort_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


