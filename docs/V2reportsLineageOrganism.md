# V2reportsLineageOrganism


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_lineage_organism import V2reportsLineageOrganism

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsLineageOrganism from a JSON string
v2reports_lineage_organism_instance = V2reportsLineageOrganism.from_json(json)
# print the JSON string representation of the object
print(V2reportsLineageOrganism.to_json())

# convert the object into a dict
v2reports_lineage_organism_dict = v2reports_lineage_organism_instance.to_dict()
# create an instance of V2reportsLineageOrganism from a dict
v2reports_lineage_organism_from_dict = V2reportsLineageOrganism.from_dict(v2reports_lineage_organism_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


