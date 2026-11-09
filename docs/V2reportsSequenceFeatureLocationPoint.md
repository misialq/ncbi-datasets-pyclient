# V2reportsSequenceFeatureLocationPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**point** | **int** |  | [optional] 
**strand** | [**V2reportsSequenceFeatureLocationStrand**](V2reportsSequenceFeatureLocationStrand.md) |  | [optional] [default to V2reportsSequenceFeatureLocationStrand.STRAND_UNKNOWN]
**point_status** | [**V2reportsSequenceFeatureLocationCoordinateStatus**](V2reportsSequenceFeatureLocationCoordinateStatus.md) |  | [optional] 
**accession** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_feature_location_point import V2reportsSequenceFeatureLocationPoint

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceFeatureLocationPoint from a JSON string
v2reports_sequence_feature_location_point_instance = V2reportsSequenceFeatureLocationPoint.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceFeatureLocationPoint.to_json())

# convert the object into a dict
v2reports_sequence_feature_location_point_dict = v2reports_sequence_feature_location_point_instance.to_dict()
# create an instance of V2reportsSequenceFeatureLocationPoint from a dict
v2reports_sequence_feature_location_point_from_dict = V2reportsSequenceFeatureLocationPoint.from_dict(v2reports_sequence_feature_location_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


