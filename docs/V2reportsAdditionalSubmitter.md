# V2reportsAdditionalSubmitter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genbank_accession** | **str** |  | [optional] 
**refseq_accession** | **str** |  | [optional] 
**chr_name** | **str** |  | [optional] 
**molecule_type** | **str** |  | [optional] 
**submitter** | **str** |  | [optional] 
**bioproject_accession** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_additional_submitter import V2reportsAdditionalSubmitter

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsAdditionalSubmitter from a JSON string
v2reports_additional_submitter_instance = V2reportsAdditionalSubmitter.from_json(json)
# print the JSON string representation of the object
print(V2reportsAdditionalSubmitter.to_json())

# convert the object into a dict
v2reports_additional_submitter_dict = v2reports_additional_submitter_instance.to_dict()
# create an instance of V2reportsAdditionalSubmitter from a dict
v2reports_additional_submitter_from_dict = V2reportsAdditionalSubmitter.from_dict(v2reports_additional_submitter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


