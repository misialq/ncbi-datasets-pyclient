# V2SequenceAccessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_sequence_accession_request import V2SequenceAccessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2SequenceAccessionRequest from a JSON string
v2_sequence_accession_request_instance = V2SequenceAccessionRequest.from_json(json)
# print the JSON string representation of the object
print(V2SequenceAccessionRequest.to_json())

# convert the object into a dict
v2_sequence_accession_request_dict = v2_sequence_accession_request_instance.to_dict()
# create an instance of V2SequenceAccessionRequest from a dict
v2_sequence_accession_request_from_dict = V2SequenceAccessionRequest.from_dict(v2_sequence_accession_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


