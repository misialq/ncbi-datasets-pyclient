# V2reportsAssemblyInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembly_level** | **str** |  | [optional] 
**assembly_status** | [**V2reportsAssemblyStatus**](V2reportsAssemblyStatus.md) |  | [optional] 
**paired_assembly** | [**V2reportsPairedAssembly**](V2reportsPairedAssembly.md) |  | [optional] 
**assembly_name** | **str** |  | [optional] 
**assembly_long_name** | **str** |  | [optional] 
**assembly_type** | **str** |  | [optional] 
**bioproject_lineage** | [**List[V2reportsBioProjectLineage]**](V2reportsBioProjectLineage.md) |  | [optional] 
**bioproject_accession** | **str** |  | [optional] 
**submission_date** | **str** |  | [optional] 
**release_date** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**submitter** | **str** |  | [optional] 
**refseq_category** | **str** |  | [optional] 
**synonym** | **str** |  | [optional] 
**linked_assembly** | **str** |  | [optional] 
**linked_assemblies** | [**List[V2reportsLinkedAssembly]**](V2reportsLinkedAssembly.md) |  | [optional] 
**atypical** | [**V2reportsAtypicalInfo**](V2reportsAtypicalInfo.md) |  | [optional] 
**genome_notes** | **List[str]** |  | [optional] 
**sequencing_tech** | **str** |  | [optional] 
**assembly_method** | **str** |  | [optional] 
**grouping_method** | **str** |  | [optional] 
**biosample** | [**V2reportsBioSampleDescriptor**](V2reportsBioSampleDescriptor.md) |  | [optional] 
**blast_url** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**suppression_reason** | **str** |  | [optional] 
**diploid_role** | [**V2reportsLinkedAssemblyType**](V2reportsLinkedAssemblyType.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_assembly_info import V2reportsAssemblyInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsAssemblyInfo from a JSON string
v2reports_assembly_info_instance = V2reportsAssemblyInfo.from_json(json)
# print the JSON string representation of the object
print(V2reportsAssemblyInfo.to_json())

# convert the object into a dict
v2reports_assembly_info_dict = v2reports_assembly_info_instance.to_dict()
# create an instance of V2reportsAssemblyInfo from a dict
v2reports_assembly_info_from_dict = V2reportsAssemblyInfo.from_dict(v2reports_assembly_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


