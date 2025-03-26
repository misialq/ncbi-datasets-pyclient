# V2reportsBioSampleAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_bio_sample_attribute import V2reportsBioSampleAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsBioSampleAttribute from a JSON string
v2reports_bio_sample_attribute_instance = V2reportsBioSampleAttribute.from_json(json)
# print the JSON string representation of the object
print(V2reportsBioSampleAttribute.to_json())

# convert the object into a dict
v2reports_bio_sample_attribute_dict = v2reports_bio_sample_attribute_instance.to_dict()
# create an instance of V2reportsBioSampleAttribute from a dict
v2reports_bio_sample_attribute_from_dict = V2reportsBioSampleAttribute.from_dict(v2reports_bio_sample_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


