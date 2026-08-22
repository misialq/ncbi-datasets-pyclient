# V2SeqReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**length** | **str** |  | [optional] 
**molecule_type** | [**V2reportsMoleculeType**](V2reportsMoleculeType.md) |  | [optional] [default to V2reportsMoleculeType.MOLECULE_TYPE_UNSPECIFIED]
**defline** | **str** |  | [optional] 
**sequence** | **str** |  | [optional] 
**begin** | **str** |  | [optional] 
**end** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_seq_reply import V2SeqReply

# TODO update the JSON string below
json = "{}"
# create an instance of V2SeqReply from a JSON string
v2_seq_reply_instance = V2SeqReply.from_json(json)
# print the JSON string representation of the object
print(V2SeqReply.to_json())

# convert the object into a dict
v2_seq_reply_dict = v2_seq_reply_instance.to_dict()
# create an instance of V2SeqReply from a dict
v2_seq_reply_from_dict = V2SeqReply.from_dict(v2_seq_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


