# V2AssemblyLinksReplyAssemblyLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**assembly_link_type** | [**V2AssemblyLinksReplyAssemblyLinkType**](V2AssemblyLinksReplyAssemblyLinkType.md) |  | [optional] [default to V2AssemblyLinksReplyAssemblyLinkType.DEFAULT]
**resource_link** | **str** |  | [optional] 
**linked_identifiers** | **List[str]** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_assembly_links_reply_assembly_link import V2AssemblyLinksReplyAssemblyLink

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssemblyLinksReplyAssemblyLink from a JSON string
v2_assembly_links_reply_assembly_link_instance = V2AssemblyLinksReplyAssemblyLink.from_json(json)
# print the JSON string representation of the object
print(V2AssemblyLinksReplyAssemblyLink.to_json())

# convert the object into a dict
v2_assembly_links_reply_assembly_link_dict = v2_assembly_links_reply_assembly_link_instance.to_dict()
# create an instance of V2AssemblyLinksReplyAssemblyLink from a dict
v2_assembly_links_reply_assembly_link_from_dict = V2AssemblyLinksReplyAssemblyLink.from_dict(v2_assembly_links_reply_assembly_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


