# V2reportsBioSampleOwner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**contacts** | [**List[V2reportsBioSampleContact]**](V2reportsBioSampleContact.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_bio_sample_owner import V2reportsBioSampleOwner

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsBioSampleOwner from a JSON string
v2reports_bio_sample_owner_instance = V2reportsBioSampleOwner.from_json(json)
# print the JSON string representation of the object
print(V2reportsBioSampleOwner.to_json())

# convert the object into a dict
v2reports_bio_sample_owner_dict = v2reports_bio_sample_owner_instance.to_dict()
# create an instance of V2reportsBioSampleOwner from a dict
v2reports_bio_sample_owner_from_dict = V2reportsBioSampleOwner.from_dict(v2reports_bio_sample_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


