# V2reportsGenomicLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**genomic_accession_version** | **str** |  | [optional] 
**sequence_name** | **str** |  | [optional] 
**genomic_range** | [**V2reportsRange**](V2reportsRange.md) |  | [optional] 
**exons** | [**List[V2reportsRange]**](V2reportsRange.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_genomic_location import V2reportsGenomicLocation

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsGenomicLocation from a JSON string
v2reports_genomic_location_instance = V2reportsGenomicLocation.from_json(json)
# print the JSON string representation of the object
print(V2reportsGenomicLocation.to_json())

# convert the object into a dict
v2reports_genomic_location_dict = v2reports_genomic_location_instance.to_dict()
# create an instance of V2reportsGenomicLocation from a dict
v2reports_genomic_location_from_dict = V2reportsGenomicLocation.from_dict(v2reports_genomic_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


