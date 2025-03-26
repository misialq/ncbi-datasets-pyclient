# V2reportsVirusAssemblySubmitterInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** |  | [optional] 
**affiliation** | **str** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_virus_assembly_submitter_info import V2reportsVirusAssemblySubmitterInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsVirusAssemblySubmitterInfo from a JSON string
v2reports_virus_assembly_submitter_info_instance = V2reportsVirusAssemblySubmitterInfo.from_json(json)
# print the JSON string representation of the object
print(V2reportsVirusAssemblySubmitterInfo.to_json())

# convert the object into a dict
v2reports_virus_assembly_submitter_info_dict = v2reports_virus_assembly_submitter_info_instance.to_dict()
# create an instance of V2reportsVirusAssemblySubmitterInfo from a dict
v2reports_virus_assembly_submitter_info_from_dict = V2reportsVirusAssemblySubmitterInfo.from_dict(v2reports_virus_assembly_submitter_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


