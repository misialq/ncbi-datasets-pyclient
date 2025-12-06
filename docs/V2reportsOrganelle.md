# V2reportsOrganelle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | [**V2reportsOrganelleType**](V2reportsOrganelleType.md) |  | [optional] [default to V2reportsOrganelleType.ORGANELLE_TYPE_UNKNOWN]
**genbank** | [**V2reportsSequenceInformation**](V2reportsSequenceInformation.md) |  | [optional] 
**refseq** | [**V2reportsSequenceInformation**](V2reportsSequenceInformation.md) |  | [optional] 
**organism** | [**V2reportsOrganism**](V2reportsOrganism.md) |  | [optional] 
**bioprojects** | [**List[V2reportsBioProject]**](V2reportsBioProject.md) |  | [optional] 
**biosample** | [**V2reportsOrganelleBiosample**](V2reportsOrganelleBiosample.md) |  | [optional] 
**gene_counts** | [**V2reportsOrganelleGeneCounts**](V2reportsOrganelleGeneCounts.md) |  | [optional] 
**length** | **int** |  | [optional] 
**topology** | [**V2reportsOrganelleTopology**](V2reportsOrganelleTopology.md) |  | [optional] [default to V2reportsOrganelleTopology.TOPOLOGY_UNKNOWN]
**gene_count** | **int** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_organelle import V2reportsOrganelle

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsOrganelle from a JSON string
v2reports_organelle_instance = V2reportsOrganelle.from_json(json)
# print the JSON string representation of the object
print(V2reportsOrganelle.to_json())

# convert the object into a dict
v2reports_organelle_dict = v2reports_organelle_instance.to_dict()
# create an instance of V2reportsOrganelle from a dict
v2reports_organelle_from_dict = V2reportsOrganelle.from_dict(v2reports_organelle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


