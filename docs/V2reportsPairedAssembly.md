# V2reportsPairedAssembly


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**status** | [**V2reportsAssemblyStatus**](V2reportsAssemblyStatus.md) |  | [optional] 
**annotation_name** | **str** |  | [optional] 
**only_genbank** | **str** |  | [optional] 
**only_refseq** | **str** |  | [optional] 
**changed** | **str** |  | [optional] 
**manual_diff** | **str** |  | [optional] 
**refseq_genbank_are_different** | **bool** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_paired_assembly import V2reportsPairedAssembly

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsPairedAssembly from a JSON string
v2reports_paired_assembly_instance = V2reportsPairedAssembly.from_json(json)
# print the JSON string representation of the object
print(V2reportsPairedAssembly.to_json())

# convert the object into a dict
v2reports_paired_assembly_dict = v2reports_paired_assembly_instance.to_dict()
# create an instance of V2reportsPairedAssembly from a dict
v2reports_paired_assembly_from_dict = V2reportsPairedAssembly.from_dict(v2reports_paired_assembly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


