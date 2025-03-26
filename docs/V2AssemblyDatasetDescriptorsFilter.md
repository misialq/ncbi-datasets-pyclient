# V2AssemblyDatasetDescriptorsFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_only** | **bool** |  | [optional] 
**assembly_source** | [**V2AssemblyDatasetDescriptorsFilterAssemblySource**](V2AssemblyDatasetDescriptorsFilterAssemblySource.md) |  | [optional] 
**has_annotation** | **bool** |  | [optional] 
**exclude_paired_reports** | **bool** |  | [optional] 
**exclude_atypical** | **bool** |  | [optional] 
**assembly_version** | [**V2AssemblyDatasetDescriptorsFilterAssemblyVersion**](V2AssemblyDatasetDescriptorsFilterAssemblyVersion.md) |  | [optional] 
**assembly_level** | [**List[V2reportsAssemblyLevel]**](V2reportsAssemblyLevel.md) |  | [optional] 
**first_release_date** | **datetime** |  | [optional] 
**last_release_date** | **datetime** |  | [optional] 
**search_text** | **List[str]** |  | [optional] 
**is_metagenome_derived** | [**V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter**](V2AssemblyDatasetDescriptorsFilterMetagenomeDerivedFilter.md) |  | [optional] 
**is_type_material** | **bool** |  | [optional] 
**is_ictv_exemplar** | **bool** |  | [optional] 
**exclude_multi_isolate** | **bool** |  | [optional] 
**type_material_category** | [**V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory**](V2AssemblyDatasetDescriptorsFilterTypeMaterialCategory.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter import V2AssemblyDatasetDescriptorsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssemblyDatasetDescriptorsFilter from a JSON string
v2_assembly_dataset_descriptors_filter_instance = V2AssemblyDatasetDescriptorsFilter.from_json(json)
# print the JSON string representation of the object
print(V2AssemblyDatasetDescriptorsFilter.to_json())

# convert the object into a dict
v2_assembly_dataset_descriptors_filter_dict = v2_assembly_dataset_descriptors_filter_instance.to_dict()
# create an instance of V2AssemblyDatasetDescriptorsFilter from a dict
v2_assembly_dataset_descriptors_filter_from_dict = V2AssemblyDatasetDescriptorsFilter.from_dict(v2_assembly_dataset_descriptors_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


