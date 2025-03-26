# V2GenomeAnnotationTableSummaryReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**chromosomes** | **List[str]** |  | [optional] 
**gene_types** | **List[str]** |  | [optional] 
**empty_columns** | **List[str]** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_genome_annotation_table_summary_reply import V2GenomeAnnotationTableSummaryReply

# TODO update the JSON string below
json = "{}"
# create an instance of V2GenomeAnnotationTableSummaryReply from a JSON string
v2_genome_annotation_table_summary_reply_instance = V2GenomeAnnotationTableSummaryReply.from_json(json)
# print the JSON string representation of the object
print(V2GenomeAnnotationTableSummaryReply.to_json())

# convert the object into a dict
v2_genome_annotation_table_summary_reply_dict = v2_genome_annotation_table_summary_reply_instance.to_dict()
# create an instance of V2GenomeAnnotationTableSummaryReply from a dict
v2_genome_annotation_table_summary_reply_from_dict = V2GenomeAnnotationTableSummaryReply.from_dict(v2_genome_annotation_table_summary_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


