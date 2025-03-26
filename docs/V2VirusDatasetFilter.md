# V2VirusDatasetFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessions** | **List[str]** |  | [optional] 
**taxon** | **str** |  | [optional] 
**taxons** | **List[str]** |  | [optional] 
**refseq_only** | **bool** |  | [optional] 
**annotated_only** | **bool** |  | [optional] 
**released_since** | **datetime** |  | [optional] 
**updated_since** | **datetime** |  | [optional] 
**host** | **str** |  | [optional] 
**pangolin_classification** | **str** |  | [optional] 
**geo_location** | **str** |  | [optional] 
**usa_state** | **str** |  | [optional] 
**complete_only** | **bool** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_virus_dataset_filter import V2VirusDatasetFilter

# TODO update the JSON string below
json = "{}"
# create an instance of V2VirusDatasetFilter from a JSON string
v2_virus_dataset_filter_instance = V2VirusDatasetFilter.from_json(json)
# print the JSON string representation of the object
print(V2VirusDatasetFilter.to_json())

# convert the object into a dict
v2_virus_dataset_filter_dict = v2_virus_dataset_filter_instance.to_dict()
# create an instance of V2VirusDatasetFilter from a dict
v2_virus_dataset_filter_from_dict = V2VirusDatasetFilter.from_dict(v2_virus_dataset_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


