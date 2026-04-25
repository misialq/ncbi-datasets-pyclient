# V2reportsSequenceGenomicLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chromosome** | **str** |  | [optional] 
**accession** | **str** |  | [optional] 
**range** | [**V2reportsSequenceGenomicRange**](V2reportsSequenceGenomicRange.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_genomic_location import V2reportsSequenceGenomicLocation

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceGenomicLocation from a JSON string
v2reports_sequence_genomic_location_instance = V2reportsSequenceGenomicLocation.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceGenomicLocation.to_json())

# convert the object into a dict
v2reports_sequence_genomic_location_dict = v2reports_sequence_genomic_location_instance.to_dict()
# create an instance of V2reportsSequenceGenomicLocation from a dict
v2reports_sequence_genomic_location_from_dict = V2reportsSequenceGenomicLocation.from_dict(v2reports_sequence_genomic_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


