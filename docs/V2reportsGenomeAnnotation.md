# V2reportsGenomeAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_id** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**taxname** | **str** |  | [optional] 
**common_name** | **str** |  | [optional] 
**type** | [**V2reportsGeneType**](V2reportsGeneType.md) |  | [optional] 
**gene_type** | **str** |  | [optional] 
**rna_type** | [**V2reportsRnaType**](V2reportsRnaType.md) |  | [optional] 
**orientation** | [**V2reportsOrientation**](V2reportsOrientation.md) |  | [optional] 
**locus_tag** | **str** |  | [optional] 
**reference_standards** | [**List[V2reportsGenomicRegion]**](V2reportsGenomicRegion.md) |  | [optional] 
**genomic_regions** | [**List[V2reportsGenomicRegion]**](V2reportsGenomicRegion.md) |  | [optional] 
**transcripts** | [**List[V2reportsTranscript]**](V2reportsTranscript.md) |  | [optional] 
**proteins** | [**List[V2reportsProtein]**](V2reportsProtein.md) |  | [optional] 
**chromosomes** | **List[str]** |  | [optional] 
**swiss_prot_accessions** | **List[str]** |  | [optional] 
**ensembl_gene_ids** | **List[str]** |  | [optional] 
**omim_ids** | **List[str]** |  | [optional] 
**synonyms** | **List[str]** |  | [optional] 
**annotations** | [**List[V2reportsAnnotation]**](V2reportsAnnotation.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_genome_annotation import V2reportsGenomeAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsGenomeAnnotation from a JSON string
v2reports_genome_annotation_instance = V2reportsGenomeAnnotation.from_json(json)
# print the JSON string representation of the object
print(V2reportsGenomeAnnotation.to_json())

# convert the object into a dict
v2reports_genome_annotation_dict = v2reports_genome_annotation_instance.to_dict()
# create an instance of V2reportsGenomeAnnotation from a dict
v2reports_genome_annotation_from_dict = V2reportsGenomeAnnotation.from_dict(v2reports_genome_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


