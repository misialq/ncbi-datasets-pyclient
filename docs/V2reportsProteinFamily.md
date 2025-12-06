# V2reportsProteinFamily


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** |  | [optional] 
**identifier** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_protein_family import V2reportsProteinFamily

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsProteinFamily from a JSON string
v2reports_protein_family_instance = V2reportsProteinFamily.from_json(json)
# print the JSON string representation of the object
print(V2reportsProteinFamily.to_json())

# convert the object into a dict
v2reports_protein_family_dict = v2reports_protein_family_instance.to_dict()
# create an instance of V2reportsProteinFamily from a dict
v2reports_protein_family_from_dict = V2reportsProteinFamily.from_dict(v2reports_protein_family_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


