# V2MicroBiggeDatasetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**opaque_solr_query** | **str** |  | [optional] 
**files** | [**List[V2MicroBiggeDatasetRequestFileType]**](V2MicroBiggeDatasetRequestFileType.md) |  | [optional] 
**element_flank_config** | [**V2ElementFlankConfig**](V2ElementFlankConfig.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_micro_bigge_dataset_request import V2MicroBiggeDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2MicroBiggeDatasetRequest from a JSON string
v2_micro_bigge_dataset_request_instance = V2MicroBiggeDatasetRequest.from_json(json)
# print the JSON string representation of the object
print(V2MicroBiggeDatasetRequest.to_json())

# convert the object into a dict
v2_micro_bigge_dataset_request_dict = v2_micro_bigge_dataset_request_instance.to_dict()
# create an instance of V2MicroBiggeDatasetRequest from a dict
v2_micro_bigge_dataset_request_from_dict = V2MicroBiggeDatasetRequest.from_dict(v2_micro_bigge_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


