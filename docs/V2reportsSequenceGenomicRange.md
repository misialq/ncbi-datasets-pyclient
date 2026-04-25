# V2reportsSequenceGenomicRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **str** |  | [optional] 
**end** | **str** |  | [optional] 
**orientation** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_genomic_range import V2reportsSequenceGenomicRange

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceGenomicRange from a JSON string
v2reports_sequence_genomic_range_instance = V2reportsSequenceGenomicRange.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceGenomicRange.to_json())

# convert the object into a dict
v2reports_sequence_genomic_range_dict = v2reports_sequence_genomic_range_instance.to_dict()
# create an instance of V2reportsSequenceGenomicRange from a dict
v2reports_sequence_genomic_range_from_dict = V2reportsSequenceGenomicRange.from_dict(v2reports_sequence_genomic_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


