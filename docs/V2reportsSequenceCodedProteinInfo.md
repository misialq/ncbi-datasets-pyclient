# V2reportsSequenceCodedProteinInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_coded_protein_info import V2reportsSequenceCodedProteinInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceCodedProteinInfo from a JSON string
v2reports_sequence_coded_protein_info_instance = V2reportsSequenceCodedProteinInfo.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceCodedProteinInfo.to_json())

# convert the object into a dict
v2reports_sequence_coded_protein_info_dict = v2reports_sequence_coded_protein_info_instance.to_dict()
# create an instance of V2reportsSequenceCodedProteinInfo from a dict
v2reports_sequence_coded_protein_info_from_dict = V2reportsSequenceCodedProteinInfo.from_dict(v2reports_sequence_coded_protein_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


