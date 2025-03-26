# V2AssemblyAccessions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessions** | **List[str]** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_assembly_accessions import V2AssemblyAccessions

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssemblyAccessions from a JSON string
v2_assembly_accessions_instance = V2AssemblyAccessions.from_json(json)
# print the JSON string representation of the object
print(V2AssemblyAccessions.to_json())

# convert the object into a dict
v2_assembly_accessions_dict = v2_assembly_accessions_instance.to_dict()
# create an instance of V2AssemblyAccessions from a dict
v2_assembly_accessions_from_dict = V2AssemblyAccessions.from_dict(v2_assembly_accessions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


