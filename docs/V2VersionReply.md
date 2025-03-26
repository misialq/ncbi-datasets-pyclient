# V2VersionReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**major_ver** | **int** |  | [optional] 
**minor_ver** | **int** |  | [optional] 
**patch_ver** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_version_reply import V2VersionReply

# TODO update the JSON string below
json = "{}"
# create an instance of V2VersionReply from a JSON string
v2_version_reply_instance = V2VersionReply.from_json(json)
# print the JSON string representation of the object
print(V2VersionReply.to_json())

# convert the object into a dict
v2_version_reply_dict = v2_version_reply_instance.to_dict()
# create an instance of V2VersionReply from a dict
v2_version_reply_from_dict = V2VersionReply.from_dict(v2_version_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


