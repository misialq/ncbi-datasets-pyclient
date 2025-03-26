# V2reportsGeneGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**method** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_gene_group import V2reportsGeneGroup

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsGeneGroup from a JSON string
v2reports_gene_group_instance = V2reportsGeneGroup.from_json(json)
# print the JSON string representation of the object
print(V2reportsGeneGroup.to_json())

# convert the object into a dict
v2reports_gene_group_dict = v2reports_gene_group_instance.to_dict()
# create an instance of V2reportsGeneGroup from a dict
v2reports_gene_group_from_dict = V2reportsGeneGroup.from_dict(v2reports_gene_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


