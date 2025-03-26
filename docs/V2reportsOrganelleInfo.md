# V2reportsOrganelleInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembly_name** | **str** |  | [optional] 
**infraspecific_name** | **str** |  | [optional] 
**bioproject** | **List[str]** |  | [optional] 
**description** | **str** |  | [optional] 
**total_seq_length** | **str** |  | [optional] 
**submitter** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_organelle_info import V2reportsOrganelleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsOrganelleInfo from a JSON string
v2reports_organelle_info_instance = V2reportsOrganelleInfo.from_json(json)
# print the JSON string representation of the object
print(V2reportsOrganelleInfo.to_json())

# convert the object into a dict
v2reports_organelle_info_dict = v2reports_organelle_info_instance.to_dict()
# create an instance of V2reportsOrganelleInfo from a dict
v2reports_organelle_info_from_dict = V2reportsOrganelleInfo.from_dict(v2reports_organelle_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


