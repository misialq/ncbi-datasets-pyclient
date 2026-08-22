# V2reportsSequenceDataReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**organism_name** | **str** |  | [optional] 
**length** | **int** |  | [optional] 
**update_date** | **str** |  | [optional] 
**units** | [**V2reportsSequenceDataReportUnits**](V2reportsSequenceDataReportUnits.md) |  | [optional] [default to V2reportsSequenceDataReportUnits.UNITS_UNSPECIFIED]
**molecule_type** | [**V2reportsMoleculeType**](V2reportsMoleculeType.md) |  | [optional] [default to V2reportsMoleculeType.MOLECULE_TYPE_UNSPECIFIED]
**sequencing_method** | [**V2reportsSequenceDataReportSequencingMethod**](V2reportsSequenceDataReportSequencingMethod.md) |  | [optional] [default to V2reportsSequenceDataReportSequencingMethod.SEQUENCING_METHOD_UNKNOWN]
**completeness** | [**V2reportsSequenceDataReportCompleteness**](V2reportsSequenceDataReportCompleteness.md) |  | [optional] [default to V2reportsSequenceDataReportCompleteness.COMPLETENESS_UNKNOWN]
**database_provider** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**source_mrna** | **str** |  | [optional] 
**tax_id** | **int** |  | [optional] 
**submissions** | [**List[V2reportsSubmission]**](V2reportsSubmission.md) |  | [optional] 
**references** | [**List[V2reportsSequenceReference]**](V2reportsSequenceReference.md) |  | [optional] 
**bioproject_accession** | **str** |  | [optional] 
**biosample_accessions** | **List[str]** |  | [optional] 
**origin_type** | [**V2reportsSequenceDataReportOriginType**](V2reportsSequenceDataReportOriginType.md) |  | [optional] [default to V2reportsSequenceDataReportOriginType.UNKNOWN]
**infraspecific_modifiers** | [**V2reportsInfraspecificModifers**](V2reportsInfraspecificModifers.md) |  | [optional] 
**sample_info** | [**V2reportsSampleInfo**](V2reportsSampleInfo.md) |  | [optional] 
**genome_type** | [**V2reportsSequenceDataReportGenomeType**](V2reportsSequenceDataReportGenomeType.md) |  | [optional] [default to V2reportsSequenceDataReportGenomeType.GENOME_TYPE_UNKNOWN]
**topology** | [**V2reportsSequenceDataReportTopologyType**](V2reportsSequenceDataReportTopologyType.md) |  | [optional] [default to V2reportsSequenceDataReportTopologyType.NOT_SET]
**protein_name_evidence** | [**V2reportsProteinNameEvidence**](V2reportsProteinNameEvidence.md) |  | [optional] 

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


