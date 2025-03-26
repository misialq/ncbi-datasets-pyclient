# V2AssemblyDatasetAvailability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valid_assemblies** | **List[str]** |  | [optional] 
**invalid_assemblies** | **List[str]** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_assembly_dataset_availability import V2AssemblyDatasetAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssemblyDatasetAvailability from a JSON string
v2_assembly_dataset_availability_instance = V2AssemblyDatasetAvailability.from_json(json)
# print the JSON string representation of the object
print(V2AssemblyDatasetAvailability.to_json())

# convert the object into a dict
v2_assembly_dataset_availability_dict = v2_assembly_dataset_availability_instance.to_dict()
# create an instance of V2AssemblyDatasetAvailability from a dict
v2_assembly_dataset_availability_from_dict = V2AssemblyDatasetAvailability.from_dict(v2_assembly_dataset_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


