# V2reportsAssemblyRevision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genbank_accession** | **str** |  | [optional] 
**refseq_accession** | **str** |  | [optional] 
**assembly_name** | **str** |  | [optional] 
**assembly_level** | [**V2reportsAssemblyLevel**](V2reportsAssemblyLevel.md) |  | [optional] 
**release_date** | **str** |  | [optional] 
**submission_date** | **str** |  | [optional] 
**sequencing_technology** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_assembly_revision import V2reportsAssemblyRevision

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsAssemblyRevision from a JSON string
v2reports_assembly_revision_instance = V2reportsAssemblyRevision.from_json(json)
# print the JSON string representation of the object
print(V2reportsAssemblyRevision.to_json())

# convert the object into a dict
v2reports_assembly_revision_dict = v2reports_assembly_revision_instance.to_dict()
# create an instance of V2reportsAssemblyRevision from a dict
v2reports_assembly_revision_from_dict = V2reportsAssemblyRevision.from_dict(v2reports_assembly_revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


