# V2reportsAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assembly_accession** | **str** |  | [optional] 
**assembly_name** | **str** |  | [optional] 
**annotation_name** | **str** |  | [optional] 
**annotation_release_date** | **str** |  | [optional] 
**genomic_locations** | [**List[V2reportsGenomicLocation]**](V2reportsGenomicLocation.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_annotation import V2reportsAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsAnnotation from a JSON string
v2reports_annotation_instance = V2reportsAnnotation.from_json(json)
# print the JSON string representation of the object
print(V2reportsAnnotation.to_json())

# convert the object into a dict
v2reports_annotation_dict = v2reports_annotation_instance.to_dict()
# create an instance of V2reportsAnnotation from a dict
v2reports_annotation_from_dict = V2reportsAnnotation.from_dict(v2reports_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


