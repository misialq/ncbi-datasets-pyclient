# V2archiveSequence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**length** | **int** |  | [optional] 
**units** | [**V2archiveSequenceLengthUnits**](V2archiveSequenceLengthUnits.md) |  | [optional] [default to V2archiveSequenceLengthUnits.SEQUENCE_LENGTH_UNITS_UNSPECIFIED]

## Example

```python
from ncbi.datasets.openapi.models.v2archive_sequence import V2archiveSequence

# TODO update the JSON string below
json = "{}"
# create an instance of V2archiveSequence from a JSON string
v2archive_sequence_instance = V2archiveSequence.from_json(json)
# print the JSON string representation of the object
print(V2archiveSequence.to_json())

# convert the object into a dict
v2archive_sequence_dict = v2archive_sequence_instance.to_dict()
# create an instance of V2archiveSequence from a dict
v2archive_sequence_from_dict = V2archiveSequence.from_dict(v2archive_sequence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


