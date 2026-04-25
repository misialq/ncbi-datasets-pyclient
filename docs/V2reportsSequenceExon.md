# V2reportsSequenceExon


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exon_number** | **int** |  | [optional] 
**begin** | **str** |  | [optional] 
**end** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_exon import V2reportsSequenceExon

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceExon from a JSON string
v2reports_sequence_exon_instance = V2reportsSequenceExon.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceExon.to_json())

# convert the object into a dict
v2reports_sequence_exon_dict = v2reports_sequence_exon_instance.to_dict()
# create an instance of V2reportsSequenceExon from a dict
v2reports_sequence_exon_from_dict = V2reportsSequenceExon.from_dict(v2reports_sequence_exon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


