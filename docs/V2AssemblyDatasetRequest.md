# V2AssemblyDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessions** | **List[str]** |  | [optional] 
**chromosomes** | **List[str]** |  | [optional] 
**include_annotation_type** | [**List[V2AnnotationForAssemblyType]**](V2AnnotationForAssemblyType.md) |  | [optional] 
**hydrated** | [**V2AssemblyDatasetRequestResolution**](V2AssemblyDatasetRequestResolution.md) |  | [optional] [default to V2AssemblyDatasetRequestResolution.FULLY_HYDRATED]
**include_tsv** | **bool** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_assembly_dataset_request import V2AssemblyDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssemblyDatasetRequest from a JSON string
v2_assembly_dataset_request_instance = V2AssemblyDatasetRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssemblyDatasetRequest.to_json())

# convert the object into a dict
v2_assembly_dataset_request_dict = v2_assembly_dataset_request_instance.to_dict()
# create an instance of V2AssemblyDatasetRequest from a dict
v2_assembly_dataset_request_from_dict = V2AssemblyDatasetRequest.from_dict(v2_assembly_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


