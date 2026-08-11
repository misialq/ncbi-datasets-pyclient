# V2SequenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessions** | **List[str]** |  | [optional] 
**include_all_versions** | **bool** |  | [optional] 
**returned_content** | [**V2SequenceRequestContentType**](V2SequenceRequestContentType.md) |  | [optional] [default to V2SequenceRequestContentType.COMPLETE]
**include_tabular_header** | [**V2IncludeTabularHeader**](V2IncludeTabularHeader.md) |  | [optional] [default to V2IncludeTabularHeader.INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
**table_format** | [**V2SequenceRequestTableFormat**](V2SequenceRequestTableFormat.md) |  | [optional] [default to V2SequenceRequestTableFormat.SUMMARY]

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


