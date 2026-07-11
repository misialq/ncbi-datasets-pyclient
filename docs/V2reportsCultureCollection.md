# V2reportsCultureCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**biocollection_code** | **str** |  | [optional] 

## Example

```python
from ncbi.datasets.openapi.models.v2reports_culture_collection import V2reportsCultureCollection

# TODO update the JSON string below
json = "{}"
# create an instance of V2reportsCultureCollection from a JSON string
v2reports_culture_collection_instance = V2reportsCultureCollection.from_json(json)
# print the JSON string representation of the object
print(V2reportsCultureCollection.to_json())

# convert the object into a dict
v2reports_culture_collection_dict = v2reports_culture_collection_instance.to_dict()
# create an instance of V2reportsCultureCollection from a dict
v2reports_culture_collection_from_dict = V2reportsCultureCollection.from_dict(v2reports_culture_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


