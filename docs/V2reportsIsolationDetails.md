# V2reportsIsolationDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metagenomic** | **bool** |  | [optional] 
**metagenome_name** | **str** |  | [optional] 
**metagenome_taxid** | **int** |  | [optional] 
**lab_host** | **str** |  | [optional] 
**natural_host** | **str** |  | [optional] 
**environmental_sample** | **bool** |  | [optional] 
**isolation_source** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_isolation_details import V2reportsIsolationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsIsolationDetails from a JSON string
v2reports_isolation_details_instance = V2reportsIsolationDetails.from_json(json)
# print the JSON string representation of the object
print(V2reportsIsolationDetails.to_json())

# convert the object into a dict
v2reports_isolation_details_dict = v2reports_isolation_details_instance.to_dict()
# create an instance of V2reportsIsolationDetails from a dict
v2reports_isolation_details_from_dict = V2reportsIsolationDetails.from_dict(v2reports_isolation_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


