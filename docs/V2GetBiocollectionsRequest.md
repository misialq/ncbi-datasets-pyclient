# V2GetBiocollectionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_ids** | **List[str]** |  | [optional] 
**page_size** | **int** |  | [optional] 
**page_token** | **str** |  | [optional] 
**sort** | [**List[V2BiocollectionsSortField]**](V2BiocollectionsSortField.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_get_biocollections_request import V2GetBiocollectionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2GetBiocollectionsRequest from a JSON string
v2_get_biocollections_request_instance = V2GetBiocollectionsRequest.from_json(json)
# print the JSON string representation of the object
print(V2GetBiocollectionsRequest.to_json())

# convert the object into a dict
v2_get_biocollections_request_dict = v2_get_biocollections_request_instance.to_dict()
# create an instance of V2GetBiocollectionsRequest from a dict
v2_get_biocollections_request_from_dict = V2GetBiocollectionsRequest.from_dict(v2_get_biocollections_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


