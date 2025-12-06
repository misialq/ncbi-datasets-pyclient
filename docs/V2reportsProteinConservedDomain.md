# V2reportsProteinConservedDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**start** | **int** |  | [optional] 
**stop** | **int** |  | [optional] 
**specific** | **bool** |  | [optional] 
**partial** | **bool** |  | [optional] 
**evalue** | **float** |  | [optional] 
**bit_score** | **float** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_protein_conserved_domain import V2reportsProteinConservedDomain

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsProteinConservedDomain from a JSON string
v2reports_protein_conserved_domain_instance = V2reportsProteinConservedDomain.from_json(json)
# print the JSON string representation of the object
print(V2reportsProteinConservedDomain.to_json())

# convert the object into a dict
v2reports_protein_conserved_domain_dict = v2reports_protein_conserved_domain_instance.to_dict()
# create an instance of V2reportsProteinConservedDomain from a dict
v2reports_protein_conserved_domain_from_dict = V2reportsProteinConservedDomain.from_dict(v2reports_protein_conserved_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


