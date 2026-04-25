# V2reportsSequenceDataProvenance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_database** | **str** |  | [optional] 
**source_accession** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_data_provenance import V2reportsSequenceDataProvenance

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceDataProvenance from a JSON string
v2reports_sequence_data_provenance_instance = V2reportsSequenceDataProvenance.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceDataProvenance.to_json())

# convert the object into a dict
v2reports_sequence_data_provenance_dict = v2reports_sequence_data_provenance_instance.to_dict()
# create an instance of V2reportsSequenceDataProvenance from a dict
v2reports_sequence_data_provenance_from_dict = V2reportsSequenceDataProvenance.from_dict(v2reports_sequence_data_provenance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


