# GoogleapiHttpBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | [optional] 
**data** | **bytes** |  | [optional] 
**extensions** | [**List[ProtobufAny]**](ProtobufAny.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.googleapi_http_body import GoogleapiHttpBody

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleapiHttpBody from a JSON string
googleapi_http_body_instance = GoogleapiHttpBody.from_json(json)
# print the JSON string representation of the object
print(GoogleapiHttpBody.to_json())

# convert the object into a dict
googleapi_http_body_dict = googleapi_http_body_instance.to_dict()
# create an instance of GoogleapiHttpBody from a dict
googleapi_http_body_from_dict = GoogleapiHttpBody.from_dict(googleapi_http_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


