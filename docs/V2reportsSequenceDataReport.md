# V2reportsSequenceDataReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**organism_name** | **str** |  | [optional] 
**length** | **int** |  | [optional] 
**units** | **str** |  | [optional] 
**molecule_type** | **str** |  | [optional] 
**database_provider** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**source_mrna** | **str** |  | [optional] 
**tax_id** | **int** |  | [optional] 
**submissions** | [**List[V2reportsSubmission]**](V2reportsSubmission.md) |  | [optional] 
**references** | [**List[V2reportsSequenceReference]**](V2reportsSequenceReference.md) |  | [optional] 
**bioproject_accession** | **str** |  | [optional] 
**biosample_accessions** | **List[str]** |  | [optional] 
**origin_type** | [**V2reportsSequenceDataReportOriginType**](V2reportsSequenceDataReportOriginType.md) |  | [optional] [default to V2reportsSequenceDataReportOriginType.UNKNOWN]
**specimen_voucher** | [**V2reportsSpecimenVoucher**](V2reportsSpecimenVoucher.md) |  | [optional] 
**infraspecific_names** | [**V2reportsInfraspecificName**](V2reportsInfraspecificName.md) |  | [optional] 
**sample_info** | [**V2reportsSampleInfo**](V2reportsSampleInfo.md) |  | [optional] 
**genome_type** | [**V2reportsSequenceDataReportGenomeType**](V2reportsSequenceDataReportGenomeType.md) |  | [optional] [default to V2reportsSequenceDataReportGenomeType.GENOME_TYPE_UNKNOWN]
**errors** | [**List[V2reportsError]**](V2reportsError.md) |  | [optional] 

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


