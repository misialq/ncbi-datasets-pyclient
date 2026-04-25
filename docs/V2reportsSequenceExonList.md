# V2reportsSequenceExonList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**inference_method** | **str** |  | [optional] 
**items** | [**List[V2reportsSequenceExon]**](V2reportsSequenceExon.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_exon_list import V2reportsSequenceExonList

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceExonList from a JSON string
v2reports_sequence_exon_list_instance = V2reportsSequenceExonList.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceExonList.to_json())

# convert the object into a dict
v2reports_sequence_exon_list_dict = v2reports_sequence_exon_list_instance.to_dict()
# create an instance of V2reportsSequenceExonList from a dict
v2reports_sequence_exon_list_from_dict = V2reportsSequenceExonList.from_dict(v2reports_sequence_exon_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


