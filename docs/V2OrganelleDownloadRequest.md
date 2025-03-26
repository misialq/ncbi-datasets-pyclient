# V2OrganelleDownloadRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessions** | **List[str]** |  | [optional] 
**exclude_sequence** | **bool** |  | [optional] 
**include_annotation_type** | [**List[V2AnnotationForOrganelleType]**](V2AnnotationForOrganelleType.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2_organelle_download_request import V2OrganelleDownloadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of V2OrganelleDownloadRequest from a JSON string
v2_organelle_download_request_instance = V2OrganelleDownloadRequest.from_json(json)
# print the JSON string representation of the object
print(V2OrganelleDownloadRequest.to_json())

# convert the object into a dict
v2_organelle_download_request_dict = v2_organelle_download_request_instance.to_dict()
# create an instance of V2OrganelleDownloadRequest from a dict
v2_organelle_download_request_from_dict = V2OrganelleDownloadRequest.from_dict(v2_organelle_download_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


