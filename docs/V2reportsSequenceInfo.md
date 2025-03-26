# V2reportsSequenceInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembly_accession** | **str** |  | [optional] 
**chr_name** | **str** |  | [optional] 
**ucsc_style_name** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**assigned_molecule_location_type** | **str** |  | [optional] 
**refseq_accession** | **str** |  | [optional] 
**assembly_unit** | **str** |  | [optional] 
**length** | **int** |  | [optional] 
**genbank_accession** | **str** |  | [optional] 
**gc_count** | **str** |  | [optional] 
**gc_percent** | **float** |  | [optional] 
**unlocalized_count** | **int** |  | [optional] 
**assembly_unplaced_count** | **int** |  | [optional] 
**role** | **str** |  | [optional] 
**sequence_name** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_info import V2reportsSequenceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceInfo from a JSON string
v2reports_sequence_info_instance = V2reportsSequenceInfo.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceInfo.to_json())

# convert the object into a dict
v2reports_sequence_info_dict = v2reports_sequence_info_instance.to_dict()
# create an instance of V2reportsSequenceInfo from a dict
v2reports_sequence_info_from_dict = V2reportsSequenceInfo.from_dict(v2reports_sequence_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


