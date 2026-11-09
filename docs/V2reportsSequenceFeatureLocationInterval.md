# V2reportsSequenceFeatureLocationInterval


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **int** |  | [optional] 
**to** | **int** |  | [optional] 
**strand** | [**V2reportsSequenceFeatureLocationStrand**](V2reportsSequenceFeatureLocationStrand.md) |  | [optional] [default to V2reportsSequenceFeatureLocationStrand.STRAND_UNKNOWN]
**from_status** | [**V2reportsSequenceFeatureLocationCoordinateStatus**](V2reportsSequenceFeatureLocationCoordinateStatus.md) |  | [optional] 
**to_status** | [**V2reportsSequenceFeatureLocationCoordinateStatus**](V2reportsSequenceFeatureLocationCoordinateStatus.md) |  | [optional] 
**accession** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_feature_location_interval import V2reportsSequenceFeatureLocationInterval

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceFeatureLocationInterval from a JSON string
v2reports_sequence_feature_location_interval_instance = V2reportsSequenceFeatureLocationInterval.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceFeatureLocationInterval.to_json())

# convert the object into a dict
v2reports_sequence_feature_location_interval_dict = v2reports_sequence_feature_location_interval_instance.to_dict()
# create an instance of V2reportsSequenceFeatureLocationInterval from a dict
v2reports_sequence_feature_location_interval_from_dict = V2reportsSequenceFeatureLocationInterval.from_dict(v2reports_sequence_feature_location_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


