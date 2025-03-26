# V2reportsBioSampleDescription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**organism** | [**V2reportsOrganism**](V2reportsOrganism.md) |  | [optional] 
**comment** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_bio_sample_description import V2reportsBioSampleDescription

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsBioSampleDescription from a JSON string
v2reports_bio_sample_description_instance = V2reportsBioSampleDescription.from_json(json)
# print the JSON string representation of the object
print(V2reportsBioSampleDescription.to_json())

# convert the object into a dict
v2reports_bio_sample_description_dict = v2reports_bio_sample_description_instance.to_dict()
# create an instance of V2reportsBioSampleDescription from a dict
v2reports_bio_sample_description_from_dict = V2reportsBioSampleDescription.from_dict(v2reports_bio_sample_description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


