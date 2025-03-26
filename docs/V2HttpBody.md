# V2HttpBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | [optional] 
**data** | **bytearray** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_http_body import V2HttpBody

# TODO update the JSON string below
json = "{}"
# create an instance of V2HttpBody from a JSON string
v2_http_body_instance = V2HttpBody.from_json(json)
# print the JSON string representation of the object
print(V2HttpBody.to_json())

# convert the object into a dict
v2_http_body_dict = v2_http_body_instance.to_dict()
# create an instance of V2HttpBody from a dict
v2_http_body_from_dict = V2HttpBody.from_dict(v2_http_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


