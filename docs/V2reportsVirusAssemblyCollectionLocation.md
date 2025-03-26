# V2reportsVirusAssemblyCollectionLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geographic_location** | **str** |  | [optional] 
**geographic_region** | **str** |  | [optional] 
**usa_state** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_virus_assembly_collection_location import V2reportsVirusAssemblyCollectionLocation

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsVirusAssemblyCollectionLocation from a JSON string
v2reports_virus_assembly_collection_location_instance = V2reportsVirusAssemblyCollectionLocation.from_json(json)
# print the JSON string representation of the object
print(V2reportsVirusAssemblyCollectionLocation.to_json())

# convert the object into a dict
v2reports_virus_assembly_collection_location_dict = v2reports_virus_assembly_collection_location_instance.to_dict()
# create an instance of V2reportsVirusAssemblyCollectionLocation from a dict
v2reports_virus_assembly_collection_location_from_dict = V2reportsVirusAssemblyCollectionLocation.from_dict(v2reports_virus_assembly_collection_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


