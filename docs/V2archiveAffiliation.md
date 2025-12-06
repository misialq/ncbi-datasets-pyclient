# V2archiveAffiliation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliation** | **str** |  | [optional] 
**division** | **str** |  | [optional] 
**location** | [**V2archiveLocation**](V2archiveLocation.md) |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2archive_affiliation import V2archiveAffiliation

# TODO update the JSON string below
json = "{}"
# create an instance of V2archiveAffiliation from a JSON string
v2archive_affiliation_instance = V2archiveAffiliation.from_json(json)
# print the JSON string representation of the object
print(V2archiveAffiliation.to_json())

# convert the object into a dict
v2archive_affiliation_dict = v2archive_affiliation_instance.to_dict()
# create an instance of V2archiveAffiliation from a dict
v2archive_affiliation_from_dict = V2archiveAffiliation.from_dict(v2archive_affiliation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


