# V2SequenceFeatureTreeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_sequence_feature_tree_request import V2SequenceFeatureTreeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2SequenceFeatureTreeRequest from a JSON string
v2_sequence_feature_tree_request_instance = V2SequenceFeatureTreeRequest.from_json(json)
# print the JSON string representation of the object
print(V2SequenceFeatureTreeRequest.to_json())

# convert the object into a dict
v2_sequence_feature_tree_request_dict = v2_sequence_feature_tree_request_instance.to_dict()
# create an instance of V2SequenceFeatureTreeRequest from a dict
v2_sequence_feature_tree_request_from_dict = V2SequenceFeatureTreeRequest.from_dict(v2_sequence_feature_tree_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


