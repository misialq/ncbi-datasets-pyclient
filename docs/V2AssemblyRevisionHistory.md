# V2AssemblyRevisionHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembly_revisions** | [**List[V2reportsAssemblyRevision]**](V2reportsAssemblyRevision.md) |  | [optional] 
**total_count** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_assembly_revision_history import V2AssemblyRevisionHistory

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssemblyRevisionHistory from a JSON string
v2_assembly_revision_history_instance = V2AssemblyRevisionHistory.from_json(json)
# print the JSON string representation of the object
print(V2AssemblyRevisionHistory.to_json())

# convert the object into a dict
v2_assembly_revision_history_dict = v2_assembly_revision_history_instance.to_dict()
# create an instance of V2AssemblyRevisionHistory from a dict
v2_assembly_revision_history_from_dict = V2AssemblyRevisionHistory.from_dict(v2_assembly_revision_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


