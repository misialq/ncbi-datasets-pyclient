# V2reportsCheckM


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkm_marker_set** | **str** |  | [optional] 
**checkm_species_tax_id** | **int** |  | [optional] 
**checkm_marker_set_rank** | **str** |  | [optional] 
**checkm_version** | **str** |  | [optional] 
**completeness** | **float** |  | [optional] 
**contamination** | **float** |  | [optional] 
**completeness_percentile** | **float** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_check_m import V2reportsCheckM

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsCheckM from a JSON string
v2reports_check_m_instance = V2reportsCheckM.from_json(json)
# print the JSON string representation of the object
print(V2reportsCheckM.to_json())

# convert the object into a dict
v2reports_check_m_dict = v2reports_check_m_instance.to_dict()
# create an instance of V2reportsCheckM from a dict
v2reports_check_m_from_dict = V2reportsCheckM.from_dict(v2reports_check_m_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


