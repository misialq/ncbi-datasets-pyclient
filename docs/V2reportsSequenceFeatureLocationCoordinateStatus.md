# V2reportsSequenceFeatureLocationCoordinateStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | [**V2reportsSequenceFeatureLocationCoordinateStatusRange**](V2reportsSequenceFeatureLocationCoordinateStatusRange.md) |  | [optional] 
**partial** | [**V2reportsSequenceFeatureLocationCoordinateStatusPartial**](V2reportsSequenceFeatureLocationCoordinateStatusPartial.md) |  | [optional] [default to V2reportsSequenceFeatureLocationCoordinateStatusPartial.PARTIAL_UNKNOWN]
**between** | [**V2reportsSequenceFeatureLocationCoordinateStatusBetween**](V2reportsSequenceFeatureLocationCoordinateStatusBetween.md) |  | [optional] [default to V2reportsSequenceFeatureLocationCoordinateStatusBetween.BETWEEN_UNKNOWN]
**plus_minus** | **int** |  | [optional] 
**percent** | **float** |  | [optional] 
**alternatives** | [**V2reportsSequenceFeatureLocationCoordinateStatusAlternatives**](V2reportsSequenceFeatureLocationCoordinateStatusAlternatives.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_feature_location_coordinate_status import V2reportsSequenceFeatureLocationCoordinateStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceFeatureLocationCoordinateStatus from a JSON string
v2reports_sequence_feature_location_coordinate_status_instance = V2reportsSequenceFeatureLocationCoordinateStatus.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceFeatureLocationCoordinateStatus.to_json())

# convert the object into a dict
v2reports_sequence_feature_location_coordinate_status_dict = v2reports_sequence_feature_location_coordinate_status_instance.to_dict()
# create an instance of V2reportsSequenceFeatureLocationCoordinateStatus from a dict
v2reports_sequence_feature_location_coordinate_status_from_dict = V2reportsSequenceFeatureLocationCoordinateStatus.from_dict(v2reports_sequence_feature_location_coordinate_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


