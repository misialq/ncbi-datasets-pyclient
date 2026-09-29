# V2reportsSequenceFeatureQualifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene** | **str** |  | [optional] 
**gene_synonym** | **str** |  | [optional] 
**locus_tag** | **str** |  | [optional] 
**old_locus_tag** | **str** |  | [optional] 
**allele** | **str** |  | [optional] 
**standard_name** | **str** |  | [optional] 
**map** | **str** |  | [optional] 
**operon** | **str** |  | [optional] 
**product** | **str** |  | [optional] 
**protein_accession** | **str** |  | [optional] 
**translation** | **str** |  | [optional] 
**codon_start** | **str** |  | [optional] 
**transl_table** | **str** |  | [optional] 
**translation_exception** | **List[str]** |  | [optional] 
**ec_number** | **str** |  | [optional] 
**function** | **str** |  | [optional] 
**experiment** | **str** |  | [optional] 
**inference** | **str** |  | [optional] 
**note** | **str** |  | [optional] 
**external_db** | **List[str]** |  | [optional] 
**citation** | **str** |  | [optional] 
**compare** | **str** |  | [optional] 
**number** | **str** |  | [optional] 
**phenotype** | **str** |  | [optional] 
**frequency** | **str** |  | [optional] 
**pseudo** | **bool** |  | [optional] 
**pseudogene** | **str** |  | [optional] 
**ribosomal_slippage** | **bool** |  | [optional] 
**trans_splicing** | **bool** |  | [optional] 
**circular_rna** | **bool** |  | [optional] 
**proviral** | **bool** |  | [optional] 
**germline** | **bool** |  | [optional] 
**rearranged** | **bool** |  | [optional] 
**macronuclear** | **bool** |  | [optional] 
**focus** | **bool** |  | [optional] 
**transgenic** | **bool** |  | [optional] 
**environmental_sample** | **bool** |  | [optional] 
**transcript_accession** | **str** |  | [optional] 
**regulatory_class** | **str** |  | [optional] 
**bound_moiety** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**pcr_conditions** | **str** |  | [optional] 
**pcr_primers** | **str** |  | [optional] 
**repeat_type** | **str** |  | [optional] 
**repeat_family** | **str** |  | [optional] 
**repeat_unit_range** | **str** |  | [optional] 
**repeat_unit_sequence** | **str** |  | [optional] 
**satellite** | **str** |  | [optional] 
**mod_base** | **str** |  | [optional] 
**anticodon** | **str** |  | [optional] 
**tag_peptide** | **str** |  | [optional] 
**estimated_length** | **str** |  | [optional] 
**gap_type** | **str** |  | [optional] 
**linkage_evidence** | **str** |  | [optional] 
**replace** | **str** |  | [optional] 
**recombination_class** | **str** |  | [optional] 
**mobile_element_type** | **str** |  | [optional] 
**nc_rna_class** | **str** |  | [optional] 
**artificial_location** | **str** |  | [optional] 
**exception** | **str** |  | [optional] 
**go_component** | **List[str]** |  | [optional] 
**go_function** | **List[str]** |  | [optional] 
**go_process** | **List[str]** |  | [optional] 
**used_in** | **List[str]** |  | [optional] 
**repeat_unit** | **str** |  | [optional] 
**gene_id** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sequence_feature_qualifier import V2reportsSequenceFeatureQualifier

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSequenceFeatureQualifier from a JSON string
v2reports_sequence_feature_qualifier_instance = V2reportsSequenceFeatureQualifier.from_json(json)
# print the JSON string representation of the object
print(V2reportsSequenceFeatureQualifier.to_json())

# convert the object into a dict
v2reports_sequence_feature_qualifier_dict = v2reports_sequence_feature_qualifier_instance.to_dict()
# create an instance of V2reportsSequenceFeatureQualifier from a dict
v2reports_sequence_feature_qualifier_from_dict = V2reportsSequenceFeatureQualifier.from_dict(v2reports_sequence_feature_qualifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


