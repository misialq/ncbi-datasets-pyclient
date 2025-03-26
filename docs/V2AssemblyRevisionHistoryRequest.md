# V2AssemblyRevisionHistoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_assembly_revision_history_request import V2AssemblyRevisionHistoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssemblyRevisionHistoryRequest from a JSON string
v2_assembly_revision_history_request_instance = V2AssemblyRevisionHistoryRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssemblyRevisionHistoryRequest.to_json())

# convert the object into a dict
v2_assembly_revision_history_request_dict = v2_assembly_revision_history_request_instance.to_dict()
# create an instance of V2AssemblyRevisionHistoryRequest from a dict
v2_assembly_revision_history_request_from_dict = V2AssemblyRevisionHistoryRequest.from_dict(v2_assembly_revision_history_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


