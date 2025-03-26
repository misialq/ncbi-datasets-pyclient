# V2reportsVirusAssembly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**is_complete** | **bool** |  | [optional] 
**is_annotated** | **bool** |  | [optional] 
**isolate** | [**V2reportsIsolate**](V2reportsIsolate.md) |  | [optional] 
**source_database** | **str** |  | [optional] 
**protein_count** | **int** |  | [optional] 
**host** | [**V2reportsOrganism**](V2reportsOrganism.md) |  | [optional] 
**virus** | [**V2reportsOrganism**](V2reportsOrganism.md) |  | [optional] 
**bioprojects** | **List[str]** |  | [optional] 
**location** | [**V2reportsVirusAssemblyCollectionLocation**](V2reportsVirusAssemblyCollectionLocation.md) |  | [optional] 
**update_date** | **str** |  | [optional] 
**release_date** | **str** |  | [optional] 
**nucleotide_completeness** | **str** |  | [optional] 
**completeness** | [**V2reportsVirusAssemblyCompleteness**](V2reportsVirusAssemblyCompleteness.md) |  | [optional] 
**length** | **int** |  | [optional] 
**gene_count** | **int** |  | [optional] 
**mature_peptide_count** | **int** |  | [optional] 
**biosample** | **str** |  | [optional] 
**mol_type** | **str** |  | [optional] 
**nucleotide** | [**V2reportsSeqRangeSetFasta**](V2reportsSeqRangeSetFasta.md) |  | [optional] 
**purpose_of_sampling** | [**V2reportsPurposeOfSampling**](V2reportsPurposeOfSampling.md) |  | [optional] 
**sra_accessions** | **List[str]** |  | [optional] 
**submitter** | [**V2reportsVirusAssemblySubmitterInfo**](V2reportsVirusAssemblySubmitterInfo.md) |  | [optional] 
**lab_host** | **str** |  | [optional] 
**is_lab_host** | **bool** |  | [optional] 
**is_vaccine_strain** | **bool** |  | [optional] 
**segment** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_virus_assembly import V2reportsVirusAssembly

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsVirusAssembly from a JSON string
v2reports_virus_assembly_instance = V2reportsVirusAssembly.from_json(json)
# print the JSON string representation of the object
print(V2reportsVirusAssembly.to_json())

# convert the object into a dict
v2reports_virus_assembly_dict = v2reports_virus_assembly_instance.to_dict()
# create an instance of V2reportsVirusAssembly from a dict
v2reports_virus_assembly_from_dict = V2reportsVirusAssembly.from_dict(v2reports_virus_assembly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


