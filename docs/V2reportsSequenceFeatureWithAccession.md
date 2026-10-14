# V2reportsSequenceFeatureWithAccession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**feature_type** | **str** |  | [optional] 
**location** | [**List[V2reportsSequenceFeatureLocation]**](V2reportsSequenceFeatureLocation.md) |  | [optional] 
**qualifiers** | [**V2reportsSequenceFeatureQualifier**](V2reportsSequenceFeatureQualifier.md) |  | [optional] 
**feature_id** | **int** |  | [optional] 
**parent_feature_id** | **int** |  | [optional] 
**has_children** | **bool** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_feature_with_accession import V2reportsSequenceFeatureWithAccession

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceFeatureWithAccession from a JSON string
v2reports_sequence_feature_with_accession_instance = V2reportsSequenceFeatureWithAccession.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceFeatureWithAccession.to_json())

# convert the object into a dict
v2reports_sequence_feature_with_accession_dict = v2reports_sequence_feature_with_accession_instance.to_dict()
# create an instance of V2reportsSequenceFeatureWithAccession from a dict
v2reports_sequence_feature_with_accession_from_dict = V2reportsSequenceFeatureWithAccession.from_dict(v2reports_sequence_feature_with_accession_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


