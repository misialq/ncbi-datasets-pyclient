# V2reportsSequenceDataReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**organism_name** | **str** |  | [optional] 
**length** | **int** |  | [optional] 
**units** | **str** |  | [optional] 
**molecule_type** | **str** |  | [optional] 
**source_database** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**source_mrna** | **str** |  | [optional] 
**encoded_proteins** | [**List[V2reportsSequenceEncodedProtein]**](V2reportsSequenceEncodedProtein.md) |  | [optional] 
**publication_date** | **str** |  | [optional] 
**latest_update_date** | **str** |  | [optional] 
**gene_context** | [**V2reportsSequenceGeneContext**](V2reportsSequenceGeneContext.md) |  | [optional] 
**features** | [**List[V2reportsSequenceFeature]**](V2reportsSequenceFeature.md) |  | [optional] 
**external_ids** | [**List[V2reportsSequenceExternalId]**](V2reportsSequenceExternalId.md) |  | [optional] 
**tax_id** | **int** |  | [optional] 
**submissions** | [**List[V2reportsSubmission]**](V2reportsSubmission.md) |  | [optional] 
**publications** | [**List[V2reportsPublication]**](V2reportsPublication.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_data_report import V2reportsSequenceDataReport

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceDataReport from a JSON string
v2reports_sequence_data_report_instance = V2reportsSequenceDataReport.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceDataReport.to_json())

# convert the object into a dict
v2reports_sequence_data_report_dict = v2reports_sequence_data_report_instance.to_dict()
# create an instance of V2reportsSequenceDataReport from a dict
v2reports_sequence_data_report_from_dict = V2reportsSequenceDataReport.from_dict(v2reports_sequence_data_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


