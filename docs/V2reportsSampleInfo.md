# V2reportsSampleInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clone** | **str** |  | [optional] 
**subclone** | **str** |  | [optional] 
**haplotype** | **str** |  | [optional] 
**genotype** | **str** |  | [optional] 
**sex** | **str** |  | [optional] 
**cell_line** | **str** |  | [optional] 
**cell_type** | **str** |  | [optional] 
**tissue** | **str** |  | [optional] 
**clone_lib** | **str** |  | [optional] 
**dev_stage** | **str** |  | [optional] 
**tissue_lib** | **str** |  | [optional] 
**geo_loc_name** | **str** |  | [optional] 
**lat_lon** | **str** |  | [optional] 
**collection_date** | **str** |  | [optional] 
**collected_by** | **str** |  | [optional] 
**identified_by** | **str** |  | [optional] 
**mating_type** | **str** |  | [optional] 
**phenotype** | **str** |  | [optional] 
**altitude** | **str** |  | [optional] 
**isolation_details** | [**V2reportsIsolationDetails**](V2reportsIsolationDetails.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_sample_info import V2reportsSampleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsSampleInfo from a JSON string
v2reports_sample_info_instance = V2reportsSampleInfo.from_json(json)
# print the JSON string representation of the object
print(V2reportsSampleInfo.to_json())

# convert the object into a dict
v2reports_sample_info_dict = v2reports_sample_info_instance.to_dict()
# create an instance of V2reportsSampleInfo from a dict
v2reports_sample_info_from_dict = V2reportsSampleInfo.from_dict(v2reports_sample_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


