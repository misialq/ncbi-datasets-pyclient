# V2SequenceFileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**format** | [**V2SequenceFileRequestFormat**](V2SequenceFileRequestFormat.md) |  | [optional] [default to V2SequenceFileRequestFormat.GENBANK]

## Example

```python
from ncbi.datasets.openapi.models.v2_sequence_file_request import V2SequenceFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2SequenceFileRequest from a JSON string
v2_sequence_file_request_instance = V2SequenceFileRequest.from_json(json)
# print the JSON string representation of the object
print(V2SequenceFileRequest.to_json())

# convert the object into a dict
v2_sequence_file_request_dict = v2_sequence_file_request_instance.to_dict()
# create an instance of V2SequenceFileRequest from a dict
v2_sequence_file_request_from_dict = V2SequenceFileRequest.from_dict(v2_sequence_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


