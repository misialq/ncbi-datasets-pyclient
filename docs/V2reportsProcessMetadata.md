# V2reportsProcessMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**go_id** | **str** |  | [optional] 
**evidence_code** | **str** |  | [optional] 
**qualifier** | **str** |  | [optional] 
**reference** | [**V2reportsReference**](V2reportsReference.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_process_metadata import V2reportsProcessMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsProcessMetadata from a JSON string
v2reports_process_metadata_instance = V2reportsProcessMetadata.from_json(json)
# print the JSON string representation of the object
print(V2reportsProcessMetadata.to_json())

# convert the object into a dict
v2reports_process_metadata_dict = v2reports_process_metadata_instance.to_dict()
# create an instance of V2reportsProcessMetadata from a dict
v2reports_process_metadata_from_dict = V2reportsProcessMetadata.from_dict(v2reports_process_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


