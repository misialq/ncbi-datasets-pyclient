# V2reportsSequenceFeature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**locus_tag** | **str** |  | [optional] 
**gene_id** | **str** |  | [optional] 
**location** | [**V2reportsSequenceFeatureLocation**](V2reportsSequenceFeatureLocation.md) |  | [optional] 
**other_names** | **List[str]** |  | [optional] 
**ec_number** | **List[str]** |  | [optional] 
**coded_protein_info** | [**V2reportsSequenceCodedProteinInfo**](V2reportsSequenceCodedProteinInfo.md) |  | [optional] 
**prediction_source** | [**V2reportsSequencePredictionSource**](V2reportsSequencePredictionSource.md) |  | [optional] 
**data_provenance** | [**V2reportsSequenceDataProvenance**](V2reportsSequenceDataProvenance.md) |  | [optional] 
**signal_sequence** | **str** |  | [optional] 
**nested_features** | [**List[V2reportsSequenceFeature]**](V2reportsSequenceFeature.md) |  | [optional] 

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


