# V2SequenceFeatureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**page_size** | **int** |  | [optional] 
**page_token** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_sequence_feature_request import V2SequenceFeatureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2SequenceFeatureRequest from a JSON string
v2_sequence_feature_request_instance = V2SequenceFeatureRequest.from_json(json)
# print the JSON string representation of the object
print(V2SequenceFeatureRequest.to_json())

# convert the object into a dict
v2_sequence_feature_request_dict = v2_sequence_feature_request_instance.to_dict()
# create an instance of V2SequenceFeatureRequest from a dict
v2_sequence_feature_request_from_dict = V2SequenceFeatureRequest.from_dict(v2_sequence_feature_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


