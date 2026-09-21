# Ncbiprotddv2ProteinAccessionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessions** | **List[str]** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.ncbiprotddv2_protein_accession_request import Ncbiprotddv2ProteinAccessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of Ncbiprotddv2ProteinAccessionRequest from a JSON string
ncbiprotddv2_protein_accession_request_instance = Ncbiprotddv2ProteinAccessionRequest.from_json(json)
# print the JSON string representation of the object
print(Ncbiprotddv2ProteinAccessionRequest.to_json())

# convert the object into a dict
ncbiprotddv2_protein_accession_request_dict = ncbiprotddv2_protein_accession_request_instance.to_dict()
# create an instance of Ncbiprotddv2ProteinAccessionRequest from a dict
ncbiprotddv2_protein_accession_request_from_dict = Ncbiprotddv2ProteinAccessionRequest.from_dict(ncbiprotddv2_protein_accession_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


