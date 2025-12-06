# V2archiveCatalog


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accession** | **str** |  | [optional] 
**molecule_type** | [**V2archiveMoleculeType**](V2archiveMoleculeType.md) |  | [optional] [default to V2archiveMoleculeType.MOLECULE_TYPE_UNSPECIFIED]
**definition** | **str** |  | [optional] 
**taxonomy** | [**V2archiveTaxonomyNode**](V2archiveTaxonomyNode.md) |  | [optional] 
**sequence** | [**V2archiveSequence**](V2archiveSequence.md) |  | [optional] 
**topology** | [**V2reportsOrganelleTopology**](V2reportsOrganelleTopology.md) |  | [optional] [default to V2reportsOrganelleTopology.TOPOLOGY_UNKNOWN]
**modification_date** | **str** |  | [optional] 
**publication_date** | **str** |  | [optional] 
**submitters** | [**List[V2archiveSubmitter]**](V2archiveSubmitter.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2archive_catalog import V2archiveCatalog

# TODO update the JSON string below
json = "{}"
# create an instance of V2archiveCatalog from a JSON string
v2archive_catalog_instance = V2archiveCatalog.from_json(json)
# print the JSON string representation of the object
print(V2archiveCatalog.to_json())

# convert the object into a dict
v2archive_catalog_dict = v2archive_catalog_instance.to_dict()
# create an instance of V2archiveCatalog from a dict
v2archive_catalog_from_dict = V2archiveCatalog.from_dict(v2archive_catalog_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


