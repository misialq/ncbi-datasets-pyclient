# V2reportsProductDescriptor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_id** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**taxname** | **str** |  | [optional] 
**common_name** | **str** |  | [optional] 
**type** | [**V2reportsGeneType**](V2reportsGeneType.md) |  | [optional] [default to V2reportsGeneType.UNKNOWN]
**rna_type** | [**V2reportsRnaType**](V2reportsRnaType.md) |  | [optional] [default to V2reportsRnaType.RNA_UNKNOWN]
**transcripts** | [**List[V2reportsTranscript]**](V2reportsTranscript.md) |  | [optional] 
**transcript_count** | **int** |  | [optional] 
**protein_count** | **int** |  | [optional] 
**transcript_type_counts** | [**List[V2reportsTranscriptTypeCount]**](V2reportsTranscriptTypeCount.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_product_descriptor import V2reportsProductDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsProductDescriptor from a JSON string
v2reports_product_descriptor_instance = V2reportsProductDescriptor.from_json(json)
# print the JSON string representation of the object
print(V2reportsProductDescriptor.to_json())

# convert the object into a dict
v2reports_product_descriptor_dict = v2reports_product_descriptor_instance.to_dict()
# create an instance of V2reportsProductDescriptor from a dict
v2reports_product_descriptor_from_dict = V2reportsProductDescriptor.from_dict(v2reports_product_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


