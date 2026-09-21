# V2reportsSequenceFeatureLocationIntFuzz


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**p_m** | **int** |  | [optional] 
**range** | [**V2reportsSequenceFeatureLocationFuzzRange**](V2reportsSequenceFeatureLocationFuzzRange.md) |  | [optional] 
**percentage** | **int** |  | [optional] 
**lim** | [**V2reportsSequenceFeatureLocationFuzzLim**](V2reportsSequenceFeatureLocationFuzzLim.md) |  | [optional] [default to V2reportsSequenceFeatureLocationFuzzLim.LIM_UNKNOWN]

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_feature_location_int_fuzz import V2reportsSequenceFeatureLocationIntFuzz

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceFeatureLocationIntFuzz from a JSON string
v2reports_sequence_feature_location_int_fuzz_instance = V2reportsSequenceFeatureLocationIntFuzz.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceFeatureLocationIntFuzz.to_json())

# convert the object into a dict
v2reports_sequence_feature_location_int_fuzz_dict = v2reports_sequence_feature_location_int_fuzz_instance.to_dict()
# create an instance of V2reportsSequenceFeatureLocationIntFuzz from a dict
v2reports_sequence_feature_location_int_fuzz_from_dict = V2reportsSequenceFeatureLocationIntFuzz.from_dict(v2reports_sequence_feature_location_int_fuzz_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


