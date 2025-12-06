# V2reportsVirusPeptide


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**other_names** | **List[str]** |  | [optional] 
**nucleotide** | [**V2reportsSeqRangeSetFasta**](V2reportsSeqRangeSetFasta.md) |  | [optional] 
**protein** | [**V2reportsSeqRangeSetFasta**](V2reportsSeqRangeSetFasta.md) |  | [optional] 
**pdb_ids** | **List[str]** |  | [optional] 
**cdd** | [**List[V2reportsConservedDomain]**](V2reportsConservedDomain.md) |  | [optional] 
**uni_prot_kb** | [**V2reportsVirusPeptideUniProtId**](V2reportsVirusPeptideUniProtId.md) |  | [optional] 
**mature_peptide** | [**List[V2reportsVirusPeptide]**](V2reportsVirusPeptide.md) |  | [optional] 
**protein_completeness** | [**V2reportsVirusPeptideViralPeptideCompleteness**](V2reportsVirusPeptideViralPeptideCompleteness.md) |  | [optional] [default to V2reportsVirusPeptideViralPeptideCompleteness.UNKNOWN]

## Example

```python
from ncbi.datasets.openapi.models.v2reports_virus_peptide import V2reportsVirusPeptide

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsVirusPeptide from a JSON string
v2reports_virus_peptide_instance = V2reportsVirusPeptide.from_json(json)
# print the JSON string representation of the object
print(V2reportsVirusPeptide.to_json())

# convert the object into a dict
v2reports_virus_peptide_dict = v2reports_virus_peptide_instance.to_dict()
# create an instance of V2reportsVirusPeptide from a dict
v2reports_virus_peptide_from_dict = V2reportsVirusPeptide.from_dict(v2reports_virus_peptide_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


