# V2SequenceFeaturesByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**feature_ids** | **List[int]** |  | [optional] 
**page_size** | **int** |  | [optional] 
**page_token** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_sequence_features_by_id_request import V2SequenceFeaturesByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2SequenceFeaturesByIdRequest from a JSON string
v2_sequence_features_by_id_request_instance = V2SequenceFeaturesByIdRequest.from_json(json)
# print the JSON string representation of the object
print(V2SequenceFeaturesByIdRequest.to_json())

# convert the object into a dict
v2_sequence_features_by_id_request_dict = v2_sequence_features_by_id_request_instance.to_dict()
# create an instance of V2SequenceFeaturesByIdRequest from a dict
v2_sequence_features_by_id_request_from_dict = V2SequenceFeaturesByIdRequest.from_dict(v2_sequence_features_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


