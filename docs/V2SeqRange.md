# V2SeqRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**begin** | **str** |  | [optional] 
**end** | **str** |  | [optional] 
**orientation** | [**V2reportsOrientation**](V2reportsOrientation.md) |  | [optional] [default to V2reportsOrientation.NONE]

## Example

```python
from ncbi.datasets.openapi.models.v2_seq_range import V2SeqRange

# TODO update the JSON string below
json = "{}"
# create an instance of V2SeqRange from a JSON string
v2_seq_range_instance = V2SeqRange.from_json(json)
# print the JSON string representation of the object
print(V2SeqRange.to_json())

# convert the object into a dict
v2_seq_range_dict = v2_seq_range_instance.to_dict()
# create an instance of V2SeqRange from a dict
v2_seq_range_from_dict = V2SeqRange.from_dict(v2_seq_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


