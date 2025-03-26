# V2AssemblyLinksRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessions** | **List[str]** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_assembly_links_request import V2AssemblyLinksRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssemblyLinksRequest from a JSON string
v2_assembly_links_request_instance = V2AssemblyLinksRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssemblyLinksRequest.to_json())

# convert the object into a dict
v2_assembly_links_request_dict = v2_assembly_links_request_instance.to_dict()
# create an instance of V2AssemblyLinksRequest from a dict
v2_assembly_links_request_from_dict = V2AssemblyLinksRequest.from_dict(v2_assembly_links_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


