# V2OrganelleSort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**direction** | [**V2SortDirection**](V2SortDirection.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_organelle_sort import V2OrganelleSort

# TODO update the JSON string below
json = "{}"
# create an instance of V2OrganelleSort from a JSON string
v2_organelle_sort_instance = V2OrganelleSort.from_json(json)
# print the JSON string representation of the object
print(V2OrganelleSort.to_json())

# convert the object into a dict
v2_organelle_sort_dict = v2_organelle_sort_instance.to_dict()
# create an instance of V2OrganelleSort from a dict
v2_organelle_sort_from_dict = V2OrganelleSort.from_dict(v2_organelle_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


