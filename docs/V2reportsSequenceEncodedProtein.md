# V2reportsSequenceEncodedProtein


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_encoded_protein import V2reportsSequenceEncodedProtein

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceEncodedProtein from a JSON string
v2reports_sequence_encoded_protein_instance = V2reportsSequenceEncodedProtein.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceEncodedProtein.to_json())

# convert the object into a dict
v2reports_sequence_encoded_protein_dict = v2reports_sequence_encoded_protein_instance.to_dict()
# create an instance of V2reportsSequenceEncodedProtein from a dict
v2reports_sequence_encoded_protein_from_dict = V2reportsSequenceEncodedProtein.from_dict(v2reports_sequence_encoded_protein_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


