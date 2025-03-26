# V2reportsBioSampleId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_bio_sample_id import V2reportsBioSampleId

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsBioSampleId from a JSON string
v2reports_bio_sample_id_instance = V2reportsBioSampleId.from_json(json)
# print the JSON string representation of the object
print(V2reportsBioSampleId.to_json())

# convert the object into a dict
v2reports_bio_sample_id_dict = v2reports_bio_sample_id_instance.to_dict()
# create an instance of V2reportsBioSampleId from a dict
v2reports_bio_sample_id_from_dict = V2reportsBioSampleId.from_dict(v2reports_bio_sample_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


