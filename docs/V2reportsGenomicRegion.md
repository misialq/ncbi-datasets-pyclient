# V2reportsGenomicRegion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gene_range** | [**V2reportsSeqRangeSet**](V2reportsSeqRangeSet.md) |  | [optional] 
**type** | [**V2reportsGenomicRegionGenomicRegionType**](V2reportsGenomicRegionGenomicRegionType.md) |  | [optional] [default to V2reportsGenomicRegionGenomicRegionType.UNKNOWN]

## Example

```python
from ncbi.datasets.openapi.models.v2reports_genomic_region import V2reportsGenomicRegion

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsGenomicRegion from a JSON string
v2reports_genomic_region_instance = V2reportsGenomicRegion.from_json(json)
# print the JSON string representation of the object
print(V2reportsGenomicRegion.to_json())

# convert the object into a dict
v2reports_genomic_region_dict = v2reports_genomic_region_instance.to_dict()
# create an instance of V2reportsGenomicRegion from a dict
v2reports_genomic_region_from_dict = V2reportsGenomicRegion.from_dict(v2reports_genomic_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


