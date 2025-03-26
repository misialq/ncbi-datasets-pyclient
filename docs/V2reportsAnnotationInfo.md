# V2reportsAnnotationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**release_date** | **str** |  | [optional] 
**report_url** | **str** |  | [optional] 
**stats** | [**V2reportsFeatureCounts**](V2reportsFeatureCounts.md) |  | [optional] 
**busco** | [**V2reportsBuscoStat**](V2reportsBuscoStat.md) |  | [optional] 
**method** | **str** |  | [optional] 
**pipeline** | **str** |  | [optional] 
**software_version** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**release_version** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_annotation_info import V2reportsAnnotationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsAnnotationInfo from a JSON string
v2reports_annotation_info_instance = V2reportsAnnotationInfo.from_json(json)
# print the JSON string representation of the object
print(V2reportsAnnotationInfo.to_json())

# convert the object into a dict
v2reports_annotation_info_dict = v2reports_annotation_info_instance.to_dict()
# create an instance of V2reportsAnnotationInfo from a dict
v2reports_annotation_info_from_dict = V2reportsAnnotationInfo.from_dict(v2reports_annotation_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


