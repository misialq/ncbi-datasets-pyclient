# V2reportsSequenceFeatureLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin** | **str** |  | [optional] 
**end** | **str** |  | [optional] 
**position** | **str** |  | [optional] 
**orientation** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_feature_location import V2reportsSequenceFeatureLocation

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceFeatureLocation from a JSON string
v2reports_sequence_feature_location_instance = V2reportsSequenceFeatureLocation.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceFeatureLocation.to_json())

# convert the object into a dict
v2reports_sequence_feature_location_dict = v2reports_sequence_feature_location_instance.to_dict()
# create an instance of V2reportsSequenceFeatureLocation from a dict
v2reports_sequence_feature_location_from_dict = V2reportsSequenceFeatureLocation.from_dict(v2reports_sequence_feature_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


