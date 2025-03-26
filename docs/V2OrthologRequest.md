# V2OrthologRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_id** | **int** |  | [optional] 
**returned_content** | [**V2OrthologRequestContentType**](V2OrthologRequestContentType.md) |  | [optional] 
**taxon_filter** | **List[str]** |  | [optional] 
**page_size** | **int** |  | [optional] 
**page_token** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_ortholog_request import V2OrthologRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2OrthologRequest from a JSON string
v2_ortholog_request_instance = V2OrthologRequest.from_json(json)
# print the JSON string representation of the object
print(V2OrthologRequest.to_json())

# convert the object into a dict
v2_ortholog_request_dict = v2_ortholog_request_instance.to_dict()
# create an instance of V2OrthologRequest from a dict
v2_ortholog_request_from_dict = V2OrthologRequest.from_dict(v2_ortholog_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


