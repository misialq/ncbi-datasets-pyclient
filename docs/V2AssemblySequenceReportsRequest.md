# V2AssemblySequenceReportsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**chromosomes** | **List[str]** |  | [optional] 
**role_filters** | **List[str]** |  | [optional] 
**table_fields** | **List[str]** |  | [optional] 
**count_assembly_unplaced** | **bool** |  | [optional] 
**page_size** | **int** |  | [optional] 
**page_token** | **str** |  | [optional] 
**include_tabular_header** | [**V2IncludeTabularHeader**](V2IncludeTabularHeader.md) |  | [optional] 
**table_format** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_assembly_sequence_reports_request import V2AssemblySequenceReportsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2AssemblySequenceReportsRequest from a JSON string
v2_assembly_sequence_reports_request_instance = V2AssemblySequenceReportsRequest.from_json(json)
# print the JSON string representation of the object
print(V2AssemblySequenceReportsRequest.to_json())

# convert the object into a dict
v2_assembly_sequence_reports_request_dict = v2_assembly_sequence_reports_request_instance.to_dict()
# create an instance of V2AssemblySequenceReportsRequest from a dict
v2_assembly_sequence_reports_request_from_dict = V2AssemblySequenceReportsRequest.from_dict(v2_assembly_sequence_reports_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


