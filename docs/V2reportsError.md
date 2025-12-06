# V2reportsError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembly_error_code** | [**V2reportsErrorAssemblyErrorCode**](V2reportsErrorAssemblyErrorCode.md) |  | [optional] [default to V2reportsErrorAssemblyErrorCode.UNKNOWN_ASSEMBLY_ERROR_CODE]
**gene_error_code** | [**V2reportsErrorGeneErrorCode**](V2reportsErrorGeneErrorCode.md) |  | [optional] [default to V2reportsErrorGeneErrorCode.UNKNOWN_GENE_ERROR_CODE]
**organelle_error_code** | [**V2reportsErrorOrganelleErrorCode**](V2reportsErrorOrganelleErrorCode.md) |  | [optional] [default to V2reportsErrorOrganelleErrorCode.UNKNOWN_ORGANELLE_ERROR_CODE]
**virus_error_code** | [**V2reportsErrorVirusErrorCode**](V2reportsErrorVirusErrorCode.md) |  | [optional] [default to V2reportsErrorVirusErrorCode.UNKNOWN_VIRUS_ERROR_CODE]
**taxonomy_error_code** | [**V2reportsErrorTaxonomyErrorCode**](V2reportsErrorTaxonomyErrorCode.md) |  | [optional] [default to V2reportsErrorTaxonomyErrorCode.UNKNOWN_TAXONOMY_ERROR_CODE]
**reason** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**invalid_identifiers** | **List[str]** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_error import V2reportsError

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsError from a JSON string
v2reports_error_instance = V2reportsError.from_json(json)
# print the JSON string representation of the object
print(V2reportsError.to_json())

# convert the object into a dict
v2reports_error_dict = v2reports_error_instance.to_dict()
# create an instance of V2reportsError from a dict
v2reports_error_from_dict = V2reportsError.from_dict(v2reports_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


