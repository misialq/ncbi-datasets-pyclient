# V2archiveSubmitter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | [**List[V2archiveName]**](V2archiveName.md) |  | [optional] 
**role** | **str** |  | [optional] 
**affiliation** | [**V2archiveAffiliation**](V2archiveAffiliation.md) |  | [optional] 
**var_date** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2archive_submitter import V2archiveSubmitter

# TODO update the JSON string below
json = "{}"
# create an instance of V2archiveSubmitter from a JSON string
v2archive_submitter_instance = V2archiveSubmitter.from_json(json)
# print the JSON string representation of the object
print(V2archiveSubmitter.to_json())

# convert the object into a dict
v2archive_submitter_dict = v2archive_submitter_instance.to_dict()
# create an instance of V2archiveSubmitter from a dict
v2archive_submitter_from_dict = V2archiveSubmitter.from_dict(v2archive_submitter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


