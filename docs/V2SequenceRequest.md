# V2SequenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessions** | **List[str]** |  | [optional] 
**include_all_versions** | **bool** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_sequence_request import V2SequenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2SequenceRequest from a JSON string
v2_sequence_request_instance = V2SequenceRequest.from_json(json)
# print the JSON string representation of the object
print(V2SequenceRequest.to_json())

# convert the object into a dict
v2_sequence_request_dict = v2_sequence_request_instance.to_dict()
# create an instance of V2SequenceRequest from a dict
v2_sequence_request_from_dict = V2SequenceRequest.from_dict(v2_sequence_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


