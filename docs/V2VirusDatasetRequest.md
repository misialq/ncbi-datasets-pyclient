# V2VirusDatasetRequest


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
**table_fields** | [**List[V2VirusTableField]**](V2VirusTableField.md) |  | [optional] 
**include_sequence** | [**List[V2ViralSequenceType]**](V2ViralSequenceType.md) |  | [optional] 
**aux_report** | [**List[V2VirusDatasetReportType]**](V2VirusDatasetReportType.md) |  | [optional] 
**format** | [**V2TableFormat**](V2TableFormat.md) |  | [optional] 
**use_psg** | **bool** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_virus_dataset_request import V2VirusDatasetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2VirusDatasetRequest from a JSON string
v2_virus_dataset_request_instance = V2VirusDatasetRequest.from_json(json)
# print the JSON string representation of the object
print(V2VirusDatasetRequest.to_json())

# convert the object into a dict
v2_virus_dataset_request_dict = v2_virus_dataset_request_instance.to_dict()
# create an instance of V2VirusDatasetRequest from a dict
v2_virus_dataset_request_from_dict = V2VirusDatasetRequest.from_dict(v2_virus_dataset_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


