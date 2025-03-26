# V2reportsLinkedAssembly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linked_assembly** | **str** |  | [optional] 
**assembly_type** | [**V2reportsLinkedAssemblyType**](V2reportsLinkedAssemblyType.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_linked_assembly import V2reportsLinkedAssembly

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsLinkedAssembly from a JSON string
v2reports_linked_assembly_instance = V2reportsLinkedAssembly.from_json(json)
# print the JSON string representation of the object
print(V2reportsLinkedAssembly.to_json())

# convert the object into a dict
v2reports_linked_assembly_dict = v2reports_linked_assembly_instance.to_dict()
# create an instance of V2reportsLinkedAssembly from a dict
v2reports_linked_assembly_from_dict = V2reportsLinkedAssembly.from_dict(v2reports_linked_assembly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


