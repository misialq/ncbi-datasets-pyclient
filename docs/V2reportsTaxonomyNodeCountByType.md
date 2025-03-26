# V2reportsTaxonomyNodeCountByType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**V2reportsCountType**](V2reportsCountType.md) |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_taxonomy_node_count_by_type import V2reportsTaxonomyNodeCountByType

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsTaxonomyNodeCountByType from a JSON string
v2reports_taxonomy_node_count_by_type_instance = V2reportsTaxonomyNodeCountByType.from_json(json)
# print the JSON string representation of the object
print(V2reportsTaxonomyNodeCountByType.to_json())

# convert the object into a dict
v2reports_taxonomy_node_count_by_type_dict = v2reports_taxonomy_node_count_by_type_instance.to_dict()
# create an instance of V2reportsTaxonomyNodeCountByType from a dict
v2reports_taxonomy_node_count_by_type_from_dict = V2reportsTaxonomyNodeCountByType.from_dict(v2reports_taxonomy_node_count_by_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


