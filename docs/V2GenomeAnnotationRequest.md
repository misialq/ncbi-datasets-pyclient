# V2GenomeAnnotationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**annotation_ids** | **List[str]** |  | [optional] 
**symbols** | **List[str]** |  | [optional] 
**locations** | **List[str]** |  | [optional] 
**gene_types** | **List[str]** |  | [optional] 
**search_text** | **List[str]** |  | [optional] 
**sort** | [**List[V2SortField]**](V2SortField.md) |  | [optional] 
**include_annotation_type** | [**List[V2GenomeAnnotationRequestAnnotationType]**](V2GenomeAnnotationRequestAnnotationType.md) |  | [optional] 
**page_size** | **int** |  | [optional] 
**table_fields** | **List[str]** |  | [optional] 
**table_format** | [**V2GenomeAnnotationRequestGenomeAnnotationTableFormat**](V2GenomeAnnotationRequestGenomeAnnotationTableFormat.md) |  | [optional] [default to V2GenomeAnnotationRequestGenomeAnnotationTableFormat.NO_TABLE]
**include_tabular_header** | [**V2IncludeTabularHeader**](V2IncludeTabularHeader.md) |  | [optional] [default to V2IncludeTabularHeader.INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY]
**page_token** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_genome_annotation_request import V2GenomeAnnotationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2GenomeAnnotationRequest from a JSON string
v2_genome_annotation_request_instance = V2GenomeAnnotationRequest.from_json(json)
# print the JSON string representation of the object
print(V2GenomeAnnotationRequest.to_json())

# convert the object into a dict
v2_genome_annotation_request_dict = v2_genome_annotation_request_instance.to_dict()
# create an instance of V2GenomeAnnotationRequest from a dict
v2_genome_annotation_request_from_dict = V2GenomeAnnotationRequest.from_dict(v2_genome_annotation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


