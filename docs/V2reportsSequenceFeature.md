# V2reportsSequenceFeature


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
**database_cross_references** | [**List[V2reportsDatabaseReference]**](V2reportsDatabaseReference.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_feature import V2reportsSequenceFeature

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceFeature from a JSON string
v2reports_sequence_feature_instance = V2reportsSequenceFeature.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceFeature.to_json())

# convert the object into a dict
v2reports_sequence_feature_dict = v2reports_sequence_feature_instance.to_dict()
# create an instance of V2reportsSequenceFeature from a dict
v2reports_sequence_feature_from_dict = V2reportsSequenceFeature.from_dict(v2reports_sequence_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


