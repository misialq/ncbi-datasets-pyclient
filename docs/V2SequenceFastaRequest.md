# V2SequenceFastaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**begin** | **str** |  | [optional] 
**end** | **str** |  | [optional] 
**orientation** | [**V2reportsOrientation**](V2reportsOrientation.md) |  | [optional] [default to V2reportsOrientation.NONE]
**include_header** | **bool** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_sequence_fasta_request import V2SequenceFastaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2SequenceFastaRequest from a JSON string
v2_sequence_fasta_request_instance = V2SequenceFastaRequest.from_json(json)
# print the JSON string representation of the object
print(V2SequenceFastaRequest.to_json())

# convert the object into a dict
v2_sequence_fasta_request_dict = v2_sequence_fasta_request_instance.to_dict()
# create an instance of V2SequenceFastaRequest from a dict
v2_sequence_fasta_request_from_dict = V2SequenceFastaRequest.from_dict(v2_sequence_fasta_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


