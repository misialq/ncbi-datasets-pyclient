# V2reportsOrganism


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **int** |  | [optional] 
**sci_name** | **str** |  | [optional] 
**organism_name** | **str** |  | [optional] 
**common_name** | **str** |  | [optional] 
**lineage** | [**List[V2reportsLineageOrganism]**](V2reportsLineageOrganism.md) |  | [optional] 
**strain** | **str** |  | [optional] 
**pangolin_classification** | **str** |  | [optional] 
**infraspecific_names** | [**V2reportsInfraspecificNames**](V2reportsInfraspecificNames.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_organism import V2reportsOrganism

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsOrganism from a JSON string
v2reports_organism_instance = V2reportsOrganism.from_json(json)
# print the JSON string representation of the object
print(V2reportsOrganism.to_json())

# convert the object into a dict
v2reports_organism_dict = v2reports_organism_instance.to_dict()
# create an instance of V2reportsOrganism from a dict
v2reports_organism_from_dict = V2reportsOrganism.from_dict(v2reports_organism_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


