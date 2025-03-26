# V2reportsWGSInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wgs_project_accession** | **str** |  | [optional] 
**master_wgs_url** | **str** |  | [optional] 
**wgs_contigs_url** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_wgs_info import V2reportsWGSInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsWGSInfo from a JSON string
v2reports_wgs_info_instance = V2reportsWGSInfo.from_json(json)
# print the JSON string representation of the object
print(V2reportsWGSInfo.to_json())

# convert the object into a dict
v2reports_wgs_info_dict = v2reports_wgs_info_instance.to_dict()
# create an instance of V2reportsWGSInfo from a dict
v2reports_wgs_info_from_dict = V2reportsWGSInfo.from_dict(v2reports_wgs_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


