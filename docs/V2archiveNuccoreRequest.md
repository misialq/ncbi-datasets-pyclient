# V2archiveNuccoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2archive_nuccore_request import V2archiveNuccoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2archiveNuccoreRequest from a JSON string
v2archive_nuccore_request_instance = V2archiveNuccoreRequest.from_json(json)
# print the JSON string representation of the object
print(V2archiveNuccoreRequest.to_json())

# convert the object into a dict
v2archive_nuccore_request_dict = v2archive_nuccore_request_instance.to_dict()
# create an instance of V2archiveNuccoreRequest from a dict
v2archive_nuccore_request_from_dict = V2archiveNuccoreRequest.from_dict(v2archive_nuccore_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


