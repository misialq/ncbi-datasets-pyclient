# V2reportsGeneDescriptor


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
**orientation** | [**V2reportsOrientation**](V2reportsOrientation.md) |  | [optional] [default to V2reportsOrientation.NONE]
**reference_standards** | [**List[V2reportsGenomicRegion]**](V2reportsGenomicRegion.md) |  | [optional] 
**genomic_regions** | [**List[V2reportsGenomicRegion]**](V2reportsGenomicRegion.md) |  | [optional] 
**chromosomes** | **List[str]** |  | [optional] 
**nomenclature_authority** | [**V2reportsNomenclatureAuthority**](V2reportsNomenclatureAuthority.md) |  | [optional] 
**swiss_prot_accessions** | **List[str]** |  | [optional] 
**ensembl_gene_ids** | **List[str]** |  | [optional] 
**omim_ids** | **List[str]** |  | [optional] 
**synonyms** | **List[str]** |  | [optional] 
**replaced_gene_id** | **str** |  | [optional] 
**annotations** | [**List[V2reportsAnnotation]**](V2reportsAnnotation.md) |  | [optional] 
**transcript_count** | **int** |  | [optional] 
**protein_count** | **int** |  | [optional] 
**transcript_type_counts** | [**List[V2reportsTranscriptTypeCount]**](V2reportsTranscriptTypeCount.md) |  | [optional] 
**gene_groups** | [**List[V2reportsGeneGroup]**](V2reportsGeneGroup.md) |  | [optional] 
**summary** | [**List[V2reportsGeneSummary]**](V2reportsGeneSummary.md) |  | [optional] 
**gene_ontology** | [**V2reportsGeneOntology**](V2reportsGeneOntology.md) |  | [optional] 
**locus_tag** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_gene_descriptor import V2reportsGeneDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsGeneDescriptor from a JSON string
v2reports_gene_descriptor_instance = V2reportsGeneDescriptor.from_json(json)
# print the JSON string representation of the object
print(V2reportsGeneDescriptor.to_json())

# convert the object into a dict
v2reports_gene_descriptor_dict = v2reports_gene_descriptor_instance.to_dict()
# create an instance of V2reportsGeneDescriptor from a dict
v2reports_gene_descriptor_from_dict = V2reportsGeneDescriptor.from_dict(v2reports_gene_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


