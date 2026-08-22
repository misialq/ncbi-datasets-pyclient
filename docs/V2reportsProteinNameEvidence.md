# V2reportsProteinNameEvidence


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**source_identifier** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_protein_name_evidence import V2reportsProteinNameEvidence

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsProteinNameEvidence from a JSON string
v2reports_protein_name_evidence_instance = V2reportsProteinNameEvidence.from_json(json)
# print the JSON string representation of the object
print(V2reportsProteinNameEvidence.to_json())

# convert the object into a dict
v2reports_protein_name_evidence_dict = v2reports_protein_name_evidence_instance.to_dict()
# create an instance of V2reportsProteinNameEvidence from a dict
v2reports_protein_name_evidence_from_dict = V2reportsProteinNameEvidence.from_dict(v2reports_protein_name_evidence_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


