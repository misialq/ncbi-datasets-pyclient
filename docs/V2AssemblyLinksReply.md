# V2AssemblyLinksReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembly_links** | [**List[V2AssemblyLinksReplyAssemblyLink]**](V2AssemblyLinksReplyAssemblyLink.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_assembly_links_reply import V2AssemblyLinksReply

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssemblyLinksReply from a JSON string
v2_assembly_links_reply_instance = V2AssemblyLinksReply.from_json(json)
# print the JSON string representation of the object
print(V2AssemblyLinksReply.to_json())

# convert the object into a dict
v2_assembly_links_reply_dict = v2_assembly_links_reply_instance.to_dict()
# create an instance of V2AssemblyLinksReply from a dict
v2_assembly_links_reply_from_dict = V2AssemblyLinksReply.from_dict(v2_assembly_links_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


