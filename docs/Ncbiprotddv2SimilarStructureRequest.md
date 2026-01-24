# Ncbiprotddv2SimilarStructureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sdid** | **str** |  | [optional] 
**page_token** | **str** |  | [optional] 
**redundancy_level** | [**Ncbiprotddv2RedundancyLevel**](Ncbiprotddv2RedundancyLevel.md) |  | [optional] [default to Ncbiprotddv2RedundancyLevel.NOT_SPECIFIED]
**sort_by** | [**Ncbiprotddv2SortById**](Ncbiprotddv2SortById.md) |  | [optional] [default to Ncbiprotddv2SortById.NONE]
**hits_per_page** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_similar_structure_request import Ncbiprotddv2SimilarStructureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2SimilarStructureRequest from a JSON string
ncbiprotddv2_similar_structure_request_instance = Ncbiprotddv2SimilarStructureRequest.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2SimilarStructureRequest.to_json())

# convert the object into a dict
ncbiprotddv2_similar_structure_request_dict = ncbiprotddv2_similar_structure_request_instance.to_dict()
# create an instance of Ncbiprotddv2SimilarStructureRequest from a dict
ncbiprotddv2_similar_structure_request_from_dict = Ncbiprotddv2SimilarStructureRequest.from_dict(ncbiprotddv2_similar_structure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


