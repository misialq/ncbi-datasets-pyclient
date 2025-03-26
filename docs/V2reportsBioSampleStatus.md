# V2reportsBioSampleStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**when** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_bio_sample_status import V2reportsBioSampleStatus

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsBioSampleStatus from a JSON string
v2reports_bio_sample_status_instance = V2reportsBioSampleStatus.from_json(json)
# print the JSON string representation of the object
print(V2reportsBioSampleStatus.to_json())

# convert the object into a dict
v2reports_bio_sample_status_dict = v2reports_bio_sample_status_instance.to_dict()
# create an instance of V2reportsBioSampleStatus from a dict
v2reports_bio_sample_status_from_dict = V2reportsBioSampleStatus.from_dict(v2reports_bio_sample_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


